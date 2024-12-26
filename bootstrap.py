from flask import Flask
import blueprints.index
import blueprints.auth
import blueprints.product

from db import init_mysql


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_pyfile("settings.py")
    init_mysql(app)

    app.register_blueprint(blueprints.index.bp)
    app.register_blueprint(blueprints.auth.bp)
    app.register_blueprint(blueprints.product.bp)

    return app
