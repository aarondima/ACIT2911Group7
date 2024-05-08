from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
<<<<<<<<< Temporary merge branch 1

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
=========
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

>>>>>>>>> Temporary merge branch 2
