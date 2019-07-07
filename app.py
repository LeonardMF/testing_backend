import json
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'

# username = "app"
# password = "password
# host = "localhost"
# port = "27017"

# mongo_client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, host, port))

app.config['MONGO_URI'] = 'mongodb://app:password@localhost:27017/test'

mongo = PyMongo(app)

@app.route("/")
def hello():
    return jsonify({"about":"Hello World!"})

@app.route('/dialog', methods=['GET'])
def get_all_dialogs():
    dialog = mongo.db.dialog

    dialogs = []

    for d in dialog.find():
        dialogs.append(d['name']) #, '_id' : str(d['_id'])

    return jsonify(dialogs)


@app.route('/dialog/<name>', methods=['GET'])
def get_last_dialog(name):
    dialog = mongo.db.dialog
    
    d = dialog.find({'name' : name}).sort( '_id' , pymongo.DESCENDING)[0]
    # d = dialog.find_one({'name' : name})

    if d:
        output = {'name' : d['name'], 'testcases': d['testcases']}
    else:
        output = 'No results found'

    return output

@app.route('/dialog', methods=['POST'])
def add_dialog():
    dialog = mongo.db.dialog 

    name = request.json['name']
    print('add: '+name)
    testcases = request.json['cases']

    dialog_id = dialog.insert({'name' : name, 'testcases' : testcases})
    new_dialog = dialog.find_one({'_id' : dialog_id})
    
    output = {'name' : new_dialog['name'], '_id': str(dialog_id)}

    return output


if __name__ == '__main__' :
    app.run(debug=True)