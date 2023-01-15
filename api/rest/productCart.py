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

@productCart.route('/', methods=["POST"])
@productCart.route('', methods=["POST"] )
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

@productCart.route('/')
@productCart.route('')
def displayProductCarts():
    return jsonify([*map(productCartController.productCartSerializer, productCartController.getAllproductCarts())])


@productCart.route('/<id>')
@productCart.route('<id>')
def getProductCarts(id):
    try:
        productCart = productCartController.read(id)
        return productCartController.productCartSerializer(productCart)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
    
