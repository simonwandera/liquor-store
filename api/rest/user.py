from flask import Blueprint, jsonify, request
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

from .. import db

user = Blueprint('user', __name__, url_prefix='/user')
import jwt 

from api.model.models import User
from api.controllers import cartController, userController,productsController, productCartController

@user.route('/')
@user.route('')
def getAllUsers():
    return jsonify([*map(userController.userserializer, userController.getAllUsers())])


@user.route('/cart', methods=['GET'])
@jwt_required()
def userCart():
    return jsonify(cartController.cartSerializer(cartController.getActiveUserCart(get_jwt_identity())))

@user.route('/items_in_cart', methods=['GET'])
@jwt_required()
def items_in_cart():
    
    try:
        return jsonify([*map(productCartController.productCartSerializer, cartController.getItemsInCart(get_jwt_identity()))])

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400


@user.route('/', methods=['POST'])
@user.route('', methods=['POST'])
def register():

    if (request.json is None or len(request.json) == 0):
        return {
            "success": False,
            "msg": "Please provide user data"
        }, 400

    first_name=request.json.get('firstName', None)
    other_names=request.json.get('lastName', None)
    gender = request.json.get('gender')

    dob=request.json.get('dob')
    email=request.json.get('email')
    phone=request.json.get('phone')
    username = request.json.get('username')

    password=request.json.get('password')
    confirmPassword=request.json.get('confirmPassword')

    # dob = datetime.strptime(dob, '%Y-%m-%d').date()

    user = User(first_name = first_name, other_names = other_names, phone = phone,
     gender=gender, dob=dob, email=email, username=username, password=password, confirmPassword = confirmPassword)

    try:
        userController.insert(user)
        return {
            "success": True,
            "msg": "User added successfully"
        }
    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400