import pytest
from website import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_lock_button(client):
    # Simulate logging in first (POST request to /login)
    login_data = {
        'email': 'user2@gmail.com',
        'password': 'pass123'
    }
    response = client.post('/login', data=login_data)
    assert response.status_code == 302  # Check if it redirects correctly

    # Follow the redirect to ensure login was successful
    response = client.get(response.headers["Location"], follow_redirects=True)
    assert response.status_code == 200  # Check if the final page loads correctly

    # Simulate pressing the lock button (POST request to /lock_unlock_door)
    lock_data = {'action': 'lock'}
    response = client.post('/lock_unlock_door', json=lock_data, follow_redirects=True)
    assert response.status_code == 200  # Check if the response is successful

    # Verify the presence of success message
    assert b'success' in response.data
