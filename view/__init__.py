from flask import Flask
from database import AccountDB

URL_PREFIX = "/"


def create_app():
    """
    Create a runnable app object
    :return: The runnable app object
    """

    app = Flask(__name__)  # the name of the file name
    app.config["SECRET_KEY"] = "yK#b0Yj38&@7ubv"

    # Import Blueprint objects
    from view.home import home_bp
    from view.sign_up import sign_up_bp
    from view.login import login_bp
    from view.logout import logout_bp

    # Register pages
    app.register_blueprint(home_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(sign_up_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(login_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(logout_bp, url_prefix=URL_PREFIX)

    # Create the user account database
    AccountDB.create(app)

    return app
