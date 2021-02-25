from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import UserDB
from flask_login import login_user, current_user

sign_up_bp = Blueprint("sign_up", __name__)

MIN_EMAIL_LEN = 4
MIN_PASSWORD_LEN = 7


@sign_up_bp.route("/sign-up", methods=["GET", "POST"])
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

    return render_template("signuppage.html", user=current_user)
