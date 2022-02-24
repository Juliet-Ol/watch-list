# from flask import Flask #import flask from flask module
from flask import Flask


# from app.config import DevConfig 

from .config import DevConfig # import config

# Initializing application
app = Flask(__name__, instance_relative_config = True) #create app instance and allow connct to instance folder

# Setting up configuration
app.config.from_object(DevConfig)#imports dev config class
app.config.from_pyfile('config.py')

from app import views