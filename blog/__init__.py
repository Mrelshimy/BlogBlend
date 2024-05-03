from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users_bp.login'
# login_manager.login_message_category = 'info'

from blog.main.main_routes import main_bp
from blog.errors.errors_handlers import errors_bp
from blog.users.users_routes import users_bp
from blog.posts.posts_routes import posts_bp

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)




# from BlogBlend import routes
