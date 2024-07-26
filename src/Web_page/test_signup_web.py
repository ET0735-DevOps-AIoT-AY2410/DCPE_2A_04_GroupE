import pytest
import time
from website import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_signup(client):
    # Create a unique email using the current time
    unique_email = f"testuser{int(time.time())}@example.com"
    
    # Simulate signing up (POST request to /sign-up)
    signup_data = {
        'username': 'testuser',
        'email': unique_email,
        'firstName': 'Test',
        'password1': 'password123',
        'password2': 'password123'
    }
    response = client.post('/sign-up', data=signup_data)
    
    assert response.status_code == 302  # Check if it redirects correctly
    
    # Follow the redirect
    redirect_response = client.get(response.headers["Location"], follow_redirects=True)
    assert redirect_response.status_code == 200  # Check if the final page loads correctly
    
    # Print the response data for debugging
    print(redirect_response.data.decode())
    
    
    assert b"START ENGINE" in redirect_response.data
