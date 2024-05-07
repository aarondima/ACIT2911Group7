from flask import Flask, render_template, jsonify, request, redirect, url_for, Blueprint
from pathlib import Path
from sqlalchemy import delete
from datetime import datetime
from db import db
import csv

html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def home():
    return render_template("base.html")