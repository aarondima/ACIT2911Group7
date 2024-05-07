import random
from db import db
from FlaskLab import app
from models import Student, Product, Course, Instructor
from sqlalchemy.sql import functions as func
import csv
from werkzeug.security import generate_password_hash



def load_students():
    with  open('./data/students.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            student = Student(name=row[0], phone=row[1], balance=float(row[2]),password=generate_password_hash("password", method='sha256'),email=row[3])
            db.session.add(student)
        db.session.commit()
    
def load_products():
    with open('./data/products.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] == "NA":
                product = Product(name=row[0], price=row[2],category=row[1], available=None)
            else:
                product = Product(name=row[0], price=row[2],category=row[1], available=row[3])
            db.session.add(product)
        db.session.commit()
    
def load_courses():
    with open('./data/courses.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            course = Course(name=row[0], duration=row[1], price=row[2], instructor_id=row[3])
            db.session.add(course)
        db.session.commit()

def load_instructors():
    with open('./data/teachers.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            instructor = Instructor(name=row[0], phone=row[1], email=row[2])
            db.session.add(instructor)
        db.session.commit()
        
def drop_all_tables():
    db.drop_all()   
    
def create_all_tables():
    db.create_all()
    load_students()
    load_products()
    load_instructors()
    load_courses()
    
if __name__ == "__main__":
    with app.app_context():
        drop_all_tables()
        create_all_tables()
        
        # append_random_data()