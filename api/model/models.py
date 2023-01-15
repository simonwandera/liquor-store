from sqlalchemy.dialects.mysql import INTEGER as Integer
from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    other_names = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    usertype = db.Column(db.String(25), nullable=False, default = 'USER')
    password = db.Column(db.String(25), nullable=False)
    confirmPassword = ""
    residence = db.Column(db.String(25), nullable=True)
    pick_up_point = db.Column(db.String(50), nullable=True)

class Product_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), nullable=False)
    text_description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(25), nullable=False)
    product = db.relationship('Product', backref='product_type', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('product_type.id'))
    name = db.Column(db.String(25), nullable=False)
    text_description = db.Column(db.String(1000), nullable=False)
    html_description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(25), nullable=False)
    buy_price = db.Column(db.Integer)
    quantity_in_stock = db.Column(db.Integer, default = 0)
    cart = db.relationship('Product_cart', backref='product', lazy=True)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(25), nullable=False)
    status = db.Column(db.String(25), nullable=False, default = 'ACTIVE')
    cart = db.relationship('Product_cart', backref='cart', lazy=True)

class Product_cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id  = db.Column(db.ForeignKey('cart.id'))
    product_id = db.Column(db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)