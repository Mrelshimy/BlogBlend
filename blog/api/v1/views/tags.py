# from flask import jsonify, request, abort
# from sqlalchemy_serializer import SerializerMixin
# from blog.api.v1.views import views_bp
# from blog import db, app
# from blog.models.models import Post, Tag


# """
# Need:
#     GET tags of specific post
#     GET posts under specific tag
# """


# # GET TAGS of specific post
# # http://127.0.0.1:5000/blog/api/v1/posts/<int:post_id>/<str:tag_name>
# @views_bp.route('/posts/<int:post_id>/tags', methods=['GET'], strict_slashes=False)
# def get_tags_of_post(post_id):
#     """Retrieve tags of specific post"""
#     with app.app_context():
#         post = db.get_or_404(Post, post_id)
#         if post is None:
#             abort(404, description=f'Post {post_id} not found')
#         tags = [p.to_dict() for p in post.tags]
#         return jsonify(tags), 200


# # GET POSTS of specific tag
# # http://127.0.0.1:5000/blog/api/v1/tags/<string:tag_name>/posts
# @views_bp.route('/tags/<string:tag_name>/posts', methods=['GET'], strict_slashes=False)
# def get_posts_of_tag(tag_name):
#     """Retrieve posts of specific tag"""
#     with app.app_context():
#         tag = Tag.query.filter_by(name=tag_name).first()
#         if tag is None:
#             abort(404, description=f'{tag_name} not found')
#         posts = [p.to_dict() for p in tag.posts]
#         return jsonify(posts), 200

