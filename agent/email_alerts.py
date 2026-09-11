"""
Minimal email alerts via Gmail SMTP -- just enough to notify the admin when
a user submits feedback. Not a general transactional-email system (no
templates, retries, or queue) -- if real user-facing email is ever needed
(signup verification, password reset -- see the TODO in auth.py), swap this
for a proper provider like Resend instead.

Requires two env vars on the host:
  GMAIL_SMTP_USER          -- the Gmail address to send FROM
  GMAIL_SMTP_APP_PASSWORD  -- a Google "App Password" for that account
                              (Google Account -> Security -> 2-Step
                              Verification -> App passwords -- needs 2FA
                              turned on first; a regular Gmail password
                              won't work here)
Optional:
  FEEDBACK_ALERT_EMAIL -- where alerts are sent (defaults to GMAIL_SMTP_USER)
"""
import logging
import os
import smtplib
from email.message import EmailMessage

logger = logging.getLogger("uvicorn.error")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def send_feedback_alert(user_email: str, page: str, message: str) -> None:
    """Best-effort -- logs and swallows any failure instead of raising.
    Feedback is already safely stored in the database by the time this
    runs, so a flaky or misconfigured mail server should never break
    feedback submission itself."""
    smtp_user = os.environ.get("GMAIL_SMTP_USER")
    smtp_password = os.environ.get("GMAIL_SMTP_APP_PASSWORD")
    if not smtp_user or not smtp_password:
        logger.warning(
            "send_feedback_alert: GMAIL_SMTP_USER/GMAIL_SMTP_APP_PASSWORD not set, skipping email alert."
        )
        return

    recipient = os.environ.get("FEEDBACK_ALERT_EMAIL", smtp_user)

    email = EmailMessage()
    email["Subject"] = f"Loudcase feedback from {user_email}"
    email["From"] = smtp_user
    email["To"] = recipient
    email.set_content(
        f"From: {user_email}\nPage: {page or '(unknown)'}\n\n{message}"
    )

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
            smtp.starttls()
            smtp.login(smtp_user, smtp_password)
            smtp.send_message(email)
    except Exception as exc:
        logger.error("send_feedback_alert: failed to send email: %s", exc)
