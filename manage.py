import random
from db import db
from FlaskLab import app
from models import Products, Customer, ProductOrder, Order
from sqlalchemy.sql import functions as func
import csv

def create_all_tables():
    db.create_all()

def load_students():
    with open('data/students.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                headers = csv_reader.fieldnames
                name = row['name']
                phone = (row['phone'])
                balance = row['balance']
                student = Student(name=name, , phone=phone, balance=balance)
                db.session.add(student)
                db.session.commit()

def load_teachers():
    with open('data/teachers.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            headers = csv_reader.fieldnames
            name = row['name']
            phone = row['phone']
            teacher = Teacher(name=name, phone=phone)
            db.session.add(teacher)
            db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        drop_all_tables()
        create_all_tables()
        load_students()
        load_teachers()