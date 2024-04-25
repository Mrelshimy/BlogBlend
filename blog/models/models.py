from datetime import datetime
from blog import db, app, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))

class User(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    bio = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255), nullable=False, default='https://via.placeholder.com/150')
    posts = db.relationship('Post', back_populates='user', lazy=True, cascade='all, delete, delete-orphan')
    # comments = db.relationship('Comment', back_populates='user', lazy=True, cascade='all, delete, delete-orphan')
    # likes = db.relationship('Like', back_populates='user', lazy=True, cascade='all, delete, delete-orphan')

    serialize_rules = ('-posts', '-comments', '-likes', '-password')

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, passwd):
        return bcrypt.check_password_hash(self.password, passwd)

    def __repr__(self):
        return f'<User {self.username}>'


post_tag = db.Table('post_tag',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class Post(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String(255), nullable=False, default='https://via.placeholder.com/800x400')
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='posts', lazy=True)
    tags = db.relationship('Tag', secondary=post_tag, back_populates='posts', lazy=True)
    # comments = db.relationship('Comment', back_populates='post', lazy=True, cascade='all, delete')
    # likes = db.relationship('Like', back_populates='post', lazy=True, cascade='all, delete')
    
    serialize_rules = ('-user', '-tags' ,'-comments', '-likes')

    def __repr__(self):
        return f'<Post {self.title}>'


class Tag(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', secondary=post_tag, back_populates='tags', lazy=True)

    serialize_rules = ('-posts',)

    def __repr__(self):
        return f'<Tag {self.name}>'


class Comment(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='comments', lazy=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    post = db.relationship('Post', back_populates='comments', lazy=True)

    def __repr__(self):
        return f'<Comment {self.id}>'


class Like(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='likes', lazy=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    post = db.relationship('Post', back_populates='likes', lazy=True)

    def __repr__(self):
        return f'<Like {self.id}>'


# with app.app_context():
#     db.drop_all()
#     db.create_all()
    
#     user1 = User(id=1, username='user1', email='user1@one.com', password='pass1')
#     db.session.add(user1)
#     post1 = Post(id=1, title='title1', content='content1', user_id=user1.id)
#     db.session.add(post1)
#     post2 = Post(id=2, title='title2', content='content2', user_id=user1.id)
#     db.session.add(post2)
    
#     user2 = User(id=2, username='user2', email='user2@two.com', password='pass2')
#     db.session.add(user2)
#     post3 = Post(id=3, title='title3', content='content3', user_id=user2.id)
#     db.session.add(post3)
#     post4 = Post(id=4, title='title4', content='content4', user_id=user2.id)
#     db.session.add(post4)
    
#     tag1 = Tag(id=1, name='tag1')
#     db.session.add(tag1)
#     tag2 = Tag(id=2, name='tag2')
#     db.session.add(tag2)
#     tag3 = Tag(id=3, name='tag3')
#     db.session.add(tag3)
#     tag4 = Tag(id=4, name='tag4')
#     db.session.add(tag4)

#     post1.tags.append(tag1)
#     post1.tags.append(tag2)
#     post2.tags.append(tag2)
#     post2.tags.append(tag3)
#     post3.tags.append(tag3)
#     post3.tags.append(tag4)
#     post4.tags.append(tag4)
#     post4.tags.append(tag1)


#     db.session.commit()

#     # print(post1.tags)
#     # print(post2.tags)
#     # print(tag1.posts)
#     # print(tag2.posts)
#     # print(tag3.posts)
#     # print(tag4.posts)

    # c = Comment(id=1, content='content', user_id=u.id, post_id=p1.id)
    # db.session.add(c)
    # l = Like(id=1, user_id=u.id, post_id=p1.id)
    # db.session.add(l)
    # db.session.delete(p1)
    # db.session.commit()
    # x = db.session.get(User, 4)
    # x.username = 'sameh123'
    # print(x)
