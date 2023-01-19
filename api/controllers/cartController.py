from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, JWTManager
from api.controllers import userController, productsController, productCartController, cartController
from flask import jsonify
from api.model.models import Cart, Product_cart
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

    return cart
        

def getItemsInCart(userId):
    cart = getActiveUserCart(userId)
    try:
        product_carts = Product_cart.query.filter_by(cart_id=cart.id).all()
        # return [productsController.read(product_cart.product_id) for product_cart in product_carts]

        return product_carts

    except:
        raise Exception("No active cart or invalid cart number")
        


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

def check_product_not_cart(product_id, user_id):

    try:
        cart = cartController.getActiveUserCart(get_jwt_identity())


        if cart is None:
            return {"msg":"cart not available"}

        products_in_cart = Product_cart.query.filter_by(cart_id = cart.id).all()

        for i in products_in_cart:
            if i.product_id == product_id:
                return False

        return True

    except Exception as e:
        
        return False

def get_cart_total(user_id):

    cart = cartController.getActiveUserCart(user_id)

    if cart:
        user_items = Product_cart.query.filter_by(cart_id = cart.id).all()

        total = 0

        for item in user_items:
            
            price = (productsController.read(item.product_id).buy_price) * item.quantity
            total = total + price

        return total
    else:
        return None
