from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db
import jwt

from api import create_app


cart = Blueprint('cart', __name__, url_prefix='/cart')

from api.model.models import Cart, Product_cart
from api.controllers import cartController, userController
app = create_app()

@cart.route('/', methods=["POST"])
@cart.route('', methods=["POST"] )
def addCart():

    
    cart_x = Cart(owner_id=get_jwt_identity())

    try:
        cartController.insert(cart_x)
        return {
            "success": True,
            "msg": "cart created successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@cart.route('/')
@cart.route('')
def displayCarts():
    return jsonify([*map(cartController.cartSerializer, cartController.getAllcarts())])


@cart.route('/<id>')
@cart.route('<id>')
def getCarts(id):
    try:
        cart = cartController.read(id)
        return cartController.cartSerializer(cart)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
    

