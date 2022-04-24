from flask import Flask
from .templates.password import pw, db

from .main.routes import main
from .extention import mongo 

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://nnlbmt123:{}@cluster0.c2sp4.mongodb.net/{}?retryWrites=true&w=majority'.format(pw, db)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
print('mongodb+srv://nnlbmt123:{}@cluster0.c2sp4.mongodb.net/{}?retryWrites=true&w=majority'.format(pw, db))