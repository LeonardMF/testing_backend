import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId

from manager.extensions import mongo

testcase_endpoint = Blueprint('testcase_endpoint', __name__)


@testcase_endpoint.route('/testcase', methods=['GET'])
def get_all_testcases():
    dialog = mongo.db.dialog

    dialogs = []

    for d in dialog.find():
        dialogs.append({'name' : d['name'], 'description' : d['description'], 'turns' : d['turns']}) #, '_id' : str(d['_id']) , 'turns' : d['turns']

    return jsonify(dialogs)


@testcase_endpoint.route('/testcase/<name>', methods=['GET'])
def get_last_testcase(name):
    dialog = mongo.db.dialog
    
    d = dialog.find({'name' : name}).sort( '_id' , pymongo.DESCENDING)[0]
    # d = dialog.find_one({'name' : name})

    if d:
        output = {'name' : d['name'], 'description' : d['description'], 'turns': d['turns']}
    else:
        output = 'No results found'

    return output

@testcase_endpoint.route('/testcase', methods=['POST'])
def add_testcase():
    dialog = mongo.db.dialog 

    name = request.json['name']
    description = request.json['description']

    turns = request.json['turns']

    dialog_id = dialog.insert({'name' : name, 'description':description, 'turns' : turns})

    new_dialog = dialog.find_one({'_id' : dialog_id})
    
    output = {'name' : new_dialog['name'], 'description' : new_dialog['description'], '_id': str(dialog_id)}

    return output