"""
Portfolio Backend — Flask
=========================
Serves the portfolio SPA and handles the contact form API.

Run:  python app.py
Visit: http://localhost:8000
"""

import os
import json
import logging
from pathlib import Path

from flask import Flask, Response, request, jsonify

# ── Local imports ──────────────────────────────────────────────────────────────
from components.page import render_page

# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── App ────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    static_url_path="/static",
)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me-in-production")


# ── Routes ─────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    """Serve the single-page portfolio."""
    html = render_page()
    return Response(html, mimetype="text/html")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "portfolio"})


# ── Contact Form API ───────────────────────────────────────────────────────────
@app.route("/api/contact", methods=["POST"])
def contact():
    """
    Handle contact form submissions.
    Logs the message; plug in SMTP / SendGrid in production.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"detail": "Invalid JSON payload."}), 400

    name    = str(data.get("name", "")).strip()
    email   = str(data.get("email", "")).strip()
    subject = str(data.get("subject", "Portfolio Contact")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify({"detail": "Name, email and message are required."}), 422

    if "@" not in email:
        return jsonify({"detail": "Please provide a valid email address."}), 422

    log.info("📨 New contact — from: %s <%s> | subject: %s", name, email, subject)
    log.info("Message: %s", message[:400])

    # ── TODO: Email integration ─────────────────────────────────────────────
    # Uncomment and set SMTP_HOST / SMTP_USER / SMTP_PASS env vars:
    #
    # import smtplib
    # from email.mime.text import MIMEText
    # smtp_user = os.getenv("SMTP_USER", "")
    # smtp_pass = os.getenv("SMTP_PASS", "")
    # if smtp_user and smtp_pass:
    #     body = f"Name: {name}\nEmail: {email}\n\n{message}"
    #     msg = MIMEText(body)
    #     msg["Subject"] = subject
    #     msg["From"] = smtp_user
    #     msg["To"] = "aatifkhanjodhpur@gmail.com"
    #     with smtplib.SMTP("smtp.gmail.com", 587) as srv:
    #         srv.starttls()
    #         srv.login(smtp_user, smtp_pass)
    #         srv.sendmail(smtp_user, "aatifkhanjodhpur@gmail.com", msg.as_string())
    # ────────────────────────────────────────────────────────────────────────

    return jsonify({
        "success": True,
        "message": "Thanks! I'll get back to you within 24 hours.",
    })


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "true").lower() == "true"
    log.info("🚀  Portfolio running at http://localhost:%d", port)
    app.run(host="0.0.0.0", port=port, debug=debug)
