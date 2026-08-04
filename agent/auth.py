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
DB_PATH = BASE_DIR / "users.db"

# In production, set JWT_SECRET on Railway to a long random string. Falling
# back to a fixed dev secret keeps local testing simple, but it means any
# token issued without a real JWT_SECRET set is NOT secure -- fine for
# local dev, not for a real deployment.
JWT_SECRET = os.environ.get("JWT_SECRET", "dev-only-insecure-secret-change-me")
JWT_ALGORITHM = "HS256"
JWT_TTL_SECONDS = 60 * 60 * 24 * 30  # 30 days -- this is a practice tool, not a bank

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


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
