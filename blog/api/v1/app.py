#!/usr/bin/python3
from flask import Flask, jsonify, make_response
from blog.api.v1.views import views_bp
from flask_cors import CORS

# Create a Flask application
app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(views_bp)

# Set the configuration variables for the Flask application
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Enable CORS
cors = CORS(app, resources={r"/blog/api/*": {"origins": "*"}})


# Create a route for the status
@app.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Return the status of the API
    """
    return jsonify({'status': 'OK'})


@app.errorhandler(404)
def not_found(error):
    """
    Return a 404 error
    """
    return make_response(jsonify({'error': 'NOT FOUND - 404'}), 404)


if __name__ == "__main__":
    """
    Run the application
    """
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
