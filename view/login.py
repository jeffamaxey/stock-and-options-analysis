from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from model.Account import Account

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Search the user in the database
        user = Account.query.filter_by(email=email).first()
        if user:    # If found user in the database
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="Success")
                return redirect(url_for("home.home"))  # redirect the user to the homepage
            else:
                flash("Incorrect password, please try again.", category="Error")
        else:
            flash("The email is not yet registered.", category="Error")

    return render_template("login.html")
