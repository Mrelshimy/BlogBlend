from flask import render_template, redirect, url_for, request, abort, Blueprint
from blog.posts.forms import CreateAndUpdatePostForm
from blog.models.models import Post
from blog import app, db
from flask_login import current_user, login_required
import os
import secrets
from PIL import Image

# Creating a Blueprint for the posts routes
posts_bp = Blueprint('posts_bp', __name__, url_prefix='/posts')


def save_picture(form_picture, w, h):
    """
    Saves a picture to the static/images directory.

    Args:
        form_picture: The picture to save.
        w: The width of the picture.
        h: The height of the picture.

    Returns:
        The name of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    output_size = (w, h)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


# def create_tags_post(post, tags_in_post):
#     for tag in str(tags_in_post).split():
#         if not Tag.query.filter_by(name=tag).first():
#             t = Tag(name=tag)
#             db.session.add(t)
#         else:
#             t = Tag.query.filter_by(name=tag).first()
#         post.tags.append(t)
#     db.session.commit()


# Posts routes
@posts_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    """
    Creates a new post.
    """
    form = CreateAndUpdatePostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            cover = save_picture(form.post_image.data, 800, 600)
        else:
            cover = 'default_cover.png'
        p = Post(title=form.title.data, content=form.content.data,
                 cover=cover, user_id=current_user.id)
        db.session.add(p)
        # if form.tags.data:
        #     create_tags_post(p, form.tags.data)
        db.session.commit()
        return redirect(url_for('main_bp.home'))
    return render_template('new_post.html', title='New post', form=form)


@posts_bp.route('/<int:post_id>')
def post(post_id):
    """
    Displays a post."""
    post = Post.query.get_or_404(post_id)
    # tags = post.tags
    return render_template('post.html', title='post', post=post)


@posts_bp.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    Updates a post."""
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.user_id:
        abort(403)
    form = CreateAndUpdatePostForm()
    if form.validate_on_submit():
        if form.post_image.data:
            cover_path = app.root_path +\
                '/static/images/' + post.cover
            if os.path.exists(cover_path)\
               and post.cover != 'default_cover.png':
                os.remove(cover_path)
            cover = save_picture(form.post_image.data, 800, 600)
            post.cover = cover
        post.title = form.title.data
        post.content = form.content.data
        # for t in post.tags:
        # db.session.query(post_tag).filter(post_tag.c.tag_id == t.id).delete()
        # if form.tags.data:
        #     create_tags_post(post, form.tags.data)
        db.session.commit()
        return redirect(url_for('main_bp.home'))
    form.content.data = post.content
    form.title.data = post.title
    # form.tags.data = ' '.join([tag.name for tag in post.tags])
    # tags = post.tags
    return render_template('new_post.html', title='Update post', form=form)


@posts_bp.route('/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    """
    Deletes a post."""
    post = Post.query.get_or_404(post_id)
    if current_user.id != post.user_id:
        abort(403)
    if post.cover != 'default_cover.png':
        cover_path = app.root_path+'/static/images/'+post.cover
        if os.path.exists(cover_path):
            os.remove(cover_path)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main_bp.home'))
