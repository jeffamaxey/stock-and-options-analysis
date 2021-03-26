from flask import Blueprint, render_template
from flask_login import current_user, login_required

payment_bp = Blueprint("payment", __name__)

PRODUCTS = ("BASIC", "BUNDLED", "DELUXE")


@payment_bp.route("/payment")
@login_required
def payment():
    return render_template("payment-processing-page.html", user=current_user)


@payment_bp.route("/payment2")
@login_required
def payment2():
    return render_template("payment-processing-page2.html", user=current_user)
