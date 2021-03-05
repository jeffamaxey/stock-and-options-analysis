from flask import Blueprint, render_template
from flask_login import current_user, login_required

pricing_valuation_bp = Blueprint("pricing_valuation", __name__)


@pricing_valuation_bp.route("/pricing-valuation")
@login_required
def pricing_valuation():
    return render_template("pricing-and-valuation-page.html", user=current_user)


@pricing_valuation_bp.route("/pricing-valuation/result")
@login_required
def pricing_valuation_result():
    return render_template("pricing-and-valuation-page2.html", user=current_user)
