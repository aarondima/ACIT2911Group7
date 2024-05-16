import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from manage import load_students, load_products, app  # Import the Flask application object
from models import Student, Product, Instructor, Course
from db import db
from routes.html_routes import html_bp
from flask import Flask
from flask_login import LoginManager, login_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

@pytest.fixture(scope='module')
def test_db():
    # Create a test database in memory
    engine = create_engine('sqlite:///:memory:')
    db.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

'''
def test_load_students(test_db):
    with app.app_context():  # Create an application context
        load_students()

def test_load_products(test_db):
    with app.app_context():  # Create an application context
        load_products()
'''
def test_password_hashing(test_db):
    with app.app_context():
        # Create a new user with a known password
        password = 'mypassword'
        student = Student(name='testuser', phone='1234567890', email='testuser@example.com', balance=344.24)

        # Check that the password is not hashed before calling set_password
        assert student.password is None or student.password == password

        student.set_password(password)

        # Check that the password is hashed after calling set_password
        assert student.password is not None and student.password != password

def test_signup_route(test_db):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Configure the application to use an in-memory SQLite database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable event system, which is unnecessary for this test
    app.secret_key = 'test'  # Set the secret_key
    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask application instance

    login_manager = LoginManager()  # Create a LoginManager instance
    login_manager.init_app(app)  # Initialize the LoginManager instance with the Flask application instance

    app.register_blueprint(html_bp)
    with app.app_context():
        db.create_all()  # Create all tables in the database

        # Send a POST request to the /signup route
        with app.test_client() as client:
            response = client.post('/signup', data={
                'name': 'testuser',
                'phone': '1234567890',
                'email': 'testuser@example.com',
                'password': 'mypassword'
            })

            # Check that the response status code is 302 (Redirect)
            assert response.status_code == 302

            # Check that the new user was added to the database
            student = Student.query.filter_by(email='testuser@example.com').first()
            assert student is not None
            assert student.name == 'testuser'
            assert student.phone == '1234567890'
            assert check_password_hash(student.password, 'mypassword')