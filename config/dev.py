import os
basedir = os.path.abspath(os.path.dirname(__file__))

from . import BaseConfig

class DevelopmentConfig(BaseConfig):
	DEBUG=True
	SERVER_URI=os.environ.get('SERVER_URI')
	SECRET_KEY=os.environ.get('SECRET_KEY')
	AUTH_PASSWORD=os.environ.get('AUTH_PASSWORD')
	if not SECRET_KEY:
		SECRET_KEY=os.urandom(64)
	# SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or 'postgresql://postgres:meliodas@localhost:5432/librarydb'