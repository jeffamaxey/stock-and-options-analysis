from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

pricing_valuation_bp = Blueprint("pricing_valuation", __name__)


@pricing_valuation_bp.route("/pricing-valuation", methods=["GET", "POST"])
@login_required
def pricing_valuation():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-1")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-111")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-121")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-131")

        expiration_date = request.form.get("expiration-date1")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date17")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date113")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date119")

        option_type = request.form.get("option-type1")
        if option_type is None:
            option_type = request.form.get("option-type17")
        if option_type is None:
            option_type = request.form.get("option-style114")
        if option_type is None:
            option_type = request.form.get("option-type113")

        option_style = request.form.get("option-style1")
        if option_style is None:
            option_style = request.form.get("option-style17")
        if option_style is None:
            option_style = request.form.get("option-style113")
        if option_style is None:
            option_style = request.form.get("option-style141")

        data_source = request.form.get("data-source1")
        if data_source is None:
            data_source = request.form.get("data-source111")
        if data_source is None:
            data_source = request.form.get("option-style115")
        if data_source is None:
            data_source = request.form.get("data-source121")

        itm_atm_otm = request.form.get("itm-atm-otm1")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm17")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("option-style116")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm113")

    return render_template("pricing-and-valuation-page.html", user=current_user)


@pricing_valuation_bp.route("/pricing-valuation/result", methods=["GET", "POST"])
@login_required
def pricing_valuation_result():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-17")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-117")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-127")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-137")

        expiration_date = request.form.get("expiration-date15")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date111")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date117")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date123")

        option_type = request.form.get("option-type15")
        if option_type is None:
            option_type = request.form.get("option-type111")
        if option_type is None:
            option_type = request.form.get("option-style132")
        if option_type is None:
            option_type = request.form.get("option-type117")

        option_style = request.form.get("option-style15")
        if option_style is None:
            option_style = request.form.get("option-style111")
        if option_style is None:
            option_style = request.form.get("option-style131")
        if option_style is None:
            option_style = request.form.get("option-style145")

        data_source = request.form.get("data-source17")
        if data_source is None:
            data_source = request.form.get("data-source117")
        if data_source is None:
            data_source = request.form.get("option-style133")
        if data_source is None:
            data_source = request.form.get("data-source127")

        itm_atm_otm = request.form.get("itm-atm-otm15")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm111")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("option-style134")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm117")

    return render_template("pricing-and-valuation-page2.html", user=current_user)


@pricing_valuation_bp.route("/pricing-valuation/export")
@login_required
def pricing_valuation_export():
    return redirect(url_for("pricing_valuation.pricing_valuation"))
