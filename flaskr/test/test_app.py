import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from app.app import app

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ping(client):
    """Tests the /ping endpoint."""
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'pong'}

def test_echo_valid_input(client):
    """Tests the /echo endpoint with valid input."""
    response = client.post('/echo', json={'text': 'hello'})
    assert response.status_code == 200
    assert response.get_json() == {'text': 'hello'}

def test_echo_invalid_input(client):
    """Tests the /echo endpoint with missing input."""
    response = client.post('/echo', json={})  # Missing "text"
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid input'}

def mat_divide(client):
    response = client.post('/math/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200
    assert response.get_json() == {'result': 5}

    response = client.post('/math/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert response.get_json() == {'message': 'Cannot divide by zero'}
