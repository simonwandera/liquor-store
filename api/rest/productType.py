from flask import Blueprint, jsonify, request, json
from .. import db
import jwt, os
from api.controllers import productTypeController
from werkzeug.utils import secure_filename


productType = Blueprint('productType', __name__, url_prefix='/product_type')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@productType.route('/upload', methods=["POST"])
def login():

    # print(request.json)

    # if (request.json is None or len(request.json) == 0):
    #     return {
    #         "success": False,
    #         "message": "No data provided"
    #     }, 400

    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    file = request.files['file']

    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(productType.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
    return resp
