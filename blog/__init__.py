from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.environ["DB_USER"]}:{os.environ["DB_PASS"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# from BlogBlend import routes
