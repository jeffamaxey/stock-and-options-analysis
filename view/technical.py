from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

technical_analysis_bp = Blueprint("technical", __name__)

__technical_analysis_data = []  # using a list instead of variable since it is mutable in a function


@technical_analysis_bp.route("/technical-analysis", methods=["GET", "POST"])
@login_required
def technical_analysis():
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-15")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-115")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-125")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-135")

        data_source = request.form.get("data-source15")
        if data_source is None:
            data_source = request.form.get("data-source115")
        if data_source is None:
            data_source = request.form.get("option-style129")
        if data_source is None:
            data_source = request.form.get("data-source125")

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
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-19")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-119")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-129")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-139")

        data_source = request.form.get("data-source19")
        if data_source is None:
            data_source = request.form.get("data-source119")
        if data_source is None:
            data_source = request.form.get("option-style139")
        if data_source is None:
            data_source = request.form.get("data-source129")

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
        return redirect(url_for("fundamental.fundamental_analysis"))

    # clear the list so it doesn't grow as the user analyzes multiple times
    __technical_analysis_data.clear()

    technical_analysis_data = analysis["technical_analysis_data"]
    summary = analysis["summary"]

    return render_template("technical-analysis-page2.html", user=current_user,
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
    return redirect(url_for("technical.technical_analysis"))
