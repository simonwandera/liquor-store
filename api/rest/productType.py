from flask import Blueprint, jsonify, request, send_file
from .. import db
import jwt, os
from werkzeug.utils import secure_filename
from api import create_app


productType = Blueprint('productType', __name__, url_prefix='/product_type')

from api.model.models import Product_type
from api.controllers import productTypeController, utilController
app = create_app()


@productType.route('/', methods=["POST"])
@productType.route('', methods=["POST"] )
def addProductType():

    category_name = request.json.get('category_name', None)
    text_description=request.json.get('text_description', None)
    imageURL = request.json.get('imageURL', None)

    product_type = Product_type(category_name=category_name, text_description=text_description, image=imageURL)

    try:
        productTypeController.insert(product_type)
        return {
            "success": True,
            "msg": "product type added successfully"
        }

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400

@productType.route('/')
@productType.route('')
def displayProductsTypes():
    return jsonify([*map(productTypeController.productTypeSerializer, productTypeController.getAllProductsTypes())])

@productType.route('/<id>')
@productType.route('<id>')
def getProductType(id):
    try:
        product_type = productTypeController.read(id)
        print(product_type)
        return productTypeController.productTypeSerializer(product_type)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400
