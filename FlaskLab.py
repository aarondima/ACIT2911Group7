from flask import Flask, render_template, jsonify, request, redirect, url_for
from pathlib import Path
from sqlalchemy import delete
from datetime import datetime
from db import db
from routes import html_bp
import csv

app = Flask(__name__)
#This will make Flask use a 'sqlite' database with the filename provided
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///i_copy_pasted_this.db"
#This will make Flask store the database file in the path provided
app.instance_path = Path(".").resolve()
#Adjust to your needs / liking. Most likely, you want to use "." for your instance
#path. You may also use "data".
db.init_app(app)

app.register_blueprint(html_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=8888)