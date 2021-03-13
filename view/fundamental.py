from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

fundamental_analysis_bp = Blueprint("fundamental", __name__)

fundamental_analysis_data = []  # using a list instead of variable since it is mutable in a function


@fundamental_analysis_bp.route("/fundamental-analysis", methods=["GET", "POST"])
@login_required
def fundamental_analysis():

    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-16")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-116")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-126")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-136")

        data_source = request.form.get("data-source16")
        if data_source is None:
            data_source = request.form.get("data-source116")
        if data_source is None:
            data_source = request.form.get("option-style130")
        if data_source is None:
            data_source = request.form.get("data-source126")

        from control.controller import get_fundamental_analysis
        analysis = get_fundamental_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
        else:
            fundamental_analysis_data.insert(0, analysis)
            return redirect(url_for("fundamental.fundamental_analysis_result"))

    return render_template("fundamental-analysis-page.html", user=current_user)


@fundamental_analysis_bp.route("/fundamental-analysis/result")
@login_required
def fundamental_analysis_result():
    analysis = fundamental_analysis_data[0]
    stock_details = analysis["stock_details"]
    metrics = analysis["metrics"]
    dividends = analysis["dividends"]
    financial_statements = analysis["financial_statements"]
    news = analysis["news"]

    # clear the list so it doesn't grow as the user analyzes multiple times
    fundamental_analysis_data.clear()

    return render_template("fundamental-analysis-page2.html", user=current_user,
                           open=stock_details["open"],
                           close=stock_details["close"],
                           bid=stock_details["bid"],
                           ask=stock_details["ask"],
                           earnings_date=stock_details["earnings_date"],
                           twenty_four_hour_low=stock_details["twenty_four_hour_low"],
                           twenty_four_hour_high=stock_details["twenty_four_hour_high"],
                           fifty_two_week_low=stock_details["fifty_two_week_low"],
                           fifty_two_week_high=stock_details["fifty_two_week_high"],
                           year_estimate=stock_details["year_estimate"],
                           fair_value=metrics["fair_value"],
                           market_price=metrics["market_price"],
                           volume=metrics["volume"],
                           market_cap=metrics["market_cap"],
                           metrics_extra=metrics["extra"],
                           PE_ratio=metrics["PE_ratio"],
                           current_ratio=metrics["current_ratio"],
                           debt_to_equity=metrics["debt_to_equity"],
                           price_to_book_ratio=metrics["price_to_book_ratio"],
                           frequency=dividends["frequency"],
                           amount=dividends["amount"],
                           dividend_yield=dividends["dividend_yield"],
                           dividend_date=dividends["dividend_date"],
                           ex_dividend=dividends["ex_dividend"],
                           ddm=dividends["ddm"],
                           dgm=dividends["dgm"],
                           blended_forward_PE=dividends["blended_forward_PE"],
                           npv=dividends["npv"],
                           dividends_extra=dividends["extra"],
                           current_assets=financial_statements["current_assets"],
                           long_term_assets=financial_statements["long_term_assets"],
                           total_assets=financial_statements["total_assets"],
                           current_liabilities=financial_statements["current_liabilities"],
                           long_term_liabilities=financial_statements["long_term_liabilities"],
                           total_liabilities=financial_statements["total_liabilities"],
                           shareholders_equity=financial_statements["shareholders_equity"],
                           gross_revenue=financial_statements["gross_revenue"],
                           ebitda=financial_statements["ebitda"],
                           expenses=financial_statements["expenses"],
                           net_income=financial_statements["net_income"],
                           profit_margin=financial_statements["profit_margin"],
                           net_operating_cash=financial_statements["net_operating_cash"],
                           net_investing_cash=financial_statements["net_investing_cash"],
                           net_financing_cash=financial_statements["net_financing_cash"],
                           free_cash_flow=financial_statements["free_cash_flow"],
                           news=news
                           )


