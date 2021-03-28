from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

general_bp = Blueprint("general", __name__)


def read_field(keys):
    """
    Read the value in a input field from the website by trying with multiple keys, and return the first found value.
    If the value is not found with all of the keys, then return None
    :param keys: A tuple of the keys to read
    :return: The first read value
    """
    for key in keys:
        value = request.form.get(key)
        # If found the first value
        if value is not None:
            return value
    return None


@general_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = read_field(("email1", "email17", "email112", "email117"))
        password = read_field(("password1", "password15", "password18", "password111"))
        product = read_field(("product21", "product23", "product25", "product27"))

        from view.auth import register
        successful = register(email=email, password1=password, product=product)

        if successful:
            return redirect(url_for("payment.payment"))

    return render_template("landing-page.html", user=current_user)


@general_bp.route("/profile")
@login_required     # Make sure the user can't access their profile page when not logged in
def profile():
    return render_template("profile-page.html", user=current_user)


@general_bp.route("/tutorial")
def tutorial():
    return render_template("video-player-page.html", user=current_user)


@general_bp.route("/tutorial2")
def tutorial2():
    return render_template("video-player-page.html", user=current_user)

