import pytest
from Web_page.website import create_app, db
from Web_page.website.models import User
from flask_login import login_user
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "LOGIN_DISABLED": False,
        "WTF_CSRF_ENABLED": False
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_signup_and_carstart(client, app):
    # Sign up the user
    response = client.post('/sign-up', data=dict(
        email='test1@gmail.com',
        firstName='Test1',
        password1='test1234',
        password2='test1234'
    ), follow_redirects=True)
    assert response.status_code == 200

    # Log in the user
    with app.app_context():
        user = User.query.filter_by(email='test1@gmail.com').first()
        login_user(user)

        with client.session_transaction() as sess:
            sess['_user_id'] = str(user.id)

    # Test carstart route
    response = client.post('/carstart', follow_redirects=True)
    assert response.status_code == 200
    assert b'Car Control Dashboard' in response.data

if __name__ == "__main__":
    pytest.main()
