import pytest
from website import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_aircon_temperature_change(client):
    # Simulate logging in first (POST request to /login)
    login_data = {
        'email': 'user2@gmail.com',
        'password': 'pass123'
    }
    response = client.post('/login', data=login_data)
    assert response.status_code == 302  # Check if it redirects correctly

    # Follow the redirect to ensure login was successful
    client.get(response.headers["Location"], follow_redirects=True)

    # Simulate clicking the start engine button (POST request to /carstart)
    response = client.post('/carstart', follow_redirects=True)
    assert response.status_code == 200  # Check if the final page loads correctly

    # Simulate entering a new aircon temperature (POST request to the relevant endpoint)
    aircon_data = {'temperature': 18}
    response = client.post('/set_aircon_temperature', json=aircon_data, follow_redirects=True)

    # Print the response data for debugging in case of error
    if response.status_code != 200:
        print(response.data.decode())

    assert response.status_code == 200  # Check if the final page loads correctly
    assert response.json['success'] == True  # Ensure the response indicates success
