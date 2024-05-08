
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from models import Student
from db import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"

 
login_manager = LoginManager()
login_manager.init_app(app)
 
 
 
db.init_app(app)
 
 
@login_manager.user_loader
def loader_user(user_id):
    return Student.query.get(user_id)
 
 
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        student = Student(username=request.form.get("username"),
                       firstName=request.form.get("firstName"),
                       lastName=request.form.get("lastName"),
                       email=request.form.get("email"),
                     password=request.form.get("password"))
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        student = Student.query.filter_by(
            username=request.form.get("username")).first()
        print(student)
        if student.password == request.form.get("password"):
            login_user(student)
            return redirect(url_for("home"))
    return render_template("login.html")
 
 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
 
 
@app.route("/")
def home():
    return render_template("home.html")
 
 
if __name__ == "__main__":
    app.run(debug=True, port=8888)
