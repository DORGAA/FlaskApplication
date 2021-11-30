from flask import Flask
from config import appConfig


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(appConfig[config_name])
    app.config.from_pyfile('config.py')

    from app.login import login as login_blueprint
    app.register_blueprint(login_blueprint)

    return app



