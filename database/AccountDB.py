from os import path
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


account_db = SQLAlchemy()    # database for user accounts
__USER_DATABASE_PATH = "../database/account.db"


def create(app):
    """
    Create a user account database if there is no user database
    :param app: The app created by create_app()
    """

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + __USER_DATABASE_PATH
    account_db.init_app(app)

    if not path.exists(__USER_DATABASE_PATH):  # Check if the user database doesn't exist
        account_db.create_all(app=app)
        print("Created user account database!")


def add(email, first_name, password):
    """
    Add the account to the account database
    :param email: The email of the user
    :param first_name: The first name of the user
    :param password: The unencrypted password of the user
    """
    from model.Account import Account

    encrypted_password = generate_password_hash(password, method="sha256")
    new_account = Account(email=email, first_name=first_name, password=encrypted_password)
    account_db.session.add(new_account)
    account_db.session.commit()


def get(email):
    """
    Find the account and return the account object
    :param email: The email address
    :return: The account object
    """
    from model.Account import Account

    return Account.query.filter_by(email=email).first()


def has(email):
    """
    Check if the email already exists in the account database
    :param email: The email address of the user
    :return: True if the email exists, False otherwise
    """
    account = get(email)
    return account is not None


def check_password(email, password):
    """
    Check if the email and password match
    :param email: The email address of the user
    :param password: The unencrypted password of the user
    :return: True if they match, False otherwise
    """
    account = get(email)
    return check_password_hash(account.password, password)
