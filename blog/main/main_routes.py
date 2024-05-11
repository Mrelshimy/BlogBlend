from flask import Blueprint, render_template, request
from blog.models.models import Post

# Creaing a Blueprint for the main routes
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    """
    Renders the home page with a paginated list of posts.

    Returns:
        The rendered home.html template with the posts.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc())\
                .paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
