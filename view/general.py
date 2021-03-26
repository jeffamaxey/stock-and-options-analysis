from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

general_bp = Blueprint("general", __name__)


def input_field(the_type, second, third, fourth):  # to save code space on all views
    the_type = request.form.get(second)
    if the_type is None:
        the_type = request.form.get(third)
    if the_type is None:
        the_type = request.form.get(fourth)


@general_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        email = request.form.get("email1")
        if email is None:
            email = request.form.get("email17")
        if email is None:
            email = request.form.get("email112")
        if email is None:
            email = request.form.get("email117")

        password = request.form.get("password1")
        if password is None:
            password = request.form.get("password15")
        if password is None:
            password = request.form.get("password18")
        if password is None:
            password = request.form.get("password111")

        product = request.form.get("product21")
        if product is None:
            product = request.form.get("product23")
        if product is None:
            product = request.form.get("product25")
        if product is None:
            product = request.form.get("product27")

        from view.auth import register
        register(email=email, password1=password, product=product)
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

