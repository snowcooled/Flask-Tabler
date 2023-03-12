# Welcome to the Flask-Tabler sample application. This will give you a
# guided tour around creating an application using Flask-Tabler.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#
# Then, you can actually run the application.
#
#   $ flask --app=sample_app dev
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.

from flask import Flask
#from flask_appconfig import AppConfig
from flask_tabler import Tabler

from .frontend import frontend
#from .nav import nav


def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    # We use Flask-Appconfig here, but this is not a requirement
    #AppConfig(app)

    # Install our Tabler extension
    Tabler(app)

    # Our application uses blueprints as well; these go well with the
    # application factory. We already imported the blueprint, now we just need
    # to register it:
    app.register_blueprint(frontend)

    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    #app.config['TABLER_SERVE_LOCAL'] = True

    # We initialize the navigation as well
    #nav.init_app(app)

    return app
