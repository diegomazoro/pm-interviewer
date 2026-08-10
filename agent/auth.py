"""
Email + password authentication for the Loudcase backend.

Deliberately minimal: a single SQLite file (users.db, sitting next to
sessions/ on the same Railway volume) holding one row per user, bcrypt
password hashes (never plaintext), and short-lived JWTs handed back to the
browser on signup/login. The browser stores the JWT in localStorage and
sends it back as `Authorization: Bearer <token>` on requests that should
require a logged-in user (currently: /evaluate).

No email-sending is wired up here (no verification email, no password
reset email yet) -- that needs a transactional email provider (e.g.
Resend) and a bit more plumbing, and can be added as a follow-up once
basic login is working end-to-end.
"""
import os
import re
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


FREE_INTERVIEW_LIMIT = 5


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
    conn = _get_conn()
    conn.execute("UPDATE users SET is_premium = 1 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


def set_premium_by_email(email: str) -> None:
    conn = _get_conn()
    conn.execute("UPDATE users SET is_premium = 1 WHERE email = ?", (_normalize_email(email),))
    conn.commit()
    conn.close()


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
