
from datetime import timedelta
from flask import Flask, request, redirect, url_for, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()

def create_app(environment="dev"):

    app = Flask(__name__, static_folder='static')
    CORS(app, supports_credentials=True)

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, "uploads/")
    app.config['JWT_SECRET_KEY'] = 'Please remember to change me'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)

    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, supports_credentials=True)

    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)


    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    
  

    @app.route('/upload/<filename>', methods=["GET"])
    def uploaded(filename):
        file = secure_filename(filename)

        print("SOmething here")
        print(file)

        download_image = send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],file)
        print("\n\nWe are reporting from here \n")
        return download_image


    @app.route('/api/uploads/<filename>')
    def uploaded_file(filename):
        print("Something here")
       
        # download_image = send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)

        return send_file(app.config['UPLOADED_PHOTOS_DEST'] + filename)
    

    from .rest.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .rest.product import product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .rest.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .rest.productType import productType as product_type_blueprint
    app.register_blueprint(product_type_blueprint)


    return app