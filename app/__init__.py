from flask import Flask

from app.config import DevConfig #import flask from flask module

# Initializing application
app = Flask(__name__) #create app instance

# Setting up configuration
app.config.from_object(DevConfig)

from app import views