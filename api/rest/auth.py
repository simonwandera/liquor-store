from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


from .. import db
import jwt

from api.controllers import authController
from api.model.models import User



auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/logout', methods=["POST"])

def logout():
    # logout_user()
    response = jsonify({'message': "Logged out successfully"})
    unset_jwt_cookies(response)
    return response

@auth.route('/login', methods=["POST"])
def login():
    if (request.json is None or len(request.json) == 0):
        return {
            "success": False,
            "message": "Please enter username and password to login"
        }, 400

    username=request.json.get('username', None)
    password=request.json.get('password', None)

    try:
        user = authController.login(username, password)
        return user
        
    except Exception as e:
        return{
            "success": False,
            "message": str(e)
        },400
