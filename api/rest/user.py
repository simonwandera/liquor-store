from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json

from .. import db

user = Blueprint('user', __name__, url_prefix='/user')
import jwt 


from api.controllers import authController, userController
