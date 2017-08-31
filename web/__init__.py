from flask import Flask

from .accounts import accounts_bp
from .widgets import widgets_bp

def create_app():
    app = Flask('widgether_web_server')

    app.register_blueprint(accounts_bp, url_prefix='/accounts')
    app.register_blueprint(widgets_bp, url_prefix='/widgets')

    return app