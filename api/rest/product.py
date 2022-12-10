from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json

from .. import db
import jwt
from api.controllers import productsController


product = Blueprint('product', __name__, url_prefix='/product')

