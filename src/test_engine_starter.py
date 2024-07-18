import pytest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Web_page')))

from Web_page.website import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_car_start_button(client):
  
    response = client.post('/carstart')
    assert response.status_code == 302  

    
    response = client.get('/car_menu', follow_redirects=True)
    assert response.status_code == 200  
    assert b'Engine started successfully!' in response.data  

if __name__ == '__main__':
    pytest.main()
