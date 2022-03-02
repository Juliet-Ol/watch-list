# from flask import Flask #import flask from flask module
# from ensurepip import bootstrap
import imp
from flask import Flask
from flask_bootstrap import Bootstrap # import bootstrap
from config import config_options

# Initializing application
def create_app(config_name):
    
    app = Flask(__name__) #create app instance and allow connct to instance folder
    # creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initializing flask extensions
    bootstrap = Bootstrap(app)

    #expects views nad forms

    return app
