from flask import Blueprint, jsonify, request, send_file
from .. import db
import jwt, os
from werkzeug.utils import secure_filename
from api import create_app


productType = Blueprint('productType', __name__, url_prefix='/product_type')

from api.model.models import Product_type
from api.controllers import productTypeController, utilController
app = create_app()

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@productType.route('/', methods=["POST"])
@productType.route('', methods=["POST"] )
def addProductType():
    # if (request.json is None or len(request.json) == 0):
    #     return {
    #         "success": False,
    #         "msg": "No data was sent"
    #     }, 400

    if 'file' not in request.files:
        return{
            "success": False,
            "msg":"No file part in the request"   
        }

    category_name = request.form.get('category_name', None)
    text_description=request.form.get('text_description', None)
    image = request.files['file']

    product_type = Product_type(category_name=category_name, text_description=text_description, image=image.filename)

    try:
        utilController.uploadImage(image)
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
        return productTypeController.productTypeSerializer(productType)

    except Exception as e:
        return{
            "success": False,
            "msg": str(e)
        },400



@productType.route('/uploads/<filename>', methods=["GET"])
def uploaded(filename):
    file = secure_filename(filename)

    return send_file(app.config['UPLOADED_PHOTOS_DEST'] + filename)
