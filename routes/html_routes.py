from flask import Flask, render_template, jsonify, request, redirect, url_for, Blueprint, flash, session
from pathlib import Path
from sqlalchemy import delete
from datetime import datetime
from db import db
import csv
from models import Student, Course, Instructor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask_login import login_required, current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role == "Admin":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.")
            return redirect(url_for("html.home"))
    return wrap

html_bp = Blueprint("html", __name__)


@html_bp.route("/home")
@html_bp.route("/")
@login_required
def home():
    return render_template("home.html",name=current_user.name)

@html_bp.route("/courses")
def show_courses():
    data=db.select(Course).order_by(Course.name).where(Instructor.id == Course.instructor_id)
    result= db.session.execute(data).scalars()
    return render_template("courses.html",ins_courses=result)

@html_bp.route("/feedback/", methods=["POST", "GET"])
def show_feedback():
    data=db.select(Course).order_by(Course.name)
    result= db.session.execute(data).scalars()
    result= db.session.execute(data).scalars()
    if request.method == "POST":
        return "<h1>for feedback submitted</h1>"
    elif request.method == "GET":
        return render_template("feedback.html",courses=result)

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
    role = request.form["role"]
    if Student.query.filter_by(email=email).first():
        return redirect(url_for("html.register_page"))
    student = Student(name=name, phone=phone, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'),balance=0.0, role=role)
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
        session['username'] = student.name
        return redirect(url_for("html.home"))
    else:
        return redirect(url_for("html.register_page"))
    
@html_bp.route("/admin")
@login_required
@admin_required
def admin_resource():
    return render_template("admin.html")

@html_bp.route('/clear_session/<int:user_id>', methods=['GET'])

@login_required
def clear_session(user_id):
    # Check if the user exists or perform any other validation
    # Here, we'll simply clear the session if the user ID matches
    # return f"{user_id}"
    user = session.get('username')
    return f"{user}"
    if user_id == session.get('user_id'):
        # session.clear()
        # return redirect(url_for('index'))
        return "Hello this is the user"
    else:
        return "User ID does not match. Unable to clear session."