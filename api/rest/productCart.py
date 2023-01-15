from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db
import jwt

from api import create_app


productCart = Blueprint('productCart', __name__, url_prefix='/productCart')

from api.model.models import Product_cart
from api.controllers import productCartController, userController, cartController
app = create_app()

@productCart.route('/add_to_cart', methods=["POST"])
@jwt_required()
def addToCart():

    quantity = request.json.get('quantity')
    product_id = request.json.get('product_id')

    product_cart = Product_cart(product_id = product_id, quantity=quantity)

    try:
        productCartController.insert(product_cart)
        return {
            "success": True,
            "msg": "added to cart successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@productCart.route('/remove_from_cart', methods=["POST"])
@jwt_required()
def remove_from_cart():

    product_id = request.json.get('product_id')
    active_cart = cartController.getActiveUserCart(get_jwt_identity())
    product_cart = Product_cart.query.filter_by(cart_id = active_cart.id, product_id = product_id).first()

    
    if (product_cart is None) or (product_cart.id is None):
        
        return {
            "success": False,
            "msg": "Product not in cart"
        }

    try:
        productCartController.deleteById(product_cart.id)
        return {
            "success": True,
            "msg": "product removed from cart successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@productCart.route('/')
@productCart.route('')
def displayProductCarts():
    return jsonify([*map(productCartController.productCartSerializer, productCartController.getAllproductCarts())])


@productCart.route('/<id>')
@productCart.route('<id>')
def getProductCart(id):
    try:
        productCart = productCartController.read(id)
        return productCartController.productCartSerializer(productCart)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
    

