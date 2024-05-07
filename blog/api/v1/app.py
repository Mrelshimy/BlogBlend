#!/usr/bin/python3
from flask import Flask, jsonify, make_response
from blog.api.v1.views import views_bp
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(views_bp)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/blog/api/*": {"origins": "*"}})

@app.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({'status': 'OK'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'NOT FOUND - 404'}), 404)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
