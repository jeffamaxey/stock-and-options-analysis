from flask import Blueprint, render_template, request, flash, redirect, url_for
from view import user_db
from database.User import User
from werkzeug.security import generate_password_hash

sign_up_bp = Blueprint("sign_up", __name__)

MIN_EMAIL_LEN = 4
MIN_FIRST_NAME_LEN = 2
MIN_PASSWORD_LEN = 7


@sign_up_bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # Reads the input data when the user presses the submit button
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:    # Check if the entered email already exists in the database
            flash("The email is already used. Please try another email.", category="Error")
        elif len(email) < MIN_EMAIL_LEN:
            flash("Email must be at least " + str(MIN_EMAIL_LEN) + " characters.", category="Error")
        elif len(first_name) < MIN_FIRST_NAME_LEN:
            flash("First name must be at least " + str(MIN_FIRST_NAME_LEN) + " characters.", category="Error")
        elif password1 != password2:
            flash("Two passwords don't match", category="Error")
        elif len(password1) < MIN_PASSWORD_LEN:
            flash("Password must be at least " + str(MIN_FIRST_NAME_LEN) + " characters.", category="Error")
        else:
            # Add the new user to the database
            encrypted_password = generate_password_hash(password1, method="sha256")
            new_user = User(email=email, first_name=first_name, password=encrypted_password)
            user_db.session.add(new_user)
            user_db.session.commit()

            flash("Account has been successfully created!", category="Success")

            return redirect(url_for("views.home"))  # redirect the user to the homepage

    return render_template("sign_up.html")
