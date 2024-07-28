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

def test_home_redirect(client):
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
    
    # Simulate clicking the home button (GET request to /)
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200  # Check if the final page loads correctly
    
    # Print the response data for debugging
    print(response.data.decode())
    
    # Verify the presence of "START ENGINE" text on the home page
    assert b"START ENGINE" in response.data
