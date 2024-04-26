from flask import render_template, redirect, url_for, request, abort
from blog.routes.forms import RegistrationForm, LoginForm, UpdateAccountForm, CreateAndUpdatePostForm
from blog.models.models import User, Post, Tag, post_tag
from blog import app, db
from flask_login import current_user, login_user, logout_user, login_required
import os
import secrets
from PIL import Image


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, username=form.username.data)
        user.set_password(user.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.image.data:
            current_user.avatar = save_picture(form.image.data)
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.username.data = current_user.username
    image_file = url_for('static', filename='images/' + current_user.avatar)
    return render_template('account.html', title='Account', form=form, image_file=image_file)


def create_tags_post(post, tags_in_post):
    for tag in str(tags_in_post).split():
        t = Tag(name=tag)
        db.session.add(t)
        post.tags.append(t)
    db.session.commit()


@app.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreateAndUpdatePostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            cover = save_picture(form.post_image.data)
        else:
            cover = 'https://via.placeholder.com/800x400'
        p = Post(title=form.title.data, content=form.content.data, cover=cover, user_id=current_user.id)
        db.session.add(p)
        if form.tags.data:
            create_tags_post(p, form.tags.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_post.html', title='New post', form=form)


@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    tags = post.tags
    return render_template('post.html', title='post', post=post, tags=tags)


@app.route('/post/<int:post_id>/update')
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    tags = post.tags
    return render_template('post.html', title='post', post=post, tags=tags)


@app.route('/post/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.user_id:
        abort(403)
    if post.cover != 'https://via.placeholder.com/800x400':
        cover_path = app.root_path+'static/images/'+post.cover
        if os.path.exists(cover_path):
            os.remove(cover_path)
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
