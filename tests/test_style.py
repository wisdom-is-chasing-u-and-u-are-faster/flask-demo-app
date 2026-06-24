import os
import re
import sys

# Ensure flask-demo-app directory is at the absolute top of sys.path to avoid importing other "app" packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # noqa: E402


def test_css_background_color():
    # 1. Verify the CSS file exists and has background-color: orange;
    css_path = os.path.join(os.path.dirname(__file__), "../static/css/style.css")
    assert os.path.exists(css_path), "style.css should exist"

    with open(css_path, "r") as f:
        content = f.read()

    # Clean whitespace and look for body background color
    body_match = re.search(r"body\s*\{([^}]+)\}", content)
    assert body_match is not None, "CSS should contain body style"
    body_styles = body_match.group(1)
    assert "background-color:" in body_styles, "body style should specify background-color"
    assert "orange" in body_styles.lower() or "#ffa500" in body_styles.lower(), "body background-color should be orange"


def test_flask_serves_css():
    # 2. Verify Flask app serves style.css successfully
    client = app.test_client()
    response = client.get("/static/css/style.css")
    assert response.status_code == 200, "Flask should serve style.css"
    assert b"background-color: orange" in response.data, "Served CSS should contain orange background color"
