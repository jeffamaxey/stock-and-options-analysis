from flask import Blueprint, render_template
from flask_login import login_required, current_user

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
@login_required     # Make sure the user can't go to the homepage when the user is not logged in
def home():
    return render_template("home.html", user=current_user)

