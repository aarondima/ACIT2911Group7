from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
<<<<<<< HEAD

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
=======
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

>>>>>>> adafe8204624f824e262bf8239a3c1ac1ddf309a
