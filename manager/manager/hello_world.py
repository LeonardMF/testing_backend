
from flask import Blueprint, jsonify, request

hello_world = Blueprint('hello_world', __name__)
@hello_world.route('/hello')
def hello():
    return jsonify({"about":"Hello World!"})
