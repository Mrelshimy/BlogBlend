#!/usr/bin/python3
from datetime import datetime
from blog import db, app, bcrypt


class User(db.Model):
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

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        """Editing the __dict__ representation of the object"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        dic['posts'] = [post.to_dict() for post in self.posts]
        del dic['password']
        if '_sa_instance_state' in dic:
            del dic['_sa_instance_state']
        return dic


# post_tag = db.Table('post_tag',
#     db.Column('post_id', db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
# )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover = db.Column(db.String(255), nullable=False, default='https://via.placeholder.com/800x400')
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='posts', lazy=True)
    # comments = db.relationship('Comment', back_populates='post', lazy=True, cascade='all, delete')
    # likes = db.relationship('Like', back_populates='post', lazy=True, cascade='all, delete')
    # tags = db.relationship('Tag', secondary=post_tag, back_populates='posts', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'

    def to_dict(self):
        """Editing the __dict__ representation of the object"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in dic:
            del dic['_sa_instance_state']
        return dic


# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', back_populates='comments', lazy=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
#     post = db.relationship('Post', back_populates='comments', lazy=True)

#     def __repr__(self):
#         return f'<Comment {self.id}>'


# class Like(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', back_populates='likes', lazy=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
#     post = db.relationship('Post', back_populates='likes', lazy=True)

#     def __repr__(self):
#         return f'<Like {self.id}>'


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     posts = db.relationship('Post', secondary=post_tag, back_populates='tags', lazy=True)

#     def __repr__(self):
#         return f'<Tag {self.name}>'

#     def to_dict(self):
#         """Editing the __dict__ representation of the object"""
#         dictionary = self.__dict__.copy()
#         dictionary["created_at"] = self.created_at.isoformat()
#         dictionary["updated_at"] = self.updated_at.isoformat()
#         dictionary['__class__'] = self.__class__.__name__
#         if '_sa_instance_state' in dictionary:
#             del dictionary['_sa_instance_state']
#         return dictionary


# with app.app_context():
    # db.drop_all()
    # db.create_all()
    # u = User(id=1, username='admin', email='admin@a.c', password='admin')
    # db.session.add(u)
    # uu = User(id=2, username='admin_admin', email='admin_admin@a.c', password='admin_admin')
    # db.session.add(uu)
    # p1 = Post(id=1, title='title', content='content1', user_id=u.id)
    # db.session.add(p1)
    # p2 = Post(id=2, title='title', content='content2', user_id=uu.id)
    # db.session.add(p2)
    # p3 = Post(id=3, title='title', content='content3', user_id=uu.id)
    # db.session.add(p3)
    # p4 = Post(id=4, title='title', content='content4', user_id=u.id)
    # db.session.add(p4)
#     c = Comment(id=1, content='content', user_id=u.id, post_id=p1.id)
#     db.session.add(c)
#     l = Like(id=1, user_id=u.id, post_id=p1.id)
#     db.session.add(l)
#     t = Tag(id=1, name='technology')
#     db.session.add(t)
#     p1.tags.append(t)
#     p2.tags.append(t)
#
    # db.session.commit()
#     db.session.delete(p1)
#     db.session.commit()