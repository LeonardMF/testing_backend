import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId
from flask_cors import CORS

from manager.extensions import mongo
from manager.hello_world import hello_world
from manager.dialog_endpoint import dialog_endpoint

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'test'

# username = "app"
# password = "password
# host = "localhost"
# port = "27017"

# mongo_client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))

app.config['MONGO_URI'] = 'mongodb://app:password@mongodb:27017/test'

mongo.init_app(app)

app.register_blueprint(hello_world)
app.register_blueprint(dialog_endpoint)

if __name__ == '__main__' :
    app.run(host="0.0.0.0",debug=True)