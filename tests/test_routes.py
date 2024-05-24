import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from manage import load_students, load_products, app
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

def test_load_students(test_db):
    with app.app_context():  # Create an application context
        load_students()

        students = Student.query.all()

        assert len(students) > 0

        first_student = students[0]
        assert first_student.name is not None

def test_load_products(test_db):
    with app.app_context():  # Create an application context
        load_products()
        # Query the database for all products
        products = Product.query.all()

        # Check that the list of products is not empty
        assert len(products) > 0

        # Optionally, you can also check the attributes of the first product to make sure they match what you expect
        first_product = products[0]
        assert first_product.name is not None
        # Add more assertions as needed for other product attributes

def test_password_hashing(test_db):
    with app.app_context():
        password = 'mypassword'
        student = Student(name='testuser', phone='1234567890', email='testuser@example.com', balance=344.24)
        assert student.password is None or student.password == password
        student.set_password(password)
        assert student.password is not None and student.password != password

def test_signup_route(test_db):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.secret_key = 'test'
    db.init_app(app)

    login_manager = LoginManager() 
    login_manager.init_app(app) 

    app.register_blueprint(html_bp)
    with app.app_context():
        db.create_all() 

        with app.test_client() as client:
            response = client.post('/signup', data={
                'name': 'testuser',
                'phone': '1234567890',
                'email': 'testuser@example.com',
                'password': 'mypassword'
            })

            assert response.status_code == 302

            student = Student.query.filter_by(email='testuser@example.com').first()
            assert student is not None
            assert student.name == 'testuser'
            assert student.phone == '1234567890'
            assert check_password_hash(student.password, 'mypassword')

def test_student_model():
    student = Student(name='testuser', phone='1234567890', email='testuser@example.com', balance=344.24)
    assert student.name == 'testuser'
    assert student.phone == '1234567890'
    assert student.email == 'testuser@example.com'
    assert student.balance == 344.24

def test_instructor_model():
    instructor = Instructor(name='Test Instructor', phone='1234567890', email='instructor@example.com')
    assert instructor.name == 'Test Instructor'
    assert instructor.phone == '1234567890'
    assert instructor.email == 'instructor@example.com'

def test_course_model():
    instructor = Instructor(name='Test Instructor', phone='1234567890', email='instructor@example.com')
    course = Course(name='Test Course', duration='1 hour', price=100.00, instructor_id=1, instructor=instructor)
    assert course.name == 'Test Course'
    assert course.duration == '1 hour'
    assert course.price == 100.00
    assert course.instructor_id == 1
    assert course.instructor == instructor
