"""
Author: Sahngwoo Kim
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import UserDB
from flask_login import login_user, current_user, login_required, logout_user
from view.general import read_field

auth_bp = Blueprint("auth", __name__)


def register(email, password1, password2=None, agreed=None, product=None):
    """
    Check if the values are valid and if so, add the user to the database
    :param email: The email address of the user
    :param password1: The password of the user
    :param password2: The confirmation of the password
    :param agreed: Result of the checkbox whether the user agreed the term of the condition or not
    :param product: The subscription plan chosen
    :return: True if the registration was successful, False otherwise
    """
    from view.payment import PRODUCTS

    if UserDB.has(email):
        flash("The email is already used. Please try another email.", category="Error")
    elif len(email) < UserDB.MIN_EMAIL_LEN:
        flash(
            f"Email must be at least {str(UserDB.MIN_EMAIL_LEN)} characters.",
            category="Error",
        )
    elif len(email) > UserDB.MAX_EMAIL_LEN:
        flash(
            f"Email must be no longer than {str(UserDB.MAX_EMAIL_LEN)} characters.",
            category="Error",
        )
    elif password2 is not None and password1 != password2:
        flash("Two passwords don't match", category="Error")
    elif len(password1) < UserDB.MIN_PASSWORD_LEN:
        flash(
            f"Password must be at least {str(UserDB.MIN_PASSWORD_LEN)} characters.",
            category="Error",
        )
    elif len(password1) > UserDB.MAX_PASSWORD_LEN:
        flash(
            f"Password must be no longer than {str(UserDB.MAX_PASSWORD_LEN)} characters.",
            category="Error",
        )
    elif agreed is not None and agreed != "on":
        flash("You must agree to the terms and conditions", category="Error")
    elif product is not None and product not in PRODUCTS:
        flash(
            f"The product {product} is not valid. Please choose one of these: {str(PRODUCTS)}",
            category="Error",
        )
    else:
        # Add the new user account to the database
        UserDB.add(email, password1)

        # Keep the user logged in
        user = UserDB.get(email)
        login_user(user, remember=True)

        flash("Account has been successfully created!", category="Success")
        return True

    return False


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = read_field(("email12", "email19", "email114", "email119"))
        password = read_field(("password11", "password16", "password19", "password112"))

        if UserDB.has(email):
            if UserDB.check_password(email, password):
                flash("Logged in successfully!", category="Success")

                # Keep the user logged in
                user = UserDB.get(email)
                login_user(user, remember=True)

                return redirect(url_for("general.home"))  # redirect the user to the homepage
            else:
                flash("Incorrect password, please try again.", category="Error")
        else:
            flash("The email is not yet registered.", category="Error")

    return render_template("login-page.html", user=current_user)


@auth_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = read_field(("email13", "email110", "email115", "email120"))
        password1 = read_field(("password12", "password17", "password110", "password113"))
        password2 = read_field(("repeat-password1", "repeat-password11", "repeat-password12", "repeat-password13"))
        agreed = read_field(("checkbox1", "checkbox2", "checkbox3", "checkbox4"))

        if successful := register(
            email=email,
            password1=password1,
            password2=password2,
            agreed=agreed,
        ):
            return redirect(url_for("payment.payment"))

    return render_template("signup-page.html", user=current_user)


@auth_bp.route("/password-recovery", methods=["GET", "POST"])
def password_recovery():
    if request.method == "POST":
        email = read_field(("email14", "email111", "email116", "email121"))

    return render_template("password-recovery-page.html", user=current_user)


@auth_bp.route("/logout")
@login_required     # Make sure user cannot logout when the user is not logged in
def logout():
    logout_user()
    flash("You are logged out.", category="Success")
    return redirect((url_for("auth.login")))   # redirect the user to the login page


@auth_bp.route("/delete-account", methods=["GET", "POST"])
@login_required     # Make sure the user can't delete their account when not logged in
def delete_user():
    if request.method == "POST":
        password = read_field(("password12", "password17", "password110", "password113"))

        if UserDB.check_password(current_user.email, password):
            UserDB.delete(current_user.email)
            flash("Your account has been successfully deleted.", category="Success")
            return redirect(url_for("general.home"))     # redirect the user to the home page
        else:
            flash("Incorrect password. Please try again.", category="Error")

    return render_template("delete-account.html", user=current_user)
