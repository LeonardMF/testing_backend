import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId

from manager.extensions import mongo

testresult_endpoint = Blueprint('testresult_endpoint', __name__)

@testresult_endpoint.route('/testresult', methods=['POST'])
def add_testresult():
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

@testresult_endpoint.route('/testresult', methods=['GET'])
def get_all_testresults():
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

@testresult_endpoint.route('/testresult/<id>', methods=['GET'])
def get_last_testresult(id):
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

# @result_endpoint.route('/result/<id>', methods=['PATCH'])
# def add_to_result(id):
#     result = mongo.db.result
    
#     // r = result.find_one({'_id' : ObjectId(id)})

# mongo.db.users.update_one( request.json['testturn'], {'$set': data.get('payload', {})})


#     if r:
#         r['testcases'].append{}
#         output = {'_id' : str(r['_id']),
#                   'dialogName' : r['dialogName'],
#                   'dialogDescription' : r['dialogDescription'],
#                   'assistant' : r['assistant'],
#                   'datetime' : r['datetime'],
#                   'testcases': r['testcases']}
#     else:
#         output = 'No results found'

#     return output


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

