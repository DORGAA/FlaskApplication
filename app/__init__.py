from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
db = SQLAlchemy(app)

Bootstrap(app)
db.init_app(app)
db.create_all()
hash = Bcrypt(app)


from .login import login as login_blueprint
app.register_blueprint(login_blueprint)

from .singup import register as register_blueprint
app.register_blueprint(register_blueprint)



from app.models import User
