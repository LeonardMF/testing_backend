import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId

from manager.extensions import mongo

result_endpoint = Blueprint('result_endpoint', __name__)

@result_endpoint.route('/result', methods=['POST'])
def add_result():
    result = mongo.db.result 

    dialogName = request.json['dialogName']
    dialogDescription = request.json['dialogDescription']
    assistant = request.json['assistant']
    datetime = request.json['datetime']
    testcases = request.json['testcases']

    result_id = result.insert({'dialogName' : dialogName,
                               'dialogDescription' : dialogDescription,
                               'datetime': datetime,
                               'assistant': assistant,
                               'testcases' : testcases})

    new_result = result.find_one({'_id' : result_id})
    
    output = {'_id': str(result_id),
              'dialogName' : new_result['dialogName'],
              'dialogDescription' : new_result['dialogDescription'],
              'assistant' : new_result['assistant'],
              'datetime' : new_result['datetime'],
              'testcases': new_result['testcases']}
    return output

@result_endpoint.route('/result', methods=['GET'])
def get_all_results():
    result = mongo.db.result 

    results = []

    for r in result.find():
        results.append({'_id': str(r['_id']),
                        'dialogName' : r['dialogName'],
                        'dialogDescription' : r['dialogDescription'],
                        'assistant' : r['assistant'],
                        'datetime' : r['datetime'],
                        'testcases': r['testcases']}) 

    return jsonify(results)

@result_endpoint.route('/result/<id>', methods=['GET'])
def get_last_test(id):
    result = mongo.db.result
    
    r = result.find_one({'_id' : ObjectId(id)})

    if r:
        output = {'_id' : str(r['_id']),
                  'dialogName' : r['dialogName'],
                  'dialogDescription' : r['dialogDescription'],
                  'assistant' : r['assistant'],
                  'datetime' : r['datetime'],
                  'testcases': r['testcases']}
    else:
        output = 'No results found'

    return output



# @app.route('/test/<id>', methods=['PATCH'])
# def patch_test(id):
#     test = mongo.db.test
    
#     mongo.db.users.update_one(
#                 request.json['testturn'], {'$set': data.get('payload', {})})

#     if t:
#         output = {'name' : t['name'], 'datetime': t['datetime'], 'testturns': t['testturns']}
#     else:
#         output = 'No results found'

#     return output

