import random
from db import db
from FlaskLab import app
from models import Products, Customer, ProductOrder, Order
from sqlalchemy.sql import functions as func
import csv
if __name__ == "__main__":
    with app.app_context():
        drop_all_tables()
        create_all_tables()
        load_customers()
        load_products()
        append_random_data()