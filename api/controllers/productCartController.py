from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from api.controllers import userController
from flask import jsonify
from api.model.models import Product_cart
from api import db


def insert(product_cart):

    if product_cart.cart_is == "" or product_cart.cart_id is None:
        raise Exception("Cart id is required")
    if product_cart.cart_is == "" or product_cart.cart_id is None:
        raise Exception("Product id is required")

    db.session.add(product_cart)
    db.session.commit()
    return True

def read(id):
    product_cart = Product_cart.query.filter_by(id=id).first()
    if product_cart:
        return product_cart
    else:
        raise Exception("product cart")

def update(product_cart):
    try:
        db.session.update(product_cart)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid cart id")

def deleteById(id):
    product_cart = read(id)
    if product_cart.cart_id:
        db.session.delete(product_cart)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid product_cart id")

def getAllproduct_cart():
    return Product_cart.query.all()

def getProduct_cartByCart(cart_id):
    return Product_cart.query.filter_by(cart_id=cart_id).all()

def cartSerializer(product_cart):
    return{
        "id": product_cart.id,
        "cart_id": product_cart.cart_id,
        "product_id": product_cart.product_id
    }