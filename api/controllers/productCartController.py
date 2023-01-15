from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from api.controllers import userController, cartController
from flask import jsonify
from api.model.models import Product_cart, Cart
from api import db


def insert(product_cart):

   
    if product_cart.product_id == "" or product_cart.product_id is None:
        raise Exception("Product id is required")
    if product_cart.quantity == "" or product_cart.quantity is None or product_cart.quantity == 0:
        raise Exception("Product quantity should be greater than 0")

    active_carts = cartController.getActiveUserCarts(get_jwt_identity())

    if len(active_carts) > 0:
        cart_x = active_carts[0]
    else:
        new_cart = Cart(owner_id=get_jwt_identity())
        cartController.insert(new_cart)
        cart_x = cartController.getActiveUserCarts(get_jwt_identity())[0]

    product_cart.cart_id = cart_x.id

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

def getAllproductCarts():
    return Product_cart.query.all()

def getProduct_cartByCart(cart_id):
    return Product_cart.query.filter_by(cart_id=cart_id).all()

def productCartSerializer(product_cart):
    return{
        "id": product_cart.id,
        "cart_id": product_cart.cart_id,
        "product_id": product_cart.product_id,
        "quatity": product_cart.quantity
    }