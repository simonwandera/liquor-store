
from datetime import timedelta
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_cors import CORS
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()

def create_app(environment="dev"):

    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOADED_PHOTOS_DEST'] = './uploads'
    app.config['JWT_SECRET_KEY'] = 'Please remember to change me'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, supports_credentials=True)

    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)


    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    
    @app.route('/api/uploads', methods=['GET', 'POST'])
    def upload_file():
        print(request.files)
        # for i in request.files:
        #     print(i)
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            print(filename)
            
            
            # rec = Photo(filename=filename, user=g.user.id)
            # rec.store()
            return redirect(url_for('uploaded_file', filename=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=photo>
        <input type=submit value=Upload>
        </form>
        '''

    @app.route('/api/uploads/<filename>')
    def uploaded_file(filename):
        download_image = send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],
                               filename)

        print(app.config['UPLOADED_PHOTOS_DEST'])
        return download_image
    

    from .rest.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .rest.product import product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .rest.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .rest.productType import productType as product_type_blueprint
    app.register_blueprint(product_type_blueprint)


    return app