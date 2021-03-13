def get_fundamental_analysis(ticker, data_source):
    """
    returns the fundamental analysis as a dictionary
    """
    try:
        stock = Stock(ticker=ticker)
    except RuntimeError:
        return None

    fundamental = stock.get_fundamental()

    analysis = {"stock_details": {"open": stock.get_open(),
                                  "close": stock.get_previous_close(),
                                  "bid": stock.get_bid(),
                                  "ask": stock.get_ask(),
                                  "earnings_date": stock.get_earnings_date(),
                                  "twenty_four_hour_low": None,
                                  "twenty_four_hour_high": None,
                                  "fifty_two_week_low": None,
                                  "fifty_two_week_high": None,
                                  "year_estimate": stock.get_one_year_estimate()
                                  },
                "metrics": {"fair_value": fundamental.get_priceFairValueTTM(),
                            "market_price": None,
                            "volume": stock.get_volume(),
                            "market_cap": stock.get_market_cap(),
                            "extra": None,
                            "PE_ratio": stock.get_pe_ratio(),
                            "current_ratio": fundamental.get_currentRatioTTM(),
                            "debt_to_equity": fundamental.get_debtEquityRatioTTM(),
                            "price_to_book_ratio": fundamental.get_priceToBookRatioTTM(),
                            },
                "dividends": {"frequency": None,
                              "amount": None,
                              "dividend_yield": stock.get_dividend_yield(),
                              "dividend_date": stock.get_dividend_date(),
                              "ex_dividend": stock.get_ex_dividend(),
                              "ddm": None,
                              "dgm": None,
                              "blended_forward_PE": None,
                              "npv": None,
                              "extra": None,
                              },
                "financial_statements": {"current_assets": None,
                                         "long_term_assets": None,
                                         "total_assets": None,
                                         "current_liabilities": None,
                                         "long_term_liabilities": None,
                                         "total_liabilities": None,
                                         "shareholders_equity": None,
                                         "gross_revenue": None,
                                         "ebitda": None,
                                         "expenses": None,
                                         "net_income": None,
                                         "profit_margin": None,
                                         "net_operating_cash": None,
                                         "net_investing_cash": None,
                                         "net_financing_cash": None,
                                         "free_cash_flow": None
                                         },
                "news": stock.get_news().news_tostring()
                }

    return analysis
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

    analysis = {"stock_details": {
        # create a field called ticker
        # "ticker": stock.get_stock_ticker()

        # create a field called companyName
        # "company_name": stock.get_stock_company_name()

        # create field currentPricePerShare
        # "currentPricePerShare": stock.get_stock_price()

        "open": stock.get_open(),

        # change name of close field to "previous_close"
        "close": stock.get_previous_close(),

        "bid": stock.get_bid(),
        "ask": stock.get_ask(),
        "earnings_date": stock.get_earnings_date(),

        # replace the twenty four hour low and high with a field called daily range I couldn;t figure out how to get this data
        # daily_range: stock.get_daily_range()
        "twenty_four_hour_low": None,
        "twenty_four_hour_high": None,

        # replace fifty week low and fifty two week high  with a fifty week range field
        # fifty_two_week_range = Stock.get_fifty_two_week_range()
        "fifty_two_week_low": None,
        "fifty_two_week_high": None,

        "year_estimate": stock.get_one_year_estimate()
    },
        "metrics": {"fair_value": fundamental.get_priceFairValueTTM(),
                    "market_price": None,
                    "volume": stock.get_volume(),

                    # create field threeMonthAverageVolume
                    # "threeMonthAverageVolume": stock.get_three_month_volume()

                    "market_cap": stock.get_market_cap(),

                    # create field called EPS
                    # "EPS": stock.get_eps()

                    # create field called Beta
                    # "Beta": stock.get_beta()

                    # you can delete the extra field
                    "extra": None,

                    "PE_ratio": stock.get_pe_ratio(),
                    "current_ratio": fundamental.get_currentRatioTTM(),
                    "debt_to_equity": fundamental.get_debtEquityRatioTTM(),
                    "price_to_book_ratio": fundamental.get_priceToBookRatioTTM(),

                    # create fields for
                    # priceFairValueTTM: double      fundamental.get_priceFairValueTTM()
                    # returnOnEquityTTM: double       fundamental.get_returnOnEquityTTM()
                    # priceEarningsToGrowthRatioTTM: double     fundamental.priceEarningsToGrowthRatioTTM
                    # returnOnAssetsTTM: double        fundamental.returnOnAssetsTTM
                    # returnOnCapitalEmployedTTM: double      fundamental.returnOnCapitalEmployedTTM




                    },

        "dividends": {
                        # create field has_dividend
                        # "has_dividend": stock.has_dividend()

                        # do not call the methods below unless the stock has a dividend
                        # if the stock doesn't have a dividend set the dividends fields values below to  None

                      #create field forward_annual_dividend_rate:
                      #"forward_annual_dividend_rate": stock.get_forward_annual_dividend_rate()


                      "dividend_yield": stock.get_dividend_yield(),
                      "dividend_date": stock.get_dividend_date(),
                      "ex_dividend": stock.get_ex_dividend(),

                     # you can delete these fields since I do not have any methods to get this info
                      "frequency": None,
                      "amount": None,
                      "ddm": None,
                      "dgm": None,
                      "blended_forward_PE": None,
                      "npv": None,
                      "extra": None,
                      },
        "financial_statements": {
                                # rename to totalCurrentAssets
                                "current_assets": None,

                                # netCashProvidedByOperatingActivities: int         cash_flow.getNetCashProvidedByOperatingActivities()
                                # netCashUsedForInvestingActivites: int             cash_flow.getNetCashUsedForInvestingActivites()
                                # netCashUsedProvidedByFinancingActivities: int     cash_flow.getNetCashUsedProvidedByFinancingActivities()
                                # freeCashFlow: int                                 cash_flow.getFreeCashFlow()


                                # revenue: int             income_statement.getRevenue()
                                # ebitda: int              income_statement.getEbitda()
                                # incomeTaxExpense: int    income_statement.getIncomeTaxExpense()
                                # netIncome: int           income_statement.getNetIncome()
                                # grossProfit: int         income_statement.getGrossProfit()



                                # totalNonCurrentAssets: int    balance_sheet.get_totalCurrentAssets()
                                # totalAssets: int              balance_sheet.get_totalAssets()
                                # totalCurrentLiabilities: int  balance_sheet.get_totalCurrentLiabilities()
                                # totalNonCurrentLiabilities: int   balance_sheet.get_totalNonCurrentLiabilities()
                                # totalLiabilities: int             balance_sheet.get_totalLiabilities()
                                # totalStockholdersEquity: int      balance_sheet.get_totalStockholdersEquity()
                                # totalLiabilitiesAndStockholdersEquity: int    balance_sheet.get_totalLiabilitiesAndStockholdersEquity()


                                # remove these fields
                                 "long_term_assets": None,
                                 "total_assets": None,
                                 "current_liabilities": None,
                                 "long_term_liabilities": None,
                                 "total_liabilities": None,
                                 "shareholders_equity": None,
                                 "gross_revenue": None,
                                 "ebitda": None,
                                 "expenses": None,
                                 "net_income": None,
                                 "profit_margin": None,
                                 "net_operating_cash": None,
                                 "net_investing_cash": None,
                                 "net_financing_cash": None,
                                 "free_cash_flow": None
                                 },
        "news": stock.get_news().news_tostring()
    }

    return analysis
