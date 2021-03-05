from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import UserDB
from flask_login import login_user, current_user, login_required, logout_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email1")
        password = request.form.get("password1")

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

    return render_template("login-page.html", user=current_user)


MIN_EMAIL_LEN = 4
MIN_PASSWORD_LEN = 7


@auth_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # Reads the input data when the user presses the submit button
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if UserDB.has(email):
            flash("The email is already used. Please try another email.", category="Error")
        elif len(email) < MIN_EMAIL_LEN:
            flash("Email must be at least " + str(MIN_EMAIL_LEN) + " characters.", category="Error")
        elif password1 != password2:
            flash("Two passwords don't match", category="Error")
        elif len(password1) < MIN_PASSWORD_LEN:
            flash("Password must be at least " + str(MIN_PASSWORD_LEN) + " characters.", category="Error")
        else:
            # Add the new user account to the database
            UserDB.add(email, password1)

            # Keep the user logged in
            user = UserDB.get(email)
            login_user(user, remember=True)

            flash("Account has been successfully created!", category="Success")

            return redirect(url_for("home.home"))  # redirect the user to the homepage

    return render_template("signup-page.html", user=current_user)


@auth_bp.route("/logout")
@login_required     # Make sure user cannot logout when the user is not logged in
def logout():
    logout_user()
    return redirect((url_for("login")))   # redirect the user to the login page


@auth_bp.route("/delete-account", methods=["GET", "POST"])
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

    return render_template("HelloWorld.html", user=current_user)
