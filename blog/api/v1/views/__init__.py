#!/usr/bin/python3
from flask import Blueprint

views_bp = Blueprint('views', __name__, url_prefix='/blog/api/v1')


from blog.api.v1.views.users import *
from blog.api.v1.views.posts import *
from blog.api.v1.views.tags import *


"""
Ra'fat APIS:
    Random 10 posts from db from different tags
    post data by id
    all articles including data
    User data (name, photo, posts) by id
    
CheckList Done:
    >>>> User
    -----------------
    # GET ALL USERS
    # http://127.0.0.1:5000/blog/api/v1/users/
    
    # GET A SPECIFIC USER BY user_id
    # http://127.0.0.1:5000/blog/api/v1/users/<user_id>
    
    # CREATE A USER
    # http://127.0.0.1:5000/blog/api/v1/users
    
    # UPDATE A USER
    # http://127.0.0.1:5000/blog/api/v1/users/<user_id>
    
    # DELETE A USER
    # http://127.0.0.1:5000/blog/api/v1/users/<user_id>
    
    
    >>>> Post
    -----------------
    # GET POSTS
    # http://127.0.0.1:5000/blog/api/v1/posts/
    
    # GET POST BY post_id
    # http://127.0.0.1:5000/blog/api/v1/posts/<post_id>
    
    # GET POSTS BY user_id
    # http://127.0.0.1:5000/blog/api/v1/users/<user_id>/posts

    # POST a POST BY user_id
    # http://127.0.0.1:5000/blog/api/v1/users/<user_id>/posts

    # PUT a POST BY post_id
    # http://127.0.0.1:5000/blog/api/v1/posts/<post_id>

    # DELETE a POST BY post_id
    # http://127.0.0.1:5000/blog/api/v1/posts/<post_id>
  
  
    >>>> Tags
    -----------------
    # GET TAGS of specific post
    # http://127.0.0.1:5000/blog/api/v1/posts/<int:post_id>/<str:tag_name>
    
    # GET POSTS of specific tag
    # http://127.0.0.1:5000/blog/api/v1/tags/<string:tag_name>/posts
"""
