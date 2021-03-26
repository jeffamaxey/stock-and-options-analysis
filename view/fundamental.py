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
            return redirect(url_for("fundamental.fundamental_analysis"))
        else:
            fundamental_analysis_data.insert(0, analysis)
            return redirect(url_for("fundamental.fundamental_analysis_result"))

    return render_template("fundamental-analysis-page.html", user=current_user)


@fundamental_analysis_bp.route("/fundamental-analysis/result", methods=["GET", "POST"])
@login_required
def fundamental_analysis_result():
    # when the user entered tha page by pressing the analyze button
    if request.method == "POST":

        ticker = request.form.get("ticker-of-the-underlying-110")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-120")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-130")
        if ticker is None:
            ticker = request.form.get("ticker-of-the-underlying-140")

        data_source = request.form.get("data-source110")
        if data_source is None:
            data_source = request.form.get("data-source120")
        if data_source is None:
            data_source = request.form.get("option-style140")
        if data_source is None:
            data_source = request.form.get("data-source130")

        from control.controller import get_fundamental_analysis
        analysis = get_fundamental_analysis(ticker=ticker, data_source=data_source)

        if analysis is None:
            flash("Invalid ticker. Please try again.", category="Error")
            return redirect(url_for("fundamental.fundamental_analysis"))
        else:
            fundamental_analysis_data.insert(0, analysis)
            return redirect(url_for("fundamental.fundamental_analysis_result"))

    # when the user entered the page without pressing the analyze button
    try:
        analysis = fundamental_analysis_data[0]
    except IndexError:  # if this exception is thrown, it means the user refreshed the result page or entered by simply tying the url
        return redirect(url_for("fundamental.fundamental_analysis"))

    # clear the list so it doesn't grow as the user analyzes multiple times
    fundamental_analysis_data.clear()

    stock_details = analysis["stock_details"]
    metrics = analysis["metrics"]
    dividends = analysis["dividends"]
    income_statements = analysis["income_statements"]
    news = analysis["news"]

    return render_template("fundamental-analysis-page2.html", user=current_user,
                           ticker=stock_details["ticker"],
                           company_name=stock_details["company_name"],
                           current_price_per_share=stock_details["current_price_per_share"],
                           open=stock_details["open"],
                           previous_close=stock_details["previous_close"],
                           bid=stock_details["bid"],
                           ask=stock_details["ask"],
                           earnings_date=stock_details["earnings_date"],
                           daily_range=stock_details["daily_range"],
                           fifty_two_week_range=stock_details["fifty_two_week_range"],
                           year_estimate=stock_details["year_estimate"],

                           fair_value=metrics["fair_value"],
                           volume=metrics["volume"],
                           three_month_average_volume=metrics["three_month_average_volume"],
                           market_cap=metrics["market_cap"],
                           EPS=metrics["EPS"],
                           Beta=metrics["Beta"],
                           PE_ratio=metrics["PE_ratio"],
                           current_ratio=metrics["current_ratio"],
                           debt_to_equity=metrics["debt_to_equity"],
                           price_to_book_ratio=metrics["price_to_book_ratio"],
                           price_fair_value_TTM=metrics["price_fair_value_TTM"],
                           return_on_equity_TTM=metrics["return_on_equity_TTM"],
                           price_earnings_to_growth_ratio_TTM=metrics["price_earnings_to_growth_ratio_TTM"],
                           return_on_assets_TTM=metrics["return_on_assets_TTM"],
                           return_on_capital_employed_TTM=metrics["return_on_capital_employed_TTM"],

                           has_dividend=dividends["has_dividend"],
                           forward_annual_dividend_rate=dividends["forward_annual_dividend_rate"],
                           dividend_yield=dividends["dividend_yield"],
                           dividend_date=dividends["dividend_date"],
                           ex_dividend=dividends["ex_dividend"],

                           total_current_assets=income_statements["total_current_assets"],
                           net_cash_provided_by_operating_activities=income_statements["net_cash_provided_by_operating_activities"],
                           net_cash_used_for_investing_activities=income_statements["net_cash_used_for_investing_activities"],
                           net_cash_used_provided_by_financing_activities=income_statements["net_cash_used_provided_by_financing_activities"],
                           free_cash_flow=income_statements["free_cash_flow"],
                           revenue=income_statements["revenue"],
                           ebitda=income_statements["ebitda"],
                           income_tax_expense=income_statements["income_tax_expense"],
                           net_income=income_statements["net_income"],
                           gross_profit=income_statements["gross_profit"],
                           total_non_current_assets=income_statements["total_non_current_assets"],
                           total_assets=income_statements["total_assets"],
                           total_current_liabilities=income_statements["total_current_liabilities"],
                           total_non_current_liabilities=income_statements["total_non_current_liabilities"],
                           total_liabilities=income_statements["total_liabilities"],
                           total_stockholders_equity=income_statements["total_stockholders_equity"],
                           total_liabilities_and_stockholders_equity=income_statements["total_liabilities_and_stockholders_equity"],

                           news=news
                           )


@fundamental_analysis_bp.route("/fundamental-analysis/export")
@login_required
def fundamental_analysis_export():
    return redirect(url_for("fundamental.fundamental_analysis"))