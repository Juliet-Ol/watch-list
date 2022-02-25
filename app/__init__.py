# from flask import Flask #import flask from flask module
from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap # import bootstrap


# from app.config import DevConfig 

from .config import DevConfig # import config

# Initializing application
app = Flask(__name__, instance_relative_config = True) #create app instance and allow connct to instance folder

# Setting up configuration
app.config.from_object(DevConfig)#imports dev config class
app.config.from_pyfile('config.py')

# Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views