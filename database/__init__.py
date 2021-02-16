from os import path
from flask_sqlalchemy import SQLAlchemy

user_db = SQLAlchemy()  # database for users

USER_DATABASE_PATH = "../database/user_database.db"


def create_user_database(app):
    """
    Create a user database if there is no user database
    :param app: The app created by create_app()
    """

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + USER_DATABASE_PATH
    user_db.init_app(app)

    if not path.exists(USER_DATABASE_PATH):  # Check if the user database doesn't exist
        user_db.create_all(app=app)
        print("Created user database!")


def add(user):
    """
    Add the user to the database
    :param user The user object to be added
    """
    user_db.session.add(user)
    user_db.session.commit()
