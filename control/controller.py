from model.Stock import Stock


def get_fundamental_analysis(ticker, data_source):
    """
    returns the fundamental analysis as a dictionary
    """
    try:
        stock = Stock(ticker=ticker)
    except RuntimeError:
        return None

    fundamental = stock.get_fundamental()

    # create these 3 classes which are needed
    balance_sheet = stock.get_balance_sheet()
    income_statement = stock.get_income_statement()
    cash_flow = stock.get_cash_flow()

    # Values to be shown to the page when dividend doesn't exist
    forward_annual_dividend_rate = "-"
    dividend_yield = "-"
    dividend_date = "-"
    ex_dividend = "-"

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
                    "market_price": "-",
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
                    "price_earnings_to_growth_ratio_TTM": fundamental.priceEarningsToGrowthRatioTTM(),
                    "return_on_assets_TTM": fundamental.returnOnAssetsTTM(),
                    "return_on_capital_employed_TTM": fundamental.returnOnCapitalEmployedTTM()
                    },

        "dividends": {
            # create field has_dividend
            "has_dividend": stock.has_dividend(),

            # do not call the methods below unless the stock has a dividend
            # if the stock doesn't have a dividend set the dividends fields values below to  None

            # create field forward_annual_dividend_rate:
            "forward_annual_dividend_rate": forward_annual_dividend_rate,
            "dividend_yield": dividend_yield,
            "dividend_date": dividend_date,
            "ex_dividend": ex_dividend,

            # you can delete these fields since I do not have any methods to get this info
        },
        "income_statements": {
            # rename to totalCurrentAssets
            "total_current_assets": None,

            "net_cash_provided_by_operating_activities": cash_flow.getNetCashProvidedByOperatingActivities(),
            "net_cash_used_for_investing_activities": cash_flow.getNetCashUsedForInvestingActivites(),
            "net_cash_used_provided_by_financing_activities:": cash_flow.getNetCashUsedProvidedByFinancingActivities(),
            "free_cash_flow": cash_flow.getFreeCashFlow(),
            "revenue": income_statement.getRevenue(),
            "ebitda": income_statement.getEbitda(),
            "income_tax_expense": income_statement.getIncomeTaxExpense(),
            "net_income": income_statement.getNetIncome(),
            "gross_profit": income_statement.getGrossProfit(),

            "total_non_current_assets": balance_sheet.get_totalCurrentAssets(),
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
