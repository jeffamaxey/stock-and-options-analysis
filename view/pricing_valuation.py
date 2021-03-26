from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from view.general import read_field

pricing_valuation_bp = Blueprint("pricing_valuation", __name__)

__pricing_valuation_data = []  # using a list instead of variable since it is mutable in a function


@pricing_valuation_bp.route("/pricing-valuation", methods=["GET", "POST"])
@login_required
def pricing_valuation():
    if request.method == "POST":
        ticker = read_field(("ticker-of-the-underlying-1", "ticker-of-the-underlying-111",
                             "ticker-of-the-underlying-121", "ticker-of-the-underlying-131"))
        expiration_date = read_field(("expiration-date1", "expiration-date17", "expiration-date113",
                                      "expiration-date119"))
        option_type = read_field(("option-type1", "option-type17", "option-type114", "option-type113"))
        option_style = read_field(("option-style1", "option-style17", "option-style113", "option-style141"))
        data_source = read_field(("data-source1", "data-source111", "data-source115", "data-source121"))
        itm_atm_otm = read_field(("itm-atm-otm1", "itm-atm-otm17", "itm-atm-otm116", "itm-atm-otm113"))

    return render_template("pricing-and-valuation-page.html", user=current_user)


@pricing_valuation_bp.route("/pricing-valuation/result", methods=["GET", "POST"])
@login_required
def pricing_valuation_result():
    if request.method == "POST":
        ticker = read_field(("ticker-of-the-underlying-17", "ticker-of-the-underlying-117",
                             "ticker-of-the-underlying-127", "ticker-of-the-underlying-137"))
        expiration_date = read_field(("expiration-date15", "expiration-date111", "expiration-date117",
                                      "expiration-date123"))
        option_type = read_field(("option-type15", "option-type111", "option-type132", "option-type117"))
        option_style = read_field(("option-style15", "option-style111", "option-style131", "option-style145"))
        data_source = read_field(("data-source17", "data-source117", "option-style133", "data-source127"))
        item_atm_otm = read_field(("itm-atm-otm15", "itm-atm-otm111", "itm-atm-otm134", "itm-atm-otm117"))

    return render_template("pricing-and-valuation-page2.html", user=current_user)


@pricing_valuation_bp.route("/pricing-valuation/export")
@login_required
def pricing_valuation_export():
    return redirect(url_for("pricing_valuation.pricing_valuation"))
