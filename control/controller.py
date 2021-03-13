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
