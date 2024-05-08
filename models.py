<<<<<<< HEAD
from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime
from db import db
from flask_login import UserMixin



class Student(UserMixin, db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    phone= mapped_column(String, nullable=False)
    email=mapped_column(String, nullable=False)
    password=mapped_column(String, nullable=False)
    balance = mapped_column(Numeric(10,2), nullable=False)
    enrollments = relationship('Enrollment', back_populates='student')
    
class Order(db.Model):
  id = mapped_column(Integer, primary_key=True)
  date = mapped_column(DateTime, default=datetime.now())
  student_id = mapped_column(Integer, ForeignKey(Student.id), nullable=False)  
  ProductOrders = relationship('ProductOrder', back_populates='order')

    
    
class Instructor(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    phone= mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    courses = relationship('Course', back_populates='instructor')
    
class Course(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    duration=  mapped_column(String, nullable=False)
    price = mapped_column(Numeric(10,2), nullable=False)
    instructor_id = mapped_column(Integer, ForeignKey(Instructor.id), nullable=False)
    instructor = relationship('Instructor', back_populates='courses')
    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(db.Model):
    id = mapped_column(Integer, primary_key=True)
    student_id = mapped_column(Integer, ForeignKey(Student.id), nullable=False)
    course_id = mapped_column(Integer, ForeignKey(Course.id), nullable=False)
    date = mapped_column(DateTime, default=datetime.now())
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')
    
class Product(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    category = mapped_column(String, nullable=False)
    price = mapped_column(Numeric(10,2), nullable=False)
    available = mapped_column(Integer, nullable=True)
    productOrders = relationship('ProductOrder', back_populates='product')
    
    


    
    
class ProductOrder(db.Model):
    id = mapped_column(Integer, primary_key=True)
    order_id = mapped_column(Integer, ForeignKey(Order.id), nullable=False)
    product_id = mapped_column(Integer, ForeignKey(Product.id), nullable=False)
    quantity = mapped_column(Integer, nullable=False)
    order = relationship('Order', back_populates='ProductOrders')
    product = relationship('Product', back_populates='productOrders')    
    
    
=======
from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, relationship
from flask_login import UserMixin
from db import db
from sqlalchemy.sql import func

class Student(UserMixin, db.Model):
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(200), nullable=False, unique=True)
    firstName = mapped_column(String(200), nullable=False)
    lastName = mapped_column(String(200), nullable=False)

    email = mapped_column(String(200), nullable=False, unique=True)
    password = mapped_column(String(200), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastname": self.lastName,
            "email": self.email,
            "password": self.password
        }
>>>>>>> adafe8204624f824e262bf8239a3c1ac1ddf309a
