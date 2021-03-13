import datetime
from time import strftime

import Stock as Stock


def main():
    """
    This is a regression test for the Stock Class
    This tests all available getter methods to make sure they are returning the appropriate data types
    The Test also displays the execution time in seconds to store and get all attributes to create the stock class
    """

    # begin timer for execution time
    ticker = "ayro"
    begin_time = datetime.datetime.now()
    s1 = Stock.Stock(ticker)
    execution_time = (datetime.datetime.now() - begin_time).total_seconds()

    print(s1.get_stock_price())
    print(s1.get_market_cap())
    print(s1.get_stock_company_name())
    print(s1.get_volume())
    print(s1.get_three_month_volume())
    print(s1.get_three_month_volume())
    print(s1.get_eps())
    print(s1.get_pe_ratio())
    print(s1.get_beta())
    print(s1.get_open())
    print(s1.get_previous_close())
    print(s1.get_bid())
    print(s1.get_ask())
    print(s1.get_fifty_two_week_range())
    print(s1.get_daily_range())
    print(s1.get_earnings_date())
    print(s1.get_one_year_estimate())
    print(s1.has_dividend())
    print(s1.get_forward_annual_dividend_rate())
    #print(s1.get_dividend_yield())
    #print(s1.get_dividend_date())
   # print(s1.get_ex_dividend())
    print(s1.get_news().news_tostring())
    print(s1.get_fundamental().get_priceFairValueTTM())
    print(s1.get_balance_sheet().get_totalCurrentAssets())
    print(s1.get_income_statement().getRevenue())
    print(s1.get_cash_flow().getNetCashUsedForInvestingActivites())

    print("Testing Complete**")

    print("Execution Time Was: " + str(execution_time))


main()
