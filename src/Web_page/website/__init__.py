from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import threading
import time
from website import rfid_checker
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .views import start_threads
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
<<<<<<< HEAD
<<<<<<< HEAD

=======
    
    @app.readrfid
    def rfid_detection_thread():
        while True:
            if rfid_checker.read():
                    from flask import redirect, url_for
                    return redirect(url_for('views.home'))
            time.sleep(1)

    thread = threading.Thread(target=rfid_detection_thread)
    thread.daemon = True
    thread.start()
>>>>>>> ezell
=======
    

>>>>>>> 4b6fe53c825ce7d954f416809c15d66870dcd655

    start_threads()

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')