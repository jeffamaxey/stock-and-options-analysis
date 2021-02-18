from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

logout_bp = Blueprint("logout", __name__)


@logout_bp.route("/logout")
@login_required     # Make sure user cannot logout when the user is not logged in
def logout():
    logout_user()
    return redirect((url_for("login.login")))   # redirect the user to the login page
