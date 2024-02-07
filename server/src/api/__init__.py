from flask import Flask
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("server/src/key.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123321123'

    from api.userAPI import userAPI

    app.register_blueprint(userAPI, url_prefix='/user')

    return app
