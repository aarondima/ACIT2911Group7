from sqlalchemy import Boolean, Float, Numeric, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime
from db import db

class Student(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False, unique=True)
    phone = mapped_column(String(20), nullable=False)
    balance = mapped_column(Float, nullable=False, default=0)

class Teacher(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False, unique=True)
    phone = mapped_column(String(20), nullable=False)