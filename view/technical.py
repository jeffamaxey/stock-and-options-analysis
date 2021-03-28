"""
Author: Adam Bouthillette
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask_login import current_user, login_required
from view.general import read_field

technical_analysis_bp = Blueprint("technical", __name__)

__technical_analysis_data = []  # using a list instead of variable since it is mutable in a function


@technical_analysis_bp.route("/technical-analysis", methods=["GET", "POST"])
@login_required
def technical_analysis():
    """
    Reads input fields and relays to back end and retrieves data to present on screen
    """
    if request.method == "POST":

        ticker = read_field(("ticker-of-the-underlying-15", "ticker-of-the-underlying-115",
                             "ticker-of-the-underlying-125", "ticker-of-the-underlying-135"))
        data_source = read_field(("data-source15", "data-source115", "option-style129", "data-source125"))

        from control.controller import get_technical_analysis
        analysis = get_technical_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
            return redirect(url_for("technical.technical_analysis"))
        else:
            __technical_analysis_data.insert(0, analysis)
            return redirect(url_for("technical.technical_analysis_result"))

    return render_template("technical-analysis-page.html", user=current_user)


@technical_analysis_bp.route("/technical-analysis/result", methods=["GET", "POST"])
@login_required
def technical_analysis_result():
    """
    Reads input fields and relays to back end and retrieves data to present on screen
    """
    if request.method == "POST":

        ticker = read_field(("ticker-of-the-underlying-19", "ticker-of-the-underlying-119",
                             "ticker-of-the-underlying-129", "ticker-of-the-underlying-139"))
        data_source = read_field(("data-source19", "data-source119", "option-style139", "data-source129"))

        from control.controller import get_technical_analysis
        analysis = get_technical_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
            return redirect(url_for("technical.technical_analysis"))
        else:
            __technical_analysis_data.insert(0, analysis)
            return redirect(url_for("technical.technical_analysis_result"))

    # when the user entered the page without pressing the analyze button
    try:
        analysis = __technical_analysis_data[0]
    except IndexError:  # if this exception is thrown, it means the user refreshed the result page or entered by
        # simply typing the url
        return redirect(url_for("technical.technical_analysis"))

    # clear the list so it doesn't grow as the user analyzes multiple times
    __technical_analysis_data.clear()

    technical_analysis_data = analysis["tech_details"]
    summary = analysis["summary"]

    # render technical-analysis-page2.html to show chart and all data
    return render_template("technical-analysis-page2.html", user=current_user,
                           ticker=technical_analysis_data["ticker"],
                           exchange=technical_analysis_data["exchange"],
                           rsi=technical_analysis_data["RSI"],
                           macd=technical_analysis_data["MACD"],
                           mri=technical_analysis_data["MRI"],
                           moving_avg=technical_analysis_data["MOVING AVGS (30, 10)"],
                           fibonacci_targets=technical_analysis_data["FIBONACCI TARGETS"],

                           summary=summary
                           )


@technical_analysis_bp.route("/technical-analysis/export")
@login_required
def technical_analysis_export():
    file_path = "static/export/Technical.csv"
    return send_file(file_path, as_attachment=True)
