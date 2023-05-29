from flask import Flask
from flask import jsonify
from api.v1.views import app_views

app = Flask(__name__)


@app.views.route('/status')
def status():
    return jsonify({'status': OK})
