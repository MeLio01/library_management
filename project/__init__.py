__version__ = '0.1.0'

import os
from flask import Flask, app
from dotenv import load_dotenv

from .extensions import db, migrate
from .blueprints_registry import register_blueprint

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=f"[%(asctime)s]: {os.getpid()} %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)
logger = logging.getLogger()

def create_app():

	load_dotenv(".flaskenv")
	app = Flask(__name__)

	#from flask_cors import CORS
	#CORS(app)

	app_settings = os.environ.get("APP_SETTINGS")
	app.config.from_object(app_settings)

	register_blueprint(app)
	register_models()
	add_extensions(app)
	error_handler_registry(app)

	return app

def add_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db, compare_type=True)

def register_models():
	from project.api.user import UserDB
	from project.api.book import BookDB
	from project.api.transaction import transactionDB

#def populate_db(app):
#	from project.api.event import populate_events
#	populate_events(app)

def error_handler_registry(app: Flask):
    """Register functions with application
    :param app: Flask Instance
    :return None
    """
    from project.lib.errors import (
        BadRequest,
        ServerError,
        bad_request_handler,
        server_error_handler,
    )

    app.register_error_handler(BadRequest, bad_request_handler)
    app.register_error_handler(ServerError, server_error_handler)