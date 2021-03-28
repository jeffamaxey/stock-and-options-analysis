from flask import Blueprint, render_template
from flask_login import current_user, login_required
from flask import request, flash, redirect, url_for

payment_bp = Blueprint("payment", __name__)

PRODUCTS = ("BASIC", "BUNDLED", "DELUXE")


@payment_bp.route("/payment", methods=["GET", "POST"])
@login_required
def payment():
    if request.method == "POST":
        flash("Our website is currently free!", category="Info")
        return redirect(url_for("general.home"))    # redirect the user to the homepage

    return render_template("payment-processing-page.html", user=current_user)


@payment_bp.route("/payment2", methods=["GET", "POST"])
@login_required
def payment2():
    return redirect(url_for("general.home"))    # redirect the user to the homepage
