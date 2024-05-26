import pytest
from flask import url_for
from app import app

@pytest.fixture
def test_index(client):
    response = client.get(url_for('index'))
    assert response.status_code == 200

def test_analyze_text(client):
    response = client.post(url_for('analyze_text'), data={'text': 'This is a test.'})
    assert response.status_code == 200
    assert 'sentiment' in response.get_json()