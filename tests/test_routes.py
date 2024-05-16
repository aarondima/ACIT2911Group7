import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from manage import load_students, load_products, app  # Import the Flask application object
from models import Student, Product
from db import db
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