# Backend 


## Create Virtual Environment

Follow the instruction in der [Docs](https://docs.python.org/3/tutorial/venv.html) and [Blog](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7):

    $ python3 -m venv venv
    $ echo 'venv' > .gitignore

    $ source venv/bin/activate
    $ pip install -r manager/manager/requirements.txt

Freeze the requirements:
    $ pip freeze > requirements.txt

## Select Interpreter (VS Code)

To select a specific environment, use the Command Palette (⇧⌘P).
Type in ```Python: Select Interpreter``` and select ```./venv/bin/python```.

[Docs](https://code.visualstudio.com/docs/python/environments)

## Install Flask

Follow the instruction in der [Docs](http://flask.pocoo.org/):

    $ pip install Flask

RESTful: 

    $ pip install Flask-RESTful

[Video](https://www.youtube.com/watch?v=s_ht4AKnWZg)

##  MongoDB
Integrate with [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/).

    $ pip install Flask-PyMongo
    
Start with docker compose.

    $ docker-compose up mongodb

Edit the `db` in NoSQLBooster for MongoDB.

Connection URI: 'mongodb://localhost:27017'
Authentication:
- Mode: Basic
- Auth DB: admin
- User Name: user
- Password: password

Add database `test` and user `app` with `ReadWrite` permissions for `test` database.

##  Run

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Test with ```curl -v http://127.0.0.1:5000```.

##  Docker 

    $ docker-compose build
    $ docker-compose up manager
    $ docker-compose exec manager /bin/bash

## Start with Rasa 

    $  docker-compose -f docker-compose.yaml -f ../testing_bot/docker-compose.yml up

[Docs](https://docs.docker.com/compose/reference/overview/#specifying-multiple-compose-files)