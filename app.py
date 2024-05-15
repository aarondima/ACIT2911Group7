
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from models import Student
from db import db
from routes import html_bp
import csv
from flask_login import LoginManager
from models import Student 

from pathlib import Path 
app = Flask(__name__)
# This will make Flask use a 'sqlite' database with the filename provided
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///i_copy_pasted_this.db"
app.config['SECRET_KEY'] = 'u5evZUBcwG6jXyH2LgVbdRMm9CFShPrENtD4nW3sAkTJQxqKYa'
# This will make Flask store the database file in the path provided
app.instance_path = Path(".").resolve()
# Adjust to your needs / liking. Most likely, you want to use "." for your instance
# path. You may also use "data".
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'html.register_page'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query forthe user
    return Student.query.get(int(user_id))


app.register_blueprint(html_bp, url_prefix="/")

# if __name__ == "__main__":
#     app.run(debug=True, port=8888)
