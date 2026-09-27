"""
Email + password authentication for the Loudcase backend.

Deliberately minimal: a single SQLite file (users.db, sitting next to
sessions/ on the same Railway volume) holding one row per user, bcrypt
password hashes (never plaintext), and short-lived JWTs handed back to the
browser on signup/login. The browser stores the JWT in localStorage and
sends it back as `Authorization: Bearer <token>` on requests that should
require a logged-in user (currently: /evaluate).

No signup-verification email is wired up here, but password reset is:
create_password_reset_token()/reset_password_with_token() below, sent via
the Gmail SMTP setup in email_alerts.py.
"""
import hashlib
import os
import re
import secrets
import sqlite3
import time
from pathlib import Path
from typing import Optional

import bcrypt
import jwt

BASE_DIR = Path(__file__).parent

# On Railway (and most PaaS hosts), the container filesystem is ephemeral --
# anything written to it is wiped on every redeploy/restart. DATA_DIR lets
# you point users.db (and sessions/, see server.py) at a mounted persistent
# volume instead. Falls back to sitting next to this file for local dev,
# where that ephemerality doesn't matter.
DATA_DIR = Path(os.environ.get("DATA_DIR", BASE_DIR))
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "users.db"

# In production, set JWT_SECRET on Railway to a long random string. Falling
# back to a fixed dev secret keeps local testing simple, but it means any
# token issued without a real JWT_SECRET set is NOT secure -- fine for
# local dev, not for a real deployment.
JWT_SECRET = os.environ.get("JWT_SECRET", "dev-only-insecure-secret-change-me")
JWT_ALGORITHM = "HS256"
JWT_TTL_SECONDS = 60 * 60 * 24 * 30  # 30 days -- this is a practice tool, not a bank

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


FREE_INTERVIEW_LIMIT = 2

# Premium is marketed as "Unlimited" and should stay that way in the UI --
# this is a quiet fair-use backstop only, well above any realistic prep
# workload (candidates realistically run 15-20 interviews before a real
# one), so no genuine user should ever hit it. It exists purely to bound
# worst-case cost exposure from a one-time $150 charge against per-use
# voice/LLM costs, not to be advertised or shown in the pricing table.
PREMIUM_INTERVIEW_LIMIT = 50

RESET_TOKEN_TTL_SECONDS = 60 * 60  # 1 hour


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at INTEGER NOT NULL
        )
        """
    )

    # Safe migration: add these columns if this is an existing users.db from
    # before Premium existed. SQLite's ADD COLUMN doesn't support "IF NOT
    # EXISTS", so check pragma table_info first instead of assuming a fresh
    # table.
    existing_cols = {row[1] for row in conn.execute("PRAGMA table_info(users)")}
    if "is_premium" not in existing_cols:
        conn.execute("ALTER TABLE users ADD COLUMN is_premium INTEGER NOT NULL DEFAULT 0")
    if "interviews_used" not in existing_cols:
        conn.execute("ALTER TABLE users ADD COLUMN interviews_used INTEGER NOT NULL DEFAULT 0")
    if "reset_token_hash" not in existing_cols:
        conn.execute("ALTER TABLE users ADD COLUMN reset_token_hash TEXT")
    if "reset_token_expires" not in existing_cols:
        conn.execute("ALTER TABLE users ADD COLUMN reset_token_expires INTEGER")
    if "premium_since" not in existing_cols:
        # Nullable, and NOT backfilled for accounts that were already
        # Premium before this column existed -- we have no record of their
        # actual purchase date, so leaving it NULL ("--" in the admin
        # dashboard) is more honest than guessing "today".
        conn.execute("ALTER TABLE users ADD COLUMN premium_since INTEGER")

    # One row per scored interview (i.e. one row per successful /evaluate
    # call), regardless of plan -- this is both the free-tier usage counter
    # source of truth and the Premium "history" data. We always store the
    # FULL scorecard here even for free users (who only ever see the score
    # extract in the API response) so that if they upgrade later, their
    # earlier interviews already have full feedback available in history.
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS interview_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            case_id TEXT NOT NULL,
            session_id TEXT NOT NULL,
            score_summary TEXT,
            scorecard TEXT NOT NULL,
            created_at INTEGER NOT NULL
        )
        """
    )

    # Free-text feedback submitted via the "Feedback" button present
    # throughout the app -- `page` is whatever page the user was on when
    # they opened it (e.g. "session.html"), for context on what they were
    # doing when they hit a bug or had a suggestion.
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            page TEXT,
            message TEXT NOT NULL,
            created_at INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


class AuthError(Exception):
    """Raised for any auth failure -- server.py maps this to an HTTP error."""


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _normalize_email(email: str) -> str:
    return email.strip().lower()


