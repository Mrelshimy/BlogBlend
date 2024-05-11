#!/usr/bin/python3
from flask import Blueprint

# Create a Blueprint for the views
views_bp = Blueprint('views', __name__, url_prefix='/blog/api/v1')

# Import the views
from blog.api.v1.views.users import *
from blog.api.v1.views.posts import *
from blog.api.v1.views.tags import *
