from flask_login import UserMixin
from database.AccountDB import account_db

MAX_EMAIL_LEN = 150
MAX_PASSWORD_LEN = 150
MAX_FIRST_NAME_LEN = 150


class Account(account_db.Model, UserMixin):
    """
    A user account of the website
    """

    id = account_db.Column(account_db.Integer, primary_key=True)
    email = account_db.Column(account_db.String(MAX_EMAIL_LEN), unique=True)
    password = account_db.Column(account_db.String(MAX_PASSWORD_LEN))
    first_name = account_db.Column(account_db.String(MAX_FIRST_NAME_LEN))
