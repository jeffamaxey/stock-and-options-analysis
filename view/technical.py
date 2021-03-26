from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

technical_analysis_bp = Blueprint("technical", __name__)

technical_analysis_data = []  # using a list instead of variable since it is mutable in a function

from view.general import input_field


@technical_analysis_bp.route("/technical-analysis", methods=["GET", "POST"])
@login_required
def technical_analysis():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-15")
        if ticker is None:
            input_field(ticker, "ticker-of-the-underlying-115", "ticker-of-the-underlying-125",
                        "ticker-of-the-underlying-135")

        data_source = request.form.get("data-source15")
        if data_source is None:
            input_field(data_source, "data-source115", "option-style129", "data-source125")

        from control.controller import get_technical_analysis
        analysis = get_technical_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
            return redirect(url_for("technical.technical_analysis"))
        else:
            technical_analysis_data.insert(0, analysis)
            return redirect(url_for("technical.technical_analysis_result"))

    return render_template("technical-analysis-page.html", user=current_user)


@technical_analysis_bp.route("/technical-analysis/result", methods=["GET", "POST"])
@login_required
def technical_analysis_result():
    # when the user entered the page by pressing the analyze button
    if request.method == "POST":
        ticker = request.form.get("ticker-of-the-underlying-19")
        if ticker is None:
            input_field(ticker, "ticker-of-the-underlying-119", "ticker-of-the-underlying-129",
                        "ticker-of-the-underlying-139")

        data_source = request.form.get("data-source19")
        if data_source is None:
            input_field(data_source, "data-source119", "option-style139", "data-source129")

        from control.controller import get_technical_analysis
        analysis = get_technical_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
            return redirect(url_for("technical.technical_analysis"))
        else:
            technical_analysis_data.insert(0, analysis)
            return redirect(url_for("technical.technical_analysis_result"))

    # when the user entered the page without pressing the analyze button
    try:
        analysis = technical_analysis_data[0]
    except IndexError:  # if this exception is thrown, it means the user refreshed the result page or entered by
        # simply tying the url
        return redirect(url_for("technical.technical_analysis"))

    technical_details = analysis["technical_details"]

    # clear the list so it doesn't grow as the user analyzes multiple times
    technical_analysis_data.clear()

    return render_template("technical-analysis-page2.html", user=current_user,
                           rsi=technical_details["RSI"],
                           macd=technical_details["MACD"],
                           mri=technical_details["MRI"],
                           moving_avgs=technical_details["MOVING AVGS (30, 10)"],
                           fibonacci_targets=technical_details["FIBONACCI TARGETS"]
                           )
