from flask import Blueprint, jsonify, request, json
from datetime import datetime

from .. import db

user = Blueprint('user', __name__, url_prefix='/user')
import jwt 

from api.model.models import User
from api.controllers import authController, userController

@user.route('/')
@user.route('')
def getAllUsers():
    return jsonify([*map(userController.userserializer, userController.getAllUsers())])



@user.route('/', methods=['POST'])
@user.route('', methods=['POST'])
def register():
    # request_data=json.loads(request.data)

    if (request.json is None or len(request.json) == 0):
        return {
            "success": False,
            "message": "Please provide user data"
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
            "message": "User added successfully"
        }
    except Exception as e:
        return{
            "success": False,
            "message": str(e)
        },400