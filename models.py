from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, DateTime, Column
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import UserMixin
from ACIT2911Group7.db import db

class Student(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone= Column(String, nullable=False)
    email=Column(String, nullable=False)
    password=Column(String, nullable=False)
    balance = Column(Numeric(10,2), nullable=False)
    enrollments = relationship('Enrollment', back_populates='student')
    
class Order(db.Model):
  id = Column(Integer, primary_key=True)
  date = Column(DateTime, default=datetime.now)
  student_id = Column(Integer, ForeignKey(Student.id), nullable=False)  
  product_orders = relationship('ProductOrder', back_populates='order')

class Instructor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone= Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship('Course', back_populates='instructor')
    
class Course(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    duration=  Column(String, nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    instructor_id = Column(Integer, ForeignKey(Instructor.id), nullable=False)
    instructor = relationship('Instructor', back_populates='courses')
    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(db.Model):
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    course_id = Column(Integer, ForeignKey(Course.id), nullable=False)
    date = Column(DateTime, default=datetime.now)
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')
    
class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    available = Column(Integer, nullable=True)
    product_orders = relationship('ProductOrder', back_populates='product')
    
class ProductOrder(db.Model):
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    quantity = Column(Integer, nullable=False)
    order = relationship('Order', back_populates='product_orders')
    product = relationship('Product', back_populates='product_orders')