import os
from app import app


def test_home_page():
    """
    Test that the home page loads successfully and references style.css.
    """
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    assert "style.css" in html


def test_css_orange_color():
    """
    Test that static/css/style.css contains the correct background color code.
    """
    css_path = os.path.join(os.path.dirname(__file__), "..", "static", "css", "style.css")
    assert os.path.exists(css_path)
    with open(css_path, "r") as f:
        content = f.read()
    # Check that body background-color is set to orange or #FFA500
    expected_colors = ["background-color: #FFA500", "background-color: Orange", "background-color: orange"]
    assert any(color in content for color in expected_colors)
