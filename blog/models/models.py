from datetime import datetime
from blog import db, app, bcrypt, login_manager, app, secret_key
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
import jwt


# login manager
@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user by its id.

    Returns:
        The user with the given id.
    """
    return db.session.query(User).get(int(user_id))


class User(db.Model, UserMixin, SerializerMixin):
    """
    User model for the database.

    Attributes:
        id: An integer representing the user's id.
        username: A string representing the user's username.
        email: A string representing the user's email.
        password: A string representing the user's password.
        created_at: A datetime object representing the user's creation date.
        updated_at: A datetime object representing the user's last update date.
        bio: A string representing the user's bio.
        avatar: A string representing the user's avatar.
        posts: A relationship to the Post model.
        comments: A relationship to the Comment model.
        likes: A relationship to the Like model.

    Relationships:
        posts: A one-to-many relationship to the Post model.
        comments: A one-to-many relationship to the Comment model.
        likes: A one-to-many relationship to the Like model.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
                           onupdate=datetime.now)
    bio = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255), nullable=False,
                       default='defaulte_profile.png')
    posts = db.relationship('Post', back_populates='user',
                            lazy=True, cascade='all, delete, delete-orphan')

    def get_token(self):
        """
        Generates a token for the user.

        Returns:
            A token for the user.
        """
        encoded_user_id = jwt.encode({'user_id': self.id},
                                     secret_key, algorithm='HS256')
        return encoded_user_id

    # comments = db.relationship('Comment', back_populates='user',
    # lazy=True, cascade='all, delete, delete-orphan')
    # likes = db.relationship('Like', back_populates='user',
    # lazy=True, cascade='all, delete, delete-orphan')

    serialize_rules = ('-posts', '-comments', '-likes', '-password')

    def set_password(self, password):
        """
        Sets the user's password.

        Returns:
            The user's password hashed inside database.
        """
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, passwd):
        """
        Checks the user's password.
        """
        return bcrypt.check_password_hash(self.password, passwd)

    def __repr__(self):
        """
        Returns:
            A string representation of the user."""
        return f'<User {self.username}>'


# post_tag = db.Table('post_tag',
#     db.Column('post_id', db.Integer,
#     db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True),
#     db.Column('tag_id', db.Integer,db.ForeignKey('tag.id'), primary_key=True)
# )


class Post(db.Model, UserMixin, SerializerMixin):
    """
    Post model for the database.

    Attributes:
        id: An integer representing the post's id.
        cover: A string representing the post's cover image.
        title: A string representing the post's title.
        content: A string representing the post's content.
        created_at: A datetime object representing the post's creation date.
        updated_at: A datetime object representing the post's last update date.
        user_id: An integer representing the user's id.
        user: A relationship to the User model.
        tags: A relationship to the Tag model.
        comments: A relationship to the Comment model.
        likes: A relationship to the Like model.

    Relationships:
        user: A many-to-one relationship to the User model.
        tags: A many-to-many relationship to the Tag model.
        comments: A one-to-many relationship to the Comment model.
        likes: A one-to-many relationship to the Like model.
    """
    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String(255), nullable=False,
                      default='defaulte_cover.png')
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now,
                           onupdate=datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id',
                                      ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='posts',
                           lazy=True)
    # tags = db.relationship('Tag', secondary=post_tag,
    # back_populates='posts', lazy=True)
    # comments = db.relationship('Comment', back_populates='post',
    # lazy=True, cascade='all, delete')
    # likes = db.relationship('Like', back_populates='post',
    # lazy=True, cascade='all, delete')

    serialize_rules = ('-user', '-tags', '-comments', '-likes')

    def __repr__(self):
        return f'<Post {self.title}>'


# class Tag(db.Model, UserMixin, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     posts = db.relationship('Post',
# secondary=post_tag, back_populates='tags', lazy=True)
#
#     serialize_rules = ('-posts',)
#
#     def __repr__(self):
#         return f'<Tag {self.name}>'


# class Comment(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime,
# default=datetime.now)
#     updated_at = db.Column(db.DateTime,
# default=datetime.now, onupdate=datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id',
# ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', back_populates='comments', lazy=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id',
# ondelete='CASCADE'), nullable=False)
#     post = db.relationship('Post', back_populates='comments', lazy=True)
#
#     def __repr__(self):
#         return f'<Comment {self.id}>'
#
#
# class Like(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id',
# ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', back_populates='likes', lazy=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id',
# ondelete='CASCADE'), nullable=False)
#     post = db.relationship('Post', back_populates='likes', lazy=True)
#
#     def __repr__(self):
#         return f'<Like {self.id}>'
