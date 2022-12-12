from api import create_app
import os
from werkzeug.utils import secure_filename


app = create_app()

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def uploadImage(file):

    if not os.path.isdir(app.config['UPLOADED_PHOTOS_DEST']):
        os.mkdir(app.config['UPLOADED_PHOTOS_DEST'])


    if file.filename == '':
        raise Exception('No file selected for uploading')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        return filename

    else:
        raise Exception('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        
