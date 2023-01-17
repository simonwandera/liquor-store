from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


from .. import db
import jwt

from api.controllers import authController
from api.model.models import User


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/logout', methods=["GET"])
@jwt_required()
def logout():
    # logout_user()
    response = jsonify({'msg': "Logged out successfully"})
    unset_jwt_cookies(response)
    return response

@auth.route('/login', methods=["POST"])
def login():
    if (request.json is None or len(request.json) == 0):
        return {
            "success": False,
            "msg": "Please enter username and password to login"
        }, 400

    username=request.json.get('username', None)
    password=request.json.get('password', None)

    try:
        return authController.login(username, password)
       
    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@auth.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    return jsonify({'msg': "This is a protected route"})
   