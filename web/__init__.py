from flask import Flask

from .main import main_bp
from .accounts import accounts_bp
from .accounts.models import User
from .widgets import widgets_bp

from .extensions import login_manager, mongo

def create_app():
    app = Flask('widgether_web_server')

    app.config.update(
        SECRET_KEY='blahblah'
    )

    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True

    app.register_blueprint(main_bp, url_prefix='')
    app.register_blueprint(accounts_bp, url_prefix='/accounts')
    app.register_blueprint(widgets_bp, url_prefix='/widgets')

    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    mongo.init_app(app)

    return app