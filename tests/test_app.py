import os
import sys

# Force importing the local app.py rather than the parent system app package
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if "/code" in sys.path:
    sys.path.remove("/code")

import app as flask_module
flask_app = flask_module.app


def test_css_color():
    """Verify that the page color is set to orange."""
    css_path = os.path.join(os.path.dirname(__file__), "../static/css/style.css")
    assert os.path.exists(css_path), f"CSS file does not exist at {css_path}"
    with open(css_path, "r") as f:
        content = f.read()
    assert "background-color: orange;" in content, "Background color is not set to orange in CSS"


def test_home_page():
    """Verify that the home page returns 200 OK."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
