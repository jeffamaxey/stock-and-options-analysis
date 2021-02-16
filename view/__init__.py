from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

user_db = SQLAlchemy()  # database for users
USER_DATABASE_PATH = "../database/user_database.db"

URL_PREFIX = "/"


def create_app():
    """
    Create a runnable app object
    :return: The runnable app object
    """

    app = Flask(__name__)  # the name of the file name
    app.config["SECRET_KEY"] = "yK#b0Yj38&@7ubv"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + USER_DATABASE_PATH
    user_db.init_app(app)

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

    create_user_database(app, USER_DATABASE_PATH)

    return app


def create_user_database(app, db_path):
    """
    Create a user database if there is no user database
    :param app: The app created by create_app()
    :param db_path: The path that user_database.db to be created
    """

    if not path.exists(db_path):  # Check if the user database doesn't exist
        user_db.create_all(app=app)
        print("Created user database!")
