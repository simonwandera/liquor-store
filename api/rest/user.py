from flask import Blueprint, jsonify, request, json

from .. import db

user = Blueprint('user', __name__, url_prefix='/user')
import jwt 

from api.model.models import User
from api.controllers import authController, userController

@user.route('/register', methods=['POST'])
def register():
    # request_data=json.loads(request.data)
    print(type(request.json))

    if len(request.json):
        return {
            "success": False,
            "message": "Please provide post data"
        }


    first_name=request.json.get('firstName', None)
    other_names=request.json.get('lastName', None)
    gender = request.json['gender']

    dob=request.json['dob']
    email=request.json['email']
    username = request.json['username']

    password=request.json['password']
    confirmPassword=request.json['confirmPassword']

    user = User(first_name = first_name, other_names = other_names,
     gender=gender, dob=dob, email=email, username=username, password=password, confirmPassword = confirmPassword)

    try:
        userController.insert(user)
        return {
            "success": True,
            "Message": "User added successfully"
        }
    except Exception as e:
        return{
            "success": False,
            "message": e
        }