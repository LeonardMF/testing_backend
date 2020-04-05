import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId
from flask_cors import CORS

from manager.extensions import mongo
from manager.hello_world import hello_world
from manager.testcase_endpoint import testcase_endpoint
from manager.testresult_endpoint import testresult_endpoint

app = Flask(__name__)
CORS(app)

# app.config['MONGO_HOST'] = 'mongodb'
# app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'test'
# app.config['MONGO_USERNAME'] = 'app'
# app.config['MONGO_PASSWORD'] = 'password'
# app.config['MONGO_AUTH_SOURCE'] = 'admin'

app.config['MONGO_URI'] = 'mongodb://app:password@mongodb:27017/test'

mongo.init_app(app)

app.register_blueprint(hello_world)
app.register_blueprint(testcase_endpoint)
app.register_blueprint(testresult_endpoint)

if __name__ == '__main__' :
    app.run(host="0.0.0.0",debug=True)