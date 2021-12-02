from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '1234' #environ.get('SECRET_KEY')
db = SQLAlchemy(app)

Bootstrap(app)
db.init_app(app)
db.create_all()
hash = Bcrypt(app)


# every time we request a route based on a specific ip address,
# flask limiter catch that ip address  from get_remote_address
# and compare (key_func return String) it to the list of ip address in the memory
limiter = Limiter(app, key_func=get_remote_address)
endpoint_limit = limiter.shared_limit("3/day", scope='limiter')


# Combination of app and flask_login
logManager = LoginManager(app)
logManager.init_app(app)
logManager.login_view = 'login_out'


from .login_out import login as login_blueprint
app.register_blueprint(login_blueprint)

from .singup import register as register_blueprint
app.register_blueprint(register_blueprint)

from .dashboard import dash as dash_blueprint
app.register_blueprint(dash_blueprint)

from .login_out import logout as logout_blueprint
app.register_blueprint(logout_blueprint)

from .limiter import testlimiter as testlimiter_blueprint
app.register_blueprint(testlimiter_blueprint)



from app.models import User
