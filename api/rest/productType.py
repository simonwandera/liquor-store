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


@productType.route('/', methods=["POST"])
@productType.route('')
def upload():
    return 0

def upload_file(request):

    if not os.path.isdir(app.config['UPLOADED_PHOTOS_DEST']):
        os.mkdir(app.config['UPLOADED_PHOTOS_DEST'])

    if 'file' not in request.files:
        
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    return 0

@productType.route('/uploads/<filename>', methods=["GET"])
def uploaded(filename):
    file = secure_filename(filename)

    return send_file(app.config['UPLOADED_PHOTOS_DEST'] +"/"+ filename)
