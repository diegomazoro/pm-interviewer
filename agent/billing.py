"""
Stripe integration for the one-time $150 Premium upgrade.

Uses Stripe Checkout (Stripe's own hosted payment page) rather than
collecting card details ourselves -- this backend never sees or touches
card numbers, which is both simpler and the right way to handle payment
data. The Checkout Session is created with inline `price_data` rather
than a pre-created Stripe Price object, so nothing needs to be manually
set up in the Stripe dashboard beyond having an account and API keys.

Required environment variables (set these on Railway, not in code):
- STRIPE_SECRET_KEY: your Stripe secret key (sk_live_... or sk_test_...
  while testing). Get it from https://dashboard.stripe.com/apikeys
- STRIPE_WEBHOOK_SECRET: the signing secret for the webhook endpoint you
  create in the Stripe dashboard pointing at
  <your-backend-url>/billing/webhook (whsec_...). Get it after creating
  that webhook endpoint at https://dashboard.stripe.com/webhooks
"""
import json
import os

import stripe

PREMIUM_PRICE_USD_CENTS = 15000  # $150.00, one-time


class BillingError(Exception):
    """Raised for any billing failure -- server.py maps this to an HTTP error."""


def _get_secret_key() -> str:
    key = os.environ.get("STRIPE_SECRET_KEY")
    if not key:
        raise BillingError("STRIPE_SECRET_KEY is not set on the server.")
    return key


def create_checkout_session(user_id: int, email: str, success_url: str, cancel_url: str) -> str:
    """Creates a Stripe Checkout Session for the one-time Premium purchase
    and returns its hosted URL, which the browser should redirect to.
    `client_reference_id` carries our user id through to the webhook, so
    we know which account to mark Premium once payment completes."""
    stripe.api_key = _get_secret_key()
    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            customer_email=email,
            client_reference_id=str(user_id),
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": PREMIUM_PRICE_USD_CENTS,
                        "product_data": {
                            "name": "Loudcase Premium",
                            "description": "Unlimited live case interviews, detailed feedback, "
                                            "and full score history -- lifetime access, one-time payment.",
                        },
                    },
                    "quantity": 1,
                }
            ],
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={"user_id": str(user_id), "email": email},
        )
    except stripe.error.StripeError as exc:
        raise BillingError(f"Stripe error: {exc.user_message or str(exc)}")
    except Exception as exc:
        # Anything below the Stripe SDK's own error hierarchy (network
        # issues, proxy config, etc.) -- still fail cleanly with a 500
        # instead of leaking a raw traceback to the client.
        raise BillingError(f"Could not reach Stripe: {exc}")
    return session.url


def verify_webhook(payload: bytes, sig_header: str) -> dict:
    """Verifies the webhook signature and returns the event as a plain
    dict. Raises BillingError if the signature doesn't check out --
    callers should treat that as a 400, not silently trust the payload,
    since anyone can POST arbitrary JSON to a webhook URL.

    construct_event() is used ONLY to verify the signature -- its return
    value is a stripe.StripeObject whose attribute/dict-access behavior
    varies across SDK versions (a plain `.get()` raised AttributeError
    when tested against the installed version here). Once the signature
    is confirmed valid, we parse the same already-verified raw payload
    ourselves as plain JSON instead, which is predictable regardless of
    SDK version."""
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET")
    if not webhook_secret:
        raise BillingError("STRIPE_WEBHOOK_SECRET is not set on the server.")
    try:
        stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except (ValueError, stripe.error.SignatureVerificationError) as exc:
        raise BillingError(f"Invalid webhook signature: {exc}")
    return json.loads(payload)


def user_id_from_checkout_event(event: dict) -> "int | None":
    """Pulls the user id back out of a checkout.session.completed event,
    preferring client_reference_id (set at session creation) with
    metadata.user_id as a fallback."""
    obj = event.get("data", {}).get("object", {})
    ref = obj.get("client_reference_id") or obj.get("metadata", {}).get("user_id")
    return int(ref) if ref else None
