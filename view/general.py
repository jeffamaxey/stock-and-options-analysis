from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

general_bp = Blueprint("general", __name__)


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
        register(email=email, password1=password, redirect_url="payment.payment", product=product)

    return render_template("landing-page.html", user=current_user)


@general_bp.route("/contact")
def contact():
    return render_template("contact-page.html", user=current_user)


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

