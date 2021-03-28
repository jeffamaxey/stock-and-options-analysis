from model.Option import Option
from model.Valuation import Valuation
import yfinance as yf
from model.Stock import Stock
from model.exportToCSV import exportToCSV

########################################################################
#user clicks expiration than the ITMATMOTM shows (5 market prices) the 2 closest ITM and 2 closest OTM Strike Prices as well as ATM price
#Each expiration will be the ID, each expiration will have 2-ITM 1-ATM 2-OTM associated with it giving results for (strike, _T, & _sigma)
########################################################################
#strike impliedVolatility expirationDate    _T   optionType
# (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
# (ATM Call) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (OTM Call) if the Call strike price is > the the current price of the underlying asset
# (OTM Put) if the Put strike price is < the current price of the underlying asset
# (ATM Put) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option

##### IN Option.py
##### NEED TO UPDATE LINES IN OPTION.PY SO-> if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == self.chosenExpiration
##### NEED TO UPDATE LINES IN OPTION.PY So user selects the restraint of an expiration date


def get_expiration_date_list():
    return ['2021-04-01', '2021-04-09', '2021-04-16', '2021-04-23', '2021-04-30',
            '2021-05-21', '2021-06-18', '2021-07-16', '2021-09-17', '2021-12-17',
            '2022-01-21', '2022-03-18', '2022-06-17', '2022-09-16', '2023-01-20', '2023-03-17']


def get_option_type_list():
    return ['American', 'European']


def get_option_style_list():
    return ['Call', 'Put']


def get_data_source_list():
    return ['Yahoo', 'Other']


def get_itm_atm_otm_list():
    return ['itm+1', 'itm', 'atm', 'otm', 'otm+1']


def get_quantitative_analysis(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm):
    """
    returns the quantitative analysis 'outputs' as a dictionary
    """

    # Call Option Class
    option = Option(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm)

    riskFreeRate = option.get_riskFreeRate()
    currentUnderlyingPrice = option.get_currentPriceOfTheUnderlyingAsset()

    # USER SELECTS PUT or CALL, USER SELECTS EXPIRATION, USER SELECTS ITMATMOTM
    # Once user selects expiration it narrows down the potential fields to five different itm_atm_otm = ['itm+1', 'itm', 'atm', 'otm', 'otm+1']
    DictCalls = {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                 'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                 'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                 'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                 'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}}

    DictPuts = {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}}

    finalDict = {}
    if option_type == "Call":
        finalDict = DictCalls[itm_atm_otm]

    elif option_type == "Put":
        finalDict = DictPuts[itm_atm_otm]

    timeToExpiration = finalDict['Time-to-expiration']
    volatility = finalDict['Sigma']
    strike = finalDict['Strike']

    # Call Valuation Class
    valuation = Valuation(1, tickerSymbol, riskFreeRate, currentUnderlyingPrice, strike, timeToExpiration, volatility, option_type, 1)

    chosenExpiration = expiration_date
    strikeMatchChosenExpiration = finalDict["Strike"]
    TmatchChosen = finalDict["Time-to-expiration"]
    sigmaMatchedChosen = finalDict["Sigma"]

    analysis = {
        "variables": {"risk_free_rate_r": riskFreeRate,
                      "underlying_s": currentUnderlyingPrice,
                      "chosen_expiration": chosenExpiration,
                      "strike_x": strikeMatchChosenExpiration,
                      "time_to_maturity_T": TmatchChosen,
                      "return_volatility": sigmaMatchedChosen,
                      "intrinsic_value": valuation.intrinsicValue(),
                      "speculative_premium": valuation.speculativePremium()},
        "valuations": {"black_scholes": valuation.blackScholes(),
                       "binomial": valuation.binomialModel(),
                       "average_price": valuation.monteCarloSimulation(),
                       "market_price": strikeMatchChosenExpiration(),
                       "implied_volatility": valuation.impliedVolatility()},
        "the_greeks": {"delta": valuation.delta(),
                       "gamma": valuation.gamma(),
                       "theta": valuation.theta(),
                       "vega": valuation.vega(),
                       "rho": valuation.rho(),
                       "charm": valuation.charm()}, }
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
    exportToCSV(stock)

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

    technical = stock.get_technical()

    analysis = {"tech_details": {
        "ticker": stock.get_stock_ticker(),
        "RSI": technical.get_rsi(),
        "MACD": technical.get_macd(),
        "MRI": technical.get_momentum_breakout_bands(),
        "MOVING AVGS (30, 10)": technical.get_simple_moving_average_range_30_10(),
        "FIBONACCI TARGETS": technical.get_pivot_fib()
    },
        "summary": technical.to_string_summary()
    }

    return analysis

#print(get_quantitative_analysis('TSLA', '2021-07-16', 'American', 'Call', 'Yahoo', 'atm'))
