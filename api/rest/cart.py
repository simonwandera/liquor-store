from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename

from .. import db
import jwt

from api import create_app


product = Blueprint('cart', __name__, url_prefix='/cart')

from api.model.models import Cart
from api.controllers import cartController
app = create_app()

@product.route('/', methods=["POST"])
@product.route('', methods=["POST"] )
def addProduct():

    owner_id = request.form.get('category_id', None)
    

    cart_x = Cart(owner_id=owner_id)

    try:
        cartController.insert(cart_x)
        return {
            "success": True,
            "msg": "product added successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@product.route('/')
@product.route('')
def displayCarts():
    return jsonify([*map(cartController.cartSerializer, cartController.getAllcarts())])


@product.route('/<id>')
@product.route('<id>')
def getCarts(id):
    try:
        cart = cartController.read(id)
        return cartController.cartSerializer(cart)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
    

