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

def test_login(client):
    # Simulate logging in (POST request to /login)
    login_data = {
        'email': 'user2@gmail.com',
        'password': 'pass123'
    }
    response = client.post('/login', data=login_data)
    
    # Print the response data for debugging
    print(response.data.decode())
    
    # Check if the login endpoint returned 200 (OK)
    if response.status_code == 200:
        # Inspect the response content
        assert b"Invalid credentials" not in response.data, "Login failed: Invalid credentials"
        assert b"Login successful" in response.data, "Login successful message not found"
    
    # Assert that the response status code is 302 (redirect)
    assert response.status_code == 302  # Check if it redirects correctly
    
    # Follow the redirect
    redirect_response = client.get(response.headers["Location"], follow_redirects=True)
    assert redirect_response.status_code == 200  # Check if the final page loads correctly
    
    # Print the response data for debugging
    print(redirect_response.data.decode())
    
    # Verify the presence of "START ENGINE" text on the redirected page
    assert b"START ENGINE" in redirect_response.data
