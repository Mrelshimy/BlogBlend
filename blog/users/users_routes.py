from flask import render_template, redirect, url_for, request, Blueprint, flash
from blog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, ResetPasswordForm, RequestResetForm
from blog.models.models import User
from blog import app, db, mail, secret_key
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message
from urllib.parse import urlencode, parse_qs
import os
import secrets
from PIL import Image
import jwt

users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, username=form.username.data)
        user.set_password(user.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_bp.home'))
    return render_template('register.html', title='Register', form=form)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main_bp.home'))
    return render_template('login.html', title='Login', form=form)


@users_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.home'))


@users_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@users_bp.route('/articles')
def articles():
    return render_template('articles.html')


def save_picture(form_picture, w, h):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    output_size = (w, h)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@users_bp.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # current_user.email = form.email.data
        current_user.username = form.username.data
        if form.image.data:
            avatar_path = app.root_path + '/static/images/' + current_user.avatar
            if os.path.exists(avatar_path):
                os.remove(avatar_path)
            current_user.avatar = save_picture(form.image.data, 150, 150)
        db.session.commit()
        return redirect(url_for('main_bp.home'))
    elif request.method == 'GET':
        # form.email.data = current_user.email
        form.username.data = current_user.username
    # image_file = url_for('static', filename='images/' + current_user.avatar)
    return render_template('account.html', title='Account', form=form)


def send_reset_email(user):
    token = user.get_token()
    reset_url = url_for('users_bp.reset_request', _external=True)
    reset_url_with_token = reset_url + f"/{token}"
    msg = Message('Password Reset Request', sender='noreply@blogblend.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{reset_url_with_token}

If you didn't make this request, ignore this email.
'''
    mail.send(msg)

@users_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password')
        return redirect(url_for('main_bp.home'))
    return render_template('reset_request.html', form=form)


@users_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    user_id = jwt.decode(token, secret_key, algorithms=['HS256'])['user_id']
    user = User.query.get(user_id)
    if user is None:
        flash('That is an invalid or expired token')
        return redirect(url_for('users_bp.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for('users_bp.login'))
    return render_template('reset_token.html', form=form)