def create_user(email: str, password: str) -> dict:
    email = _normalize_email(email)
    if not EMAIL_RE.match(email):
        raise AuthError("Enter a valid email address.")
    if len(password) < 8:
        raise AuthError("Password must be at least 8 characters.")

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    conn = _get_conn()
    try:
        conn.execute(
            "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
            (email, password_hash, int(time.time())),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise AuthError("An account with that email already exists.")
    finally:
        conn.close()

    return {"email": email}


def verify_login(email: str, password: str) -> dict:
    email = _normalize_email(email)
    conn = _get_conn()
    row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()

    # Same error message either way -- don't reveal whether the email is
    # registered at all.
    invalid = AuthError("Incorrect email or password.")
    if row is None:
        raise invalid
    if not bcrypt.checkpw(password.encode("utf-8"), row["password_hash"].encode("utf-8")):
        raise invalid

    return {"id": row["id"], "email": row["email"]}


def _hash_reset_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_password_reset_token(email: str) -> Optional[str]:
    """Returns a raw, one-time reset token if `email` matches an account,
    else None. Only the token's hash is persisted (like a password), so
    reading the database doesn't hand you a usable token. Callers must
    return the same response to the browser either way -- otherwise this
    becomes a way to check which emails have an account."""
    email = _normalize_email(email)
    conn = _get_conn()
    row = conn.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
    if row is None:
        conn.close()
        return None
    token = secrets.token_urlsafe(32)
    conn.execute(
        "UPDATE users SET reset_token_hash = ?, reset_token_expires = ? WHERE id = ?",
        (_hash_reset_token(token), int(time.time()) + RESET_TOKEN_TTL_SECONDS, row["id"]),
    )
    conn.commit()
    conn.close()
    return token


def reset_password_with_token(token: str, new_password: str) -> None:
    if len(new_password) < 8:
        raise AuthError("Password must be at least 8 characters.")

    conn = _get_conn()
    row = conn.execute(
        "SELECT id, reset_token_expires FROM users WHERE reset_token_hash = ?",
        (_hash_reset_token(token),),
    ).fetchone()
    if row is None or row["reset_token_expires"] is None or row["reset_token_expires"] < int(time.time()):
        conn.close()
        raise AuthError("This reset link is invalid or has expired.")

    password_hash = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    conn.execute(
        "UPDATE users SET password_hash = ?, reset_token_hash = NULL, reset_token_expires = NULL WHERE id = ?",
        (password_hash, row["id"]),
    )
    conn.commit()
    conn.close()


def issue_token(user_id: int, email: str) -> str:
    payload = {
        "sub": str(user_id),
        "email": email,
        "iat": int(time.time()),
        "exp": int(time.time()) + JWT_TTL_SECONDS,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise AuthError("Your session has expired -- please log in again.")
    except jwt.InvalidTokenError:
        raise AuthError("Invalid session token.")
    return payload


def user_from_bearer_header(authorization: Optional[str]) -> dict:
    """`authorization` is the raw `Authorization` header value, expected to
    look like `Bearer <token>`. Raises AuthError if missing/malformed/invalid."""
    if not authorization or not authorization.startswith("Bearer "):
        raise AuthError("Missing or malformed Authorization header.")
    token = authorization[len("Bearer "):].strip()
    payload = decode_token(token)
    return {"id": int(payload["sub"]), "email": payload["email"]}


# ---- Premium / usage ----

def get_billing_status(user_id: int) -> dict:
    conn = _get_conn()
    row = conn.execute(
        "SELECT is_premium, interviews_used FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    conn.close()
    if row is None:
        raise AuthError("User not found.")
    return {
        "is_premium": bool(row["is_premium"]),
        "interviews_used": row["interviews_used"],
        "free_limit": FREE_INTERVIEW_LIMIT,
    }


def set_premium(user_id: int) -> None:
    # COALESCE keeps the original premium_since if this fires more than
    # once for the same user (e.g. a duplicate Stripe webhook delivery)
    # instead of bumping it to "now" on every retry.
    conn = _get_conn()
    conn.execute(
        "UPDATE users SET is_premium = 1, premium_since = COALESCE(premium_since, ?) WHERE id = ?",
        (int(time.time()), user_id),
    )
    conn.commit()
    conn.close()


def set_premium_by_email(email: str) -> None:
    conn = _get_conn()
    cursor = conn.execute(
        "UPDATE users SET is_premium = 1, premium_since = COALESCE(premium_since, ?) WHERE email = ?",
        (int(time.time()), _normalize_email(email)),
    )
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise AuthError(f"No account found for {email}.")


def record_interview(user_id: int, case_id: str, session_id: str, score_summary: str, scorecard: str) -> None:
    """Saves the full scorecard to history and bumps the user's usage
    counter. Called once per successful /evaluate call, for every user
    (free or premium) -- the counter is only ever enforced for free users,
    but we track it for everyone for consistency/analytics."""
    conn = _get_conn()
    conn.execute(
        "INSERT INTO interview_history (user_id, case_id, session_id, score_summary, scorecard, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, case_id, session_id, score_summary, scorecard, int(time.time())),
    )
    conn.execute("UPDATE users SET interviews_used = interviews_used + 1 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


def get_history(user_id: int) -> list:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT case_id, session_id, score_summary, scorecard, created_at "
        "FROM interview_history WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---- Feedback ----

def record_feedback(user_id: int, page: str, message: str) -> None:
    conn = _get_conn()
    conn.execute(
        "INSERT INTO feedback (user_id, page, message, created_at) VALUES (?, ?, ?, ?)",
        (user_id, page, message, int(time.time())),
    )
    conn.commit()
    conn.close()


def get_all_feedback() -> list:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT f.id, u.email, f.page, f.message, f.created_at "
        "FROM feedback f JOIN users u ON u.id = f.user_id "
        "ORDER BY f.created_at DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
