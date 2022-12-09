from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


from .. import db
import jwt

from api.controllers import authController, userController


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/logout', methods=["POST"])
# @login_required
def logout():
    # logout_user()
    response = jsonify({'message': "Logged out successfully"})
    unset_jwt_cookies(response)
    return response

@auth.route('/login', methods=["POST"])
def login():
    return 0