from flask import render_template, Blueprint

# Create a Blueprint for the errors handlers
errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(404)
def error_404(error):
    """
    Error handler for 404 Not Found errors.

    Args:
        error: The error object.

    Returns:
        A rendered template for the 404.html page with a 404 status code.
    """
    return render_template('404.html'), 404


@errors_bp.app_errorhandler(403)
def error_403(error):
    """
    Error handler for 403 Forbidden errors.

    Args:
        error: The error object.

    Returns:
        A rendered template for the 400.html page with a 403 status code.
    """
    return render_template('400.html'), 403


@errors_bp.app_errorhandler(500)
def error_500(error):
    """
    Error handler for 500 Internal Server Error.

    Args:
        error: The error object.

    Returns:
        A rendered template for the 500.html page with a 500 status code.
    """
    return render_template('500.html'), 500
