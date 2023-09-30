from flask import Flask

app = Flask(__name__) # Instance of WSGI application

from app import routes # Importing from current directory app,
                       # in which module 'routes' needs
                       # to import variable 'app' above.
                       # Therefore this import needs to be
                       # defined after the variable app.
