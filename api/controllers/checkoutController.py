from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from api.controllers import cartController
from flask import jsonify
from api.model.models import Cart, Product_cart
from api import db


def insert(checkout):

    t_codes = ['QDRWE1234','SUPPORT', 'CHE3409CK']

    if checkout.cart_id == "" or checkout.cart_id is None:
        raise Exception("Cart id is required")
    if checkout.delivery_address == "" or checkout.delivery_address is None:
        raise Exception("Delivery_address is required")
    if checkout.receiver_name == "" or checkout.receiver_name is None:
        raise Exception("Receiver_name is required")
    if checkout.contact == "" or checkout.contact is None:
        raise Exception("contact is required")
    if checkout.alternative_contact == "" or checkout.alternative_contact is None:
        raise Exception("alternative_contact is required")
    if checkout.transaction_code == "" or checkout.transaction_code is None:
        raise Exception("Transaction code is required")
    if checkout.transaction_code not in t_codes:
        raise Exception("Transaction code not recognized")

    db.session.add(checkout)
    cart = cartController.read(checkout.cart_id)
    cart.status = "CHECKEDOUT"
    db.session.commit()

    return True