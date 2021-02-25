from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import UserDB
from flask_login import login_user, current_user

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if UserDB.has(email):
            if UserDB.check_password(email, password):
                flash("Logged in successfully!", category="Success")

                # Keep the user logged in
                user = UserDB.get(email)
                login_user(user, remember=True)

                return redirect(url_for("home.home"))  # redirect the user to the homepage
            else:
                flash("Incorrect password, please try again.", category="Error")
        else:
            flash("The email is not yet registered.", category="Error")

    return render_template("loginpage.html", user=current_user)
