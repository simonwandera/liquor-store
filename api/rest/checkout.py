from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db
import jwt

from api import create_app

checkout = Blueprint('checkout', __name__, url_prefix='/checkout')

from api.model.models import Checkout, Product_cart
from api.controllers import cartController, checkoutController

app = create_app()

@checkout.route('/', methods=["POST"])
@checkout.route('', methods=["POST"])
@jwt_required()
def check_out():

    cart_id = request.json.get('cart_id')
    delivery_address = request.json.get('delivery_address')
    receiver_name = request.json.get('receiver_name')
    contact = request.json.get('contact')
    alternative_contact = request.json.get('alternative_contact')
    transaction_code = request.json.get('transaction_code')

    checkout = Checkout(cart_id = cart_id, delivery_address = delivery_address, receiver_name = receiver_name, contact = contact, alternative_contact = alternative_contact, transaction_code = transaction_code)
    
    try:
        checkoutController.insert(checkout)
        return {
            "success": True,
            "msg": "Checkouted out successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400



