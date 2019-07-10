# test_manager


## Create Virtual Environment

Follow the instruction in der [Docs](https://docs.python.org/3/tutorial/venv.html) and [Blog](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7):

    $ python3 -m venv venv
    $ echo 'venv' > .gitignore

    $ source venv/bin/activate

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

Edit in NoSQLBooster for MongoDB.

##  Run

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Test with ```curl -v http://127.0.0.1:5000```.

##  Docker 

    $ docker-compose build
    $ docker-compose up manager
    $ docker-compose exec manager /bin/bash