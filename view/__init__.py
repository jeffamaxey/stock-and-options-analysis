from flask import Flask
from database import UserDB
from flask_login import LoginManager

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
    from view.delete_user import delete_user_bp
    from view.my_account import my_account_bp

    # Register pages
    blueprints = [home_bp, sign_up_bp, login_bp, logout_bp, delete_user_bp, my_account_bp]
    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix=URL_PREFIX)

    # Create the user account database
    UserDB.create(app)

    # Manages the login feature
    login_manager = LoginManager()
    login_manager.login_view = "login.login"  # redirect to the page when the user is not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        try:
            return UserDB.get_by_id(id)
        except LookupError:
            return None

    return app
