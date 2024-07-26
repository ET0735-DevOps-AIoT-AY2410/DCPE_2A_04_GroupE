import pytest
from website import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_carstart_button(client):
    # Simulate pressing the button (POST request to /carstart)
    response = client.post('/carstart')
    assert response.status_code == 302  # Check if it redirects correctly

    # Follow the redirect (GET request to /car_menu)
    response = client.get('/car_menu', follow_redirects=True)
    assert response.status_code == 200  # Check if it loads correctly
