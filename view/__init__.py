from flask import Flask
from database import UserDB
from flask_login import LoginManager
import ray

URL_PREFIX = "/"


def create_app():
    """
    Create and initialize a runnable app object
    :return: The runnable app object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "yK#b0Yj38&@7ubv"

    # Import Blueprint objects for pages
    from view.general import general_bp
    from view.auth import auth_bp
    from view.strategies import strategies_bp
    from view.fundamental import fundamental_analysis_bp
    from view.technical import technical_analysis_bp
    from view.pricing_valuation import pricing_valuation_bp
    from view.payment import payment_bp
    from view.contact import contact_bp

    # Register blueprints
    blueprints = [general_bp, auth_bp, strategies_bp, fundamental_analysis_bp, technical_analysis_bp,
                  pricing_valuation_bp, payment_bp, contact_bp]
    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix=URL_PREFIX)

    # initialize the user account database
    UserDB.init(app)

    # Manages the login feature
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # redirect to the page when the user is not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        try:
            return UserDB.get_by_id(id)
        except LookupError:
            return None

    # initialize the multithreading module
    ray.init(ignore_reinit_error=True)

    # Use Message and Mail with Flask-Mail imports to config SMTP settings
    from view.contact import mail
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config['MAIL_USE_TLS'] = False
    app.config["MAIL_USERNAME"] = 'thefintechorgtest@gmail.com'
    app.config["MAIL_PASSWORD"] = 'FTO12345'
    app.config['MAIL_DEFAULT_SENDER'] = 'thefintechorgtest@gmail.com'
    mail.init_app(app)

    return app
