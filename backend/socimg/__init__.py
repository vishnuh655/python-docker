import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
# from socimg.routes import register_routes

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('APP_CONFIG_FILE')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app, title="SocIMG API", version="0.0.1")

    # register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app


application = create_app()
db = SQLAlchemy(application)
