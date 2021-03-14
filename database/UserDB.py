from os import path
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


user_db = SQLAlchemy()    # database for users
__USER_DB_PATH = "../database/user.db"


def create(app):
    """
    Create a user database if there is no user database
    :param app: The app created by create_app()
    """

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + __USER_DB_PATH
    user_db.init_app(app)

    if not path.exists(__USER_DB_PATH):  # Check if the user database doesn't exist
        user_db.create_all(app=app)


def add(email, password):
    """
    Add the user to the user database
    :param email: The email of the user
    :param first_name: The first name of the user
    :param password: The unencrypted password of the user
    """
    from model.User import User

    encrypted_password = generate_password_hash(password, method="sha256")
    new_user = User(email=email, password=encrypted_password)
    user_db.session.add(new_user)
    user_db.session.commit()


def get(email):
    """
    Find the user and return the user object
    :param email: The email address of the user
    :return: The user object
    """
    from model.User import User
    user = User.query.filter_by(email=email).first()
    if user is None:
        raise LookupError("The user is not found in the user database to get.")

    return user


def get_by_id(id):
    """
    Find the user by id and return the user object
    :param id: The id of the user
    :return: The user object
    """
    from model.User import User
    user = User.query.get(int(id))
    if user is None:
        raise LookupError("The user is not found in the user database to get.")

    return user


def has(email):
    """
    Check if the email already exists in the user database
    :param email: The email address of the user
    :return: True if the email exists, False otherwise
    """
    from model.User import User
    user = User.query.filter_by(email=email).first()
    return user is not None


def check_password(email, password):
    """
    Check if the email and password match
    :param email: The email address of the user
    :param password: The unencrypted password of the user
    :return: True if they match, False otherwise
    """
    user = get(email)
    return check_password_hash(user.password, password)


def delete(email):
    """
    Delete the user from the user database
    :param email: The email address of the user
    """
    if not has(email):
        raise LookupError("The user is not found in the user database to delete.")

    user = get(email)
    user_db.session.delete(user)
    user_db.session.commit()
