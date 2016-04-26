from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    from app.blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    return app


