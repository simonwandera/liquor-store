from sqlalchemy.dialects.mysql import INTEGER as Integer
from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    other_names = db.Column(db.String(25), nullable=False)


   
    phone_number = db.Column(db.String(15), nullable=False)
    KRA_pin = db.Column(db.String(20), nullable=True)