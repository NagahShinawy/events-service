from flask import Flask
from extensions import db, migrate, jwt
from api.views import root_bp, api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    configure_extensions(app)
    configure_jwt(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    migrate.init_app(app, db)


def configure_jwt(app):
    jwt.init_app(app)


def register_blueprints(app):
    """ Registers all blueprints for application """
    app.register_blueprint(root_bp)
    app.register_blueprint(api_bp)