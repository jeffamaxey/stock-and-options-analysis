"""
Authors: Sahngwoo Kim, Adam Bouthillette, Dan Richmond-Martina
"""

from model.Option import Option
from model.OptionValuation import Valuation
from model.Stock import Stock
from model.exportToCSV import exportToCSV


def get_expiration_date_list():
    return ['2021-04-01', '2021-04-09', '2021-04-16', '2021-04-23', '2021-04-30',
            '2021-05-21', '2021-06-18', '2021-07-16', '2021-09-17', '2021-12-17',
            '2022-01-21', '2022-03-18', '2022-06-17', '2022-09-16', '2023-01-20', '2023-03-17']


def get_option_type_list():
    return ['Call', 'Put']


def get_option_style_list():
    return ['American', 'European']


def get_data_source_list():
    return ['Yahoo', 'Other']


def get_itm_atm_otm_list():
    return ['itm+1', 'itm', 'atm', 'otm', 'otm+1']


def get_quantitative_analysis(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm):
    """
    returns the quantitative analysis 'outputs' as a dictionary
    """
    from model.OptionData import get_finalDict
    # Call Option Class
    try:
        option = Option(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm)
    except RuntimeError:  # This exception is thrown when the option is invalid
        return None

    riskFreeRate = option.get_riskFreeRate()
    currentUnderlyingPrice = round(option.get_currentPriceOfTheUnderlyingAsset(), 2)
    finalDict = get_finalDict(tickerSymbol, option_type, itm_atm_otm, expiration_date)
    timeToExpiration = finalDict['Time-to-expiration']
    volatility = finalDict['Sigma']
    strike = finalDict['Strike']
    # Call Valuation Class
    try:
        valuation = Valuation(1, tickerSymbol, riskFreeRate, currentUnderlyingPrice, strike, timeToExpiration, volatility, option_type, 1)
    except RuntimeError:  # This exception is thrown when the valuation is invalid
        return None

    chosenExpiration = expiration_date
    strike = round(finalDict["Strike"], 2)
    time_to_expiration = round(finalDict["Time-to-expiration"], 5)
    sigma = round(finalDict["Sigma"], 5)

    analysis = {
        "variables": {"risk_free_rate_r": round(riskFreeRate, 2),
                      "underlying_s": currentUnderlyingPrice,
                      "chosen_expiration": chosenExpiration,
                      "strike_x": strike,
                      "time_to_maturity_T": time_to_expiration,
                      "return_volatility": sigma,
                      "intrinsic_value": round(valuation.intrinsicValue(), 2),
                      "speculative_premium": round(valuation.speculativePremium(), 2)},
        "valuations": {"black_scholes": round(valuation.blackScholes(), 2),
                       "binomial": round(valuation.binomialModel(), 2),
                       "average_price": round(valuation.monteCarloSimulation(), 2),
                       "market_price": strike,
                       "implied_volatility": sigma},  #valuation.impliedVolatility()},
        "the_greeks": {"delta": round(valuation.delta(), 5),
                       "gamma": round(valuation.gamma(), 5),
                       "theta": round(valuation.theta(), 5),
                       "vega": round(valuation.vega(), 5),
                       "rho": round(valuation.rho(), 5),
                       "charm": round(valuation.charm(), 5)}, }

    return analysis


def get_fundamental_analysis(ticker, data_source):
    """
    returns the fundamental analysis as a dictionary
    """
    try:
        stock = Stock(ticker=ticker)
    except RuntimeError:  # This exception is thrown when the ticker is invalid
        return None

    # export the result as a csv file
    exporter = exportToCSV(stock)
    exporter.exportFundamental()

    fundamental = stock.get_fundamental()
    balance_sheet = stock.get_balance_sheet()
    income_statement = stock.get_income_statement()
    cash_flow = stock.get_cash_flow()

    # Values to be shown to the page when the stock doesn't have dividend
    forward_annual_dividend_rate = "( - )"
    dividend_yield = "( - )"
    dividend_date = "( - )"
    ex_dividend = "( - )"

    if stock.has_dividend():
        forward_annual_dividend_rate = stock.get_forward_annual_dividend_rate()
        dividend_yield = stock.get_dividend_yield()
        dividend_date = stock.get_dividend_date()
        ex_dividend = stock.get_ex_dividend()

    analysis = {"stock_details": {
        "ticker": stock.get_stock_ticker(),
        "company_name": stock.get_stock_company_name(),
        "current_price_per_share": stock.get_stock_price(),
        "open": stock.get_open(),
        "previous_close": stock.get_previous_close(),
        "bid": stock.get_bid(),
        "ask": stock.get_ask(),
        "earnings_date": stock.get_earnings_date(),
        "daily_range": stock.get_daily_range(),
        "fifty_two_week_range": stock.get_fifty_two_week_range(),
        "year_estimate": stock.get_one_year_estimate(),
    },
        "metrics": {"fair_value": fundamental.get_priceFairValueTTM(),
                    "volume": stock.get_volume(),
                    "three_month_average_volume": stock.get_three_month_volume(),
                    "market_cap": stock.get_market_cap(),
                    "EPS": stock.get_eps(),
                    "Beta": stock.get_beta(),
                    "PE_ratio": stock.get_pe_ratio(),
                    "current_ratio": fundamental.get_currentRatioTTM(),
                    "debt_to_equity": fundamental.get_debtEquityRatioTTM(),
                    "price_to_book_ratio": fundamental.get_priceToBookRatioTTM(),
                    "price_fair_value_TTM": fundamental.get_priceFairValueTTM(),
                    "return_on_equity_TTM": fundamental.get_returnOnEquityTTM(),
                    "price_earnings_to_growth_ratio_TTM": fundamental.get_priceEarningsToGrowthRatioTTM(),
                    "return_on_assets_TTM": fundamental.get_returnOnAssetsTTM(),
                    "return_on_capital_employed_TTM": fundamental.get_returnOnCapitalEmployedTTM()
                    },

        "dividends": {
            "has_dividend": stock.has_dividend(),
            "forward_annual_dividend_rate": forward_annual_dividend_rate,
            "dividend_yield": dividend_yield,
            "dividend_date": dividend_date,
            "ex_dividend": ex_dividend,
        },
        "income_statements": {
            "total_current_assets": balance_sheet.get_totalCurrentAssets(),

            "net_cash_provided_by_operating_activities": cash_flow.getNetCashProvidedByOperatingActivities(),
            "net_cash_used_for_investing_activities": cash_flow.getNetCashUsedForInvestingActivites(),
            "net_cash_used_provided_by_financing_activities": cash_flow.getNetCashUsedProvidedByFinancingActivities(),
            "free_cash_flow": cash_flow.getFreeCashFlow(),
            "revenue": income_statement.getRevenue(),
            "ebitda": income_statement.getEbitda(),
            "income_tax_expense": income_statement.getIncomeTaxExpense(),
            "net_income": income_statement.getNetIncome(),
            "gross_profit": income_statement.getGrossProfit(),

            "total_non_current_assets": balance_sheet.get_totalNonCurrentAssets(),
            "total_assets": balance_sheet.get_totalAssets(),
            "total_current_liabilities": balance_sheet.get_totalCurrentLiabilities(),
            "total_non_current_liabilities": balance_sheet.get_totalNonCurrentLiabilities(),
            "total_liabilities": balance_sheet.get_totalLiabilities(),
            "total_stockholders_equity": balance_sheet.get_totalStockholdersEquity(),
            "total_liabilities_and_stockholders_equity": balance_sheet.get_totalLiabilitiesAndStockholdersEquity()
        },

        "news": stock.get_news().news_tostring()
    }

    return analysis


def get_technical_analysis(ticker, data_source):
    """
    returns the technical analysis as a dictionary
    """
    try:
        stock = Stock(ticker=ticker)
    except RuntimeError:  # This exception is thrown when the ticker is invalid
        return None

    # export the result as a csv file
    exporter = exportToCSV(stock)
    exporter.export_technical()

    technical = stock.get_technical()

    analysis = {"tech_details": {
        "ticker": stock.get_stock_ticker(),
        "exchange": technical.get_exchange(),
        "RSI": technical.get_rsi(),
        "MACD": technical.get_macd(),
        "MRI": technical.get_momentum_breakout_bands(),
        "MOVING AVGS (30, 10)": technical.get_simple_moving_average_range_30_10(),
        "FIBONACCI TARGETS": technical.get_pivot_fib()
    },
        "summary": technical.to_string_summary()
    }

    return analysis
