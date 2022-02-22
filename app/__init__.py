from flask import Flask #import flask from flask module

# Initializing application
app = Flask(__name__) #create app instance

from app import views