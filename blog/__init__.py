from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config
from flask_mail import Mail
import os


# Create a Flask application
app = Flask(__name__)

# Load the Config class into the Flask app
app.config.from_object(Config)

# Create a database instance
db = SQLAlchemy(app)

# Create a Bcrypt instance
bcrypt = Bcrypt(app)

# Create a LoginManager instance
login_manager = LoginManager(app)
login_manager.login_view = 'users_bp.login'

# Create a Mail instance
mail = Mail(app)

# Create a secret key
secret_key = app.config.get('SECRET_KEY')
# login_manager.login_message_category = 'info'


# Import the routes from the main, errors, users, and posts packages
from blog.main.main_routes import main_bp
from blog.errors.errors_handlers import errors_bp
from blog.users.users_routes import users_bp
from blog.posts.posts_routes import posts_bp

# Register the blueprints
app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

# from BlogBlend import routes
