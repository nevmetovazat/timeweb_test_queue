# app factory will be here

from flask import Flask

from . import settings
from .views import bp as main


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    app.register_blueprint(main)

    return app
