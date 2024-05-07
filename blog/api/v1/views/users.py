from flask import jsonify, request, abort
from sqlalchemy_serializer import SerializerMixin
from blog.api.v1.views import views_bp
from blog import db, app
from blog.models.models import User


"""
CheckList Done:
    GET (Retrieve all users)
    GET (Retrieve a specific user)
    POST (Create a new user)
    DELETE (Delete a user)
    PUT/PATCH (Update a user)
"""

# GET ALL USERS
# http://127.0.0.1:5000/blog/api/v1/users/
@views_bp.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieve all users"""
    with app.app_context():
        users = db.session.query(User).all()
        data = [user.to_dict() for user in users]
        return jsonify(data), 200


# GET A SPECIFIC USER BY user_id
# http://127.0.0.1:5000/blog/api/v1/users/<user_id>
@views_bp.route('/users/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a specific user with id"""
    with app.app_context():
        user = db.get_or_404(User, user_id)
        return jsonify(user.to_dict()), 200


# CREATE A USER
# http://127.0.0.1:5000/blog/api/v1/users
@views_bp.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a user"""
    with app.app_context():
        if request.is_json:
            data = request.get_json()
            if 'username' not in data:
                abort(400, 'username is missing')
            if 'email' not in data:
                abort(400, 'email is missing')
            if 'password' not in data:
                abort(400, 'password is missing')
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User added successfully"}), 200
        else:
            abort(400, 'Not a JSON')


# UPDATE A USER
# http://127.0.0.1:5000/blog/api/v1/users/<user_id>
@views_bp.route('/users/<int:user_id>', methods=['PUT'], strict_slashes=False)
def edit_user(user_id):
    """Update a user with id"""
    with app.app_context():
        user = db.get_or_404(User, user_id)
        if request.is_json:
            data = request.get_json()
            for k, v in data.items():
                if k == 'id' or k == 'created_at' or k == 'updated_at':
                    continue
                setattr(user, k, v)
            db.session.commit()
            return jsonify({"message": "User updated successfully"}), 200
        else:
            abort(400, "Not a JSON")


# DELETE A USER
# http://127.0.0.1:5000/blog/api/v1/users/<user_id>
@views_bp.route('/users/<int:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user with id"""
    with app.app_context():
        user = db.get_or_404(User, user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
