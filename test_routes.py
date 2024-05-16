import pytest
from ACIT2911Group7.routes import html_bp
from ACIT2911Group7.app import Flask
from ACIT2911Group7.db import db
from ACIT2911Group7.models import Student, Course, Instructor, Enrollment  # Import necessary models

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(html_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/home')
    assert response.status_code == 200

'''

def test_show_courses_route(client):
    response = client.get('/courses')
    assert response.status_code == 200  # Assuming the route is accessible without login

# Add tests for other routes...

def test_signup_route(client):
    response = client.post('/signup', data=dict(
        name='Test User',
        phone='1234567890',
        email='test@example.com',
        password='password'
    ))
    assert response.status_code == 302  # Redirects to home page after successful signup

def test_logout_route(client):
    response = client.get('/logout')
    assert response.status_code == 302  # Redirects to login page after logout

def test_login_route(client):
    # Assuming there's a test user created before
    student = Student(name='Test User', phone='1234567890', email='test@example.com', password='password')
    db.session.add(student)
    db.session.commit()

    response = client.post('/login', data=dict(
        email='test@example.com',
        password='password'
    ))
    assert response.status_code == 302  # Redirects to home page after successful login
'''