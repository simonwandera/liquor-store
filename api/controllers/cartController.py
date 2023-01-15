from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from api.controllers import userController
from flask import jsonify
from api.model.models import Cart
from api import db


def insert(cart):

    if cart.owner_id == "" or cart.owner_id is None:
        raise Exception("Owner id is required")

    db.session.add(cart)
    db.session.commit()
    return True

def read(id):
    cart = Cart.query.filter_by(id=id).first()
    if cart:
        return cart
    else:
        raise Exception("Invalid cart")

def getAllUserCarts(userId):
    cart = Cart.query.filter_by(owner_id=userId).all()
    if cart:
        return cart
    else:
        raise Exception("Invalid userId")

def getActiveUserCart(userId):
    cart = Cart.query.filter_by(owner_id=userId, status = "ACTIVE").first()

    if cart:
        return cart
    else:
        return None;

def update(cart):
    try:
        db.session.update(cart)
        db.session.commit()
        return True
    except:
        raise Exception("Invalid cart id")

def deleteById(id):
    cart = read(id)
    if cart.owner_id:
        db.session.delete(cart)
        db.session.commit()
        return True
    else:
        raise Exception("Invalid cart id")

def getAllcarts():
    return Cart.query.all()

def cartSerializer(cart):
    return{
        "id": cart.id,
        "owner_id": cart.owner_id,
        "status": cart.status
    }