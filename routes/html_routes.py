from flask import Flask, render_template, jsonify, request, redirect, url_for, Blueprint
from pathlib import Path
from sqlalchemy import delete
from datetime import datetime
from db import db
import csv
from models import Student
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask_login import login_required, current_user


html_bp = Blueprint("html", __name__)

@html_bp.route("/")
@login_required
def home():
    return render_template("base.html")

@html_bp.route("/courses")
def show_courses():
    return render_template("courses.html")

@html_bp.route("/students")
def show_students():
    return render_template("students.html")

@html_bp.route("/products")
def show_products():
    return render_template("products.html")

@html_bp.route("/auth")
def register_page():
    return render_template("register.html")

@html_bp.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    password = request.form["password"]
    student = Student(name=name, phone=phone, email=email, password=generate_password_hash(password, method='sha256'),balance=0.0)
    db.session.add(student)
    db.session.commit()
    login_user(student, remember=True)
    return redirect(url_for("html.home"))

@html_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('html.register_page'))

@html_bp.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    student = Student.query.filter_by(email=email).first()
    if student and check_password_hash(student.password, password):
        login_user(student, remember=True)
        return redirect(url_for("html.home"))
    else:
        return redirect(url_for("html.register_page"))