from flask import Flask

def register_blueprint(app: Flask):

	from project.api.user import user_blueprint
	app.register_blueprint(user_blueprint, url_prefix="/api")

	from project.api.book import book_blueprint
	app.register_blueprint(book_blueprint, url_prefix="/api")

	from project.api.transaction import trans_blueprint
	app.register_blueprint(trans_blueprint, url_prefix="/api")