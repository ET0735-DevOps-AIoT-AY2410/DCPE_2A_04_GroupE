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
        'password2': 'password123',
        'verificationcode': '123'  # Ensure this matches the expected code in the app logic
    }
    response = client.post('/sign-up', data=signup_data)
    
    # Print the response data for debugging
    print(response.data.decode())
    
    # Check if the signup endpoint returned 200 (OK)
    assert response.status_code == 200
    
    # Check for the presence of "Incorrect verification code." message
    assert b"Incorrect verification code." in response.data, "Expected error message not found"
