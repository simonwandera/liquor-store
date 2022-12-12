from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename

from .. import db
import jwt

from api import create_app

app = create_app()


product = Blueprint('product', __name__, url_prefix='/product')

from api.model.models import Product
from api.controllers import productsController

@product.route('/')
@product.route('')
def displayProducts():
    return jsonify([*map(productsController.productSerializer, productsController.getAllProducts())])


@product.route('/<id>')
@product.route('<id>')
def getProductType(id):
    try:
        product = productsController.read(id)
        return productsController.productSerializer(product)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
    

@product.route('/uploads/<filename>', methods=["GET"])
def uploaded(filename):
    file = secure_filename(filename)

    return send_file(app.config['UPLOADED_PHOTOS_DEST'] + filename)

