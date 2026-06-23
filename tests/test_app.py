# test_app.py — scaffolded by jira_to_code for ARCH-1218
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # noqa: E402
import pytest  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Verify that the home page loads correctly and has 200 status code."""
    rv = client.get('/')
    assert rv.status_code == 200


def test_background_color_in_css(client):
    """Verify that style.css defines the background-color as orange."""
    rv = client.get('/static/css/style.css')
    assert rv.status_code == 200
    assert b'background-color: orange' in rv.data or b'background-color: #FFA500' in rv.data
