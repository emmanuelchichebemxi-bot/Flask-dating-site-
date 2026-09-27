"""Minimal Flask application entry point."""

from __future__ import annotations

import os

from flask import Flask


app = Flask(__name__)


@app.get("/")
def index() -> dict[str, str]:
    """Return a welcome response."""
    return {"message": "Hello from Flask!"}


@app.get("/health")
def health() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG", "").lower() == "true",
    )