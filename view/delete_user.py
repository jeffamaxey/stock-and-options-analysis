from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user
from database import UserDB

delete_user_bp = Blueprint("delete_user", __name__)


@delete_user_bp.route("/delete-account", methods=["GET", "POST"])
@login_required     # Make sure the user can't delete their account when not logged in
def delete_user():
    if request.method == "POST":
        password = request.form.get("password")

        if UserDB.check_password(current_user.email, password):
            UserDB.delete(current_user.email)
            flash("Your account has been successfully deleted.", category="Success")
            return redirect(url_for("login.login"))     # redirect the user to the login page
        else:
            flash("Incorrect password. Please try again.", category="Error")

    return render_template("delete_user.html", user=current_user)
