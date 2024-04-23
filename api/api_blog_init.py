from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from urllib.parse import quote_plus
user_pass = quote_plus('01061995@DateofBirth')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{user_pass}@localhost/blog'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

