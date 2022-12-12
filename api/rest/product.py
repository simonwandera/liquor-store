from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash, json
from flask import Blueprint, jsonify, request, send_file
from werkzeug.utils import secure_filename

from .. import db
import jwt

from api import create_app


product = Blueprint('product', __name__, url_prefix='/product')

from api.model.models import Product
from api.controllers import productsController, utilController
app = create_app()

@product.route('/', methods=["POST"])
@product.route('', methods=["POST"] )
def addProduct():

    if 'file' not in request.files:
        return{
            "success": False,
            "msg":"No file part in the request"   
        }

    category_id = request.form.get('category_id', None)
    name = request.form.get('name', None)
    text_description=request.form.get('text_description', None)
    html_description=request.form.get('html_description', None)
    buy_price=request.form.get('buy_price', None)
    quantity_in_stock=request.form.get('quantity_in_stock', None)
    image = request.files['file']

    product_x = Product(category_id=category_id, name=name, text_description=text_description, html_description=html_description, buy_price=buy_price, quantity_in_stock=quantity_in_stock, image=image.filename)

    try:
        utilController.uploadImage(image)
        productsController.insert(product_x)
        return {
            "success": True,
            "msg": "product added successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

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

