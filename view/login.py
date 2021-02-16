from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import AccountDB

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if AccountDB.has(email):
            if AccountDB.check_password(email, password):
                flash("Logged in successfully!", category="Success")
                return redirect(url_for("home.home"))  # redirect the user to the homepage
            else:
                flash("Incorrect password, please try again.", category="Error")
        else:
            flash("The email is not yet registered.", category="Error")

    return render_template("login.html")
