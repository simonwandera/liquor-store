from api.model.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from api.controllers import userController
from flask import jsonify


def login(username, password):

    if (username == "" or username is None):
        raise Exception("Username is required to login")
    if (password == "" or password is None):
        raise Exception("Password is required to login")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        raise Exception('Please check your login details and try again.')
    
    message = {
        "token": create_access_token(identity=username),
        "user": userController.userserializer(user)
    }

    return message

def logout():
    return []

def changePassword():
    return []