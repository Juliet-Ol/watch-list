from flask import Flask

from app.config import DevConfig #import flask from flask module

from .config import DevConfig

# Initializing application
app = Flask(__name__) #create app instance

# Setting up configuration
app.config.from_object(DevConfig)#imports dev config class

from app import views