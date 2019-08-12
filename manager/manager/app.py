import json

from flask import Flask, Blueprint, jsonify, request
from flask_pymongo import PyMongo, pymongo, ObjectId
from flask_cors import CORS

from manager.hello_world import hello_world

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'test'

# username = "app"
# password = "password
# host = "localhost"
# port = "27017"

# mongo_client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))

app.config['MONGO_URI'] = 'mongodb://app:password@mongodb:27017/test'

mongo = PyMongo(app)

app.register_blueprint(hello_world)

@app.route('/dialog', methods=['GET'])
def get_all_dialogs():
    dialog = mongo.db.dialog

    dialogs = []

    for d in dialog.find():
        dialogs.append({'name' : d['name'], 'description' : d['description'], 'turns' : d['turns']}) #, '_id' : str(d['_id']) , 'turns' : d['turns']

    return jsonify(dialogs)


@app.route('/dialog/<name>', methods=['GET'])
def get_last_dialog(name):
    dialog = mongo.db.dialog
    
    d = dialog.find({'name' : name}).sort( '_id' , pymongo.DESCENDING)[0]
    # d = dialog.find_one({'name' : name})

    if d:
        output = {'name' : d['name'], 'description' : d['description'], 'turns': d['turns']}
    else:
        output = 'No results found'

    return output

@app.route('/dialog', methods=['POST'])
def add_dialog():
    dialog = mongo.db.dialog 

    name = request.json['name']
    description = request.json['description']

    turns = request.json['turns']

    dialog_id = dialog.insert({'name' : name, 'description':description, 'turns' : turns})

    new_dialog = dialog.find_one({'_id' : dialog_id})
    
    output = {'name' : new_dialog['name'], 'description' : new_dialog['description'], '_id': str(dialog_id)}

    return output

# @app.route('/test', methods=['GET'])
# def get_all_tests():
#     test = mongo.db.test

#     tests = []

#     for t in test.find():
#         tests.append({'name' : t['name'], '_id': str(t['_id'])}) 

#     return jsonify(tests)

# @app.route('/test/<id>', methods=['GET'])
# def get_last_test(id):
#     test = mongo.db.test
    
#     # t = test.find({'_id' : id}).sort( '_id' , pymongo.DESCENDING)[0]
#     t = test.find_one({'_id' : ObjectId(id)})

#     if t:
#         output = {'_id' : str(t['_id']), 'name' : t['name'], 'description' : t['description'], 'datetime': t['datetime'], 'turns': t['turns']}
#     else:
#         output = 'No results found'

#     return output

# @app.route('/test', methods=['POST'])
# def add_test():
#     test = mongo.db.test 

#     name = request.json['name']
#     datetime = request.json['datetime']
#     testturns = request.json['testturn']

#     test_id = test.insert({'name' : name, 'datetime': datetime, 'testturns' : testturns})
#     new_test = test.find_one({'_id' : test_id})
    
#     output = {'_id': str(test_id),
#               'name' : new_test['name'],
#               'datetime' : new_test['datetime'],
#               'testturn': new_test['testturns']}
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

# @app.route('/testturn', methods=['POST'])
# def add_testturn():
#     testturn = mongo.db.testturn 

#     testturn_id = testturn.insert(request.json)
    
#     output = {'_id': str(testturn_id)}
#     return output

if __name__ == '__main__' :
    app.run(host="0.0.0.0",debug=True)