from flask import Flask, render_template

import mongoengine as me
from pymongo import MongoClient
from urllib.parse import quote_plus

name = quote_plus('mainAdmin')
pwd = quote_plus('Julian2014!!!!')
host = '127.0.0.1'
db = quote_plus('workouts')
uri = 'mongodb://%s:%s@%s/%s?authSource=admin' % (name, pwd, host, db)
client = MongoClient(uri)

def page_not_found(error):
    return render_template('404.html')

def create_app(object_name):
    """
    A flask application factor, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories
    Args:
        object_name: the python path of the config object,
                    e.g. project.config.ProdConfig         
    """
    
    app = Flask(__name__)
    app.config.from_object(object_name)
    
    me.connect('workouts',host="mongodb://mainAdmin:Julian2014!!!!@127.0.0.1")
    
    from .auth import create_module as auth_create_module
    from .workout import create_module as workout_create_module
    from .timer import create_module as timer_create_module
    from .main import create_module as main_create_module
    from .api import create_module as api_create_module
    
    auth_create_module(app)
    workout_create_module(app)
    timer_create_module(app)
    main_create_module(app)
    api_create_module(app)
    
    return app