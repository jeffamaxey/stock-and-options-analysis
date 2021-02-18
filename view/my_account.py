from flask import Blueprint, render_template
from flask_login import login_required, current_user

my_account_bp = Blueprint("my_account", __name__)


@my_account_bp.route("/my-account")
@login_required     # Make sure the user can't access their account page when not logged in
def delete_user():
    return render_template("my_account.html", user=current_user)
