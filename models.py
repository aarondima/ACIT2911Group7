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
