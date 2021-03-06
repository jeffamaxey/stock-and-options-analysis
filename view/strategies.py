from flask import Blueprint, render_template
from flask_login import current_user, login_required

strategies_bp = Blueprint("strategies", __name__)


@strategies_bp.route("/strategies")
@login_required
def strategies():
    return render_template("strategies-page.html", user=current_user)


@strategies_bp.route("/strategies/breakdown")
@login_required
def strategies_breakdown():
    return render_template("strategies-page2.html", user=current_user)


@strategies_bp.route("/strategies/breakdown/asset")
@login_required
def strategies_breakdown_asset():
    return render_template("strategies-page-addasset.html", user=current_user)


@strategies_bp.route("strategies/breakdown/long-call")
@login_required
def long_call():
    return render_template("strategies-breakdown-longcall.html", user=current_user)


@strategies_bp.route("strategies/breakdown/long-put")
@login_required
def long_put():
    return render_template("375-strategies-breakdown2.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-call")
@login_required
def short_call():
    return render_template("375-strategies-breakdown3.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-put")
@login_required
def short_put():
    return render_template("375-strategies-breakdown4.html", user=current_user)


@strategies_bp.route("strategies/breakdown/covered-call")
@login_required
def covered_call():
    return render_template("768-strategies-breakdown-5.html", user=current_user)


@strategies_bp.route("strategies/breakdown/married-put")
@login_required
def married_put():
    return render_template("768-strategies-breakdown-6.html", user=current_user)


@strategies_bp.route("strategies/breakdown/bullCall-spread")
@login_required
def bull_call_spread():
    return render_template("768-strategies-breakdown-7.html", user=current_user)


@strategies_bp.route("strategies/breakdown/bear-put-spread")
@login_required
def bear_put_spread():
    return render_template("768-strategies-breakdown-8.html", user=current_user)


@strategies_bp.route("strategies/breakdown/protective-collar")
@login_required
def protective_collar():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/calendar-spread")
@login_required
def calendar_spread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/butterfly-spread")
@login_required
def butterfly_spread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/iron-condor")
@login_required
def iron_condor():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/iron-butterfly")
@login_required
def iron_butterfly():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/long-straddle")
@login_required
def long_straddle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/long-strangle")
@login_required
def long_strangle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-straddle")
@login_required
def short_straddle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-strangle")
@login_required
def short_strangle():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/call-backspread")
@login_required
def call_backspread():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/synthetic-short")
@login_required
def synthetic_short():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/risk-reversal")
@login_required
def risk_reversal():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/long-diagonal-call")
@login_required
def long_diagonal_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-diagonal-call")
@login_required
def short_diagonal_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/short-diagonal-put")
@login_required
def short_diagonal_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/l-christmas-tree-call")
@login_required
def l_christmas_tree_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/l-christmas-tree-put")
@login_required
def l_christmas_tree_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/s-christmas-tree-call")
@login_required
def s_christmas_tree_call():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/s-christmas-tree-put")
@login_required
def s_christmas_tree_put():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/delta-hedge")
@login_required
def delta_hedge():
    return render_template("HelloWorld.html", user=current_user)


@strategies_bp.route("strategies/breakdown/delta-gamma-hedge")
@login_required
def delta_gamma_hedge():
    return render_template("HelloWorld.html", user=current_user)
