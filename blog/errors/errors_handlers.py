from flask import render_template, Blueprint

errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(404)
def error_404(error):
    # return "404 Error", 404
    return render_template('404.html'), 404


@errors_bp.app_errorhandler(403)
def error_403(error):
    return render_template('400.html'), 403


@errors_bp.app_errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500
