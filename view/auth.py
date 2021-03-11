from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import UserDB
from flask_login import login_user, current_user, login_required, logout_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get("email12")
        if email is None:
            email = request.form.get("email19")
        if email is None:
            email = request.form.get("email114")
        if email is None:
            email = request.form.get("email119")

        password = request.form.get("password11")
        if password is None:
            password = request.form.get("password16")
        if password is None:
            password = request.form.get("password19")
        if password is None:
            password = request.form.get("password112")

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


def register(email, password1, password2=None, agreed=None, redirect_url="/", product=None):
    """
    Check if the values are valid and if so, add the user to the database
    :param email: The email address of the user
    :param password1: The password of the user
    :param password2: The confirmation of the password
    :param agreed: Result of the checkbox whether the user agreed the term of the condition or not
    :param redirect_url: The url to redirect when the registration was successful
    :param product: The subscription plan chosen
    """
    MIN_EMAIL_LEN = 6
    MIN_PASSWORD_LEN = 6
    products = ["BASIC", "BUNDLED", "DELUXE"]

    if UserDB.has(email):
        flash("The email is already used. Please try another email.", category="Error")
    elif len(email) < MIN_EMAIL_LEN:
        flash("Email must be at least " + str(MIN_EMAIL_LEN) + " characters.", category="Error")
    elif password2 is not None and password1 != password2:
        flash("Two passwords don't match", category="Error")
    elif len(password1) < MIN_PASSWORD_LEN:
        flash("Password must be at least " + str(MIN_PASSWORD_LEN) + " characters.", category="Error")
    elif agreed is not None and agreed != "on":
        flash("You must agree to the terms and conditions", category="Error")
    elif product is not None and product not in products:
        flash("The product " + product + " is not valid. Please choose one of these: " + str(products), category="Error")
    else:
        # Add the new user account to the database
        UserDB.add(email, password1)

        # Keep the user logged in
        user = UserDB.get(email)
        login_user(user, remember=True)

        flash("Account has been successfully created!", category="Success")

        return redirect(url_for(redirect_url))  # redirect the user


@auth_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # Reads the input data when the user presses the submit button
    if request.method == "POST":

        email = request.form.get("email13")
        if email is None:
            email = request.form.get("email110")
        if email is None:
            email = request.form.get("email115")
        if email is None:
            email = request.form.get("email120")

        password1 = request.form.get("password12")
        if password1 is None:
            password1 = request.form.get("password17")
        if password1 is None:
            password1 = request.form.get("password110")
        if password1 is None:
            password1 = request.form.get("password113")

        password2 = request.form.get("repeat-password1")
        if password2 is None:
            password2 = request.form.get("repeat-password11")
        if password2 is None:
            password2 = request.form.get("repeat-password12")
        if password2 is None:
            password2 = request.form.get("repeat-password13")

        agreed = request.form.get("checkbox1")
        if agreed is None:
            agreed = request.form.get("checkbox2")
        if agreed is None:
            agreed = request.form.get("checkbox3")
        if agreed is None:
            agreed = request.form.get("checkbox4")

        register(email, password1, password2, agreed, "payment.payment")

    return render_template("signup-page.html", user=current_user)


@auth_bp.route("/password-recovery", methods=["GET", "POST"])
def password_recovery():
    if request.method == "POST":

        email = request.form.get("email14")
        if email is None:
            email = request.form.get("email111")
        if email is None:
            email = request.form.get("email116")
        if email is None:
            email = request.form.get("email121")

    return render_template("password-recovery-page.html", user=current_user)


@auth_bp.route("/logout")
@login_required     # Make sure user cannot logout when the user is not logged in
def logout():
    logout_user()
    return redirect((url_for("login")))   # redirect the user to the login page


@auth_bp.route("/delete-account", methods=["GET", "POST"])
@login_required     # Make sure the user can't delete their account when not logged in
def delete_user():
    if request.method == "POST":

        password = request.form.get("password12")
        if password is None:
            password = request.form.get("password17")
        if password is None:
            password = request.form.get("password110")
        if password is None:
            password = request.form.get("password113")

        if UserDB.check_password(current_user.email, password):
            UserDB.delete(current_user.email)
            flash("Your account has been successfully deleted.", category="Success")
            return redirect(url_for("auth.login"))     # redirect the user to the login page
        else:
            flash("Incorrect password. Please try again.", category="Error")

    return render_template("delete-account.html", user=current_user)
