from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = '88dhbai28dnqg27wkww'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/web_blog'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from app import routes
