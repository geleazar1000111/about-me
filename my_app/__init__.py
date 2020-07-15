from flask import Flask
from my_app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    with app.app_context():
        import my_app.routes
        return app
