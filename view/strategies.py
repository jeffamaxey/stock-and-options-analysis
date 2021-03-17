from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

strategies_bp = Blueprint("strategies", __name__)


@strategies_bp.route("/strategies", methods=["GET", "POST"])
@login_required
def strategies():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-11")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-112")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-122")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-132")

        expiration_date = request.form.get("expiration-date11")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date18")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date114")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date120")

        option_type = request.form.get("option-type11")
        if option_type is None:
            option_type = request.form.get("option-type18")
        if option_type is None:
            option_type = request.form.get("option-style118")
        if option_type is None:
            option_type = request.form.get("option-type114")

        option_style = request.form.get("option-style11")
        if option_style is None:
            option_style = request.form.get("option-style18")
        if option_style is None:
            option_style = request.form.get("option-style117")
        if option_style is None:
            option_style = request.form.get("option-style142")

        data_source = request.form.get("data-source11")
        if data_source is None:
            data_source = request.form.get("data-source112")
        if data_source is None:
            data_source = request.form.get("option-style119")
        if data_source is None:
            data_source = request.form.get("data-source122")

        itm_atm_otm = request.form.get("itm-atm-otm11")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm18")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("option-style120")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm114")


    return render_template("strategies-page.html", user=current_user)


@strategies_bp.route("/strategies/breakdown", methods=["GET", "POST"])
@login_required
def strategies_breakdown():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-18")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-118")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-128")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-138")

        expiration_date = request.form.get("expiration-date16")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date112")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date118")
        if expiration_date is None:
            expiration_date = request.form.get("expiration-date124")

        option_type = request.form.get("option-type16")
        if option_type is None:
            option_type = request.form.get("option-type112")
        if option_type is None:
            option_type = request.form.get("option-style136")
        if option_type is None:
            option_type = request.form.get("option-type118")

        option_style = request.form.get("option-style16")
        if option_style is None:
            option_style = request.form.get("option-style112")
        if option_style is None:
            option_style = request.form.get("option-style135")
        if option_style is None:
            option_style = request.form.get("option-style146")

        data_source = request.form.get("data-source18")
        if data_source is None:
            data_source = request.form.get("data-source118")
        if data_source is None:
            data_source = request.form.get("option-style137")
        if data_source is None:
            data_source = request.form.get("data-source128")

        itm_atm_otm = request.form.get("itm-atm-otm16")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm112")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("option-style138")
        if itm_atm_otm is None:
            itm_atm_otm = request.form.get("itm-atm-otm118")

    return render_template("strategies-page2.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/asset", methods=["GET", "POST"])
@login_required
def strategies_breakdown_asset():
    return render_template("strategies-page-addasset.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/long-call")
@login_required
def long_call():
    return render_template("strategies-breakdown-longcall.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/long-put")
@login_required
def long_put():
    return render_template("375-strategies-breakdown2.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-call")
@login_required
def short_call():
    return render_template("375-strategies-breakdown3.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-put")
@login_required
def short_put():
    return render_template("375-strategies-breakdown4.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/covered-call")
@login_required
def covered_call():
    return render_template("768-strategies-breakdown-5.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/married-put")
@login_required
def married_put():
    return render_template("768-strategies-breakdown-6.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/bull-call-spread")
@login_required
def bull_call_spread():
    return render_template("768-strategies-breakdown-7.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/bear-put-spread")
@login_required
def bear_put_spread():
    return render_template("768-strategies-breakdown-8.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/protective-collar")
@login_required
def protective_collar():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/calendar-spread")
@login_required
def calendar_spread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/butterfly-spread")
@login_required
def butterfly_spread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/iron-condor")
@login_required
def iron_condor():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/iron-butterfly")
@login_required
def iron_butterfly():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/long-straddle")
@login_required
def long_straddle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/long-strangle")
@login_required
def long_strangle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-straddle")
@login_required
def short_straddle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-strangle")
@login_required
def short_strangle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/call-backspread")
@login_required
def call_backspread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/synthetic-short")
@login_required
def synthetic_short():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/risk-reversal")
@login_required
def risk_reversal():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/long-diagonal-call")
@login_required
def long_diagonal_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-diagonal-call")
@login_required
def short_diagonal_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/short-diagonal-put")
@login_required
def short_diagonal_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/l-christmas-tree-call")
@login_required
def l_christmas_tree_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/l-christmas-tree-put")
@login_required
def l_christmas_tree_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/s-christmas-tree-call")
@login_required
def s_christmas_tree_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/s-christmas-tree-put")
@login_required
def s_christmas_tree_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/delta-hedge")
@login_required
def delta_hedge():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/delta-gamma-hedge")
@login_required
def delta_gamma_hedge():
    return render_template("HelloWorld.html", user=current_user)
