from flask import Blueprint, jsonify, request, send_file
from .. import db
import jwt, os
from api.controllers import productTypeController
from werkzeug.utils import secure_filename

from api import create_app


productType = Blueprint('productType', __name__, url_prefix='/product_type')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = create_app()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@productType.route('/upload', methods=["POST"])
def upload():

    if not os.path.isdir(app.config['UPLOADED_PHOTOS_DEST']):
        os.mkdir(app.config['UPLOADED_PHOTOS_DEST'])

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
        print(filename)
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 200
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
    return resp

@productType.route('/upload/<filename>', methods=["GET"])
def uploaded(filename):
    file = secure_filename(filename)

    return send_file(app.config['UPLOADED_PHOTOS_DEST'] +"/"+ filename)
