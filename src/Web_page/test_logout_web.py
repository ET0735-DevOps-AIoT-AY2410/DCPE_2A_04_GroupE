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

def test_logout(client):
    # Simulate logging in first (POST request to /login)
    login_data = {
        'email': 'user2@gmail.com',
        'password': 'pass123'
    }
    response = client.post('/login', data=login_data)
    assert response.status_code == 302  # Check if it redirects correctly

    # Follow the redirect to ensure login was successful
    client.get(response.headers["Location"], follow_redirects=True)
    
    # Simulate logging out (GET request to /logout)
    response = client.get('/logout')
    assert response.status_code == 302  # Check if it redirects correctly
    
    # Follow the redirect to the login page
    redirect_response = client.get(response.headers["Location"], follow_redirects=True)
    assert redirect_response.status_code == 200  # Check if the login page loads correctly
    
    # Print the response data for debugging
    print(redirect_response.data.decode())
    
    # Verify the presence of "Login" text on the login page
    assert b"Login" in redirect_response.data
