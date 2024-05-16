import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from manage import load_students, load_products, app  # Import the Flask application object
from models import Student, Product
from db import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash

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

def test_load_products(test_db):
    with app.app_context():  # Create an application context
        load_products()