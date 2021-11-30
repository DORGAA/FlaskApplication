from flask import Flask
from config import appConfig
from flask_bootstrap import Bootstrap


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(appConfig[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    from app.login import login as login_blueprint
    app.register_blueprint(login_blueprint, title='login')

    return app



