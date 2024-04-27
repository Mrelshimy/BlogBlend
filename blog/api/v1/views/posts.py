from flask import jsonify, request, abort
from sqlalchemy_serializer import SerializerMixin
from blog.api.v1.views import views_bp
from blog import db, app
from blog.models.models import Post, User, Tag


"""
Need:
    Random 10 posts from db from different tags
CheckList Done:
    GET (Retrieve all posts)
    POST (Create a new post)
    /posts/{id}:
        GET (Retrieve a specific post)
        PUT/PATCH (Update a post)
        DELETE (Delete a post)
    /posts/tag_id
        GET (Retrieve posts under tag)
"""


# GET POSTS
# http://127.0.0.1:5000/blog/api/v1/posts/
@views_bp.route('/posts', methods=['GET'], strict_slashes=False)
def get_posts():
    with app.app_context():
        posts = db.session.query(Post).all()
        data = [post.to_dict() for post in posts]
        return jsonify(data), 200


# GET POST BY post_id
# http://127.0.0.1:5000/blog/api/v1/posts/<post_id>
@views_bp.route('/posts/<int:post_id>', methods=['GET'], strict_slashes=False)
def get_post(post_id):
    """Retrieve a specific post with id"""
    with app.app_context():
        post = db.get_or_404(Post, post_id)
        return jsonify(post.to_dict()), 200


# GET POST IMG by post_id
# http://127.0.0.1:5000/blog/api/v1/posts/<int:post_id>/img
@views_bp.route('/posts/<int:post_id>/img', methods=['GET'], strict_slashes=False)
def get_post_img(post_id):
    with app.app_context():
        pass



# GET POSTS BY user_id
# http://127.0.0.1:5000/blog/api/v1/users/<user_id>/posts
@views_bp.route('/users/<int:user_id>/posts', methods=['GET'], strict_slashes=False)
def get_posts_of_user(user_id):
    """Retrieve posts of specific user"""
    with app.app_context():
        user = db.get_or_404(User, user_id)
        if user is None:
            abort(404, description=f'user id {user_id} not found')
        posts = [p.to_dict() for p in user.posts]
        return jsonify(posts), 200


# POST a POST BY user_id
# http://127.0.0.1:5000/blog/api/v1/users/<user_id>/posts
@views_bp.route('/users/<int:user_id>/posts', methods=['POST'], strict_slashes=False)
def post_a_post(user_id):
    with app.app_context():
        user = db.get_or_404(User, user_id)
        if request.is_json:
            data = request.get_json()
            if 'title' not in data.keys():
                abort(400, "title is missing")
            if 'content' not in data.keys():
                abort(400, "content is missing")
            post = Post(user_id=user_id, title=data.get('title'), content=data.get('content'))
            if data.get('cover'):
                post.cover = data.get('cover')
            for t in data.get('tags').split():
                tag = db.session.query(Tag).filter(Tag.name == t).first()
                if tag is None:
                    tag = Tag(name=t)
                    db.session.add(tag)
                post.tags.append(tag)

            db.session.commit()
            return jsonify({'message': 'Post added successfully'}), 201
        else:
            abort(400, 'Not a JSON')


# PUT a POST BY post_id
# http://127.0.0.1:5000/blog/api/v1/posts/<post_id>
@views_bp.route('/posts/<int:post_id>', methods=['PUT'], strict_slashes=False)
def edit_post(post_id):
    with app.app_context():
        if request.is_json:
            post = db.get_or_404(Post, post_id)
            data = request.get_json()
            for k, v in data.items():
                if v == 'created_at' or v == "updated_at" or v == 'id':
                    continue
                setattr(post, k, v)
                db.session.commit()
            return jsonify({"message": "User updated successfully"}), 200
        else:
            abort(400, "Not a JSON")


# DELETE a POST BY post_id
# http://127.0.0.1:5000/blog/api/v1/posts/<post_id>
@views_bp.route('/posts/<int:post_id>', methods=['DELETE'], strict_slashes=False)
def delete_post(post_id):
    with app.app_context():
        post = db.get_or_404(Post, post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted successfully'}), 200
