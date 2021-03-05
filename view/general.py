from flask import Blueprint, render_template
from flask_login import current_user, login_required

general_bp = Blueprint("general", __name__)


@general_bp.route("/")
def home():
    return render_template("landing-page.html", user=current_user)


@general_bp.route("/contact")
def contact():
    return render_template("contact-page.html", user=current_user)


@general_bp.route("/profile")
@login_required     # Make sure the user can't access their profile page when not logged in
def profile():
    return render_template("profile-page.html", user=current_user)

