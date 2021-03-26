
"""
    Test Script written by Bathiya Ranasinghe for the stock and news class
    Errors within the methods will be printed out to console
    The only other console output will be from the news class printing the news articles for a manual check by the tester
    A test complete messege will be printed at the end along with the time to execute creating the stock classes

    This script does not test any of the methods from the  Fundamental, Cashflow, Income, Statement, BalanceSheet classes
    Those classes were to be tested by Ramtin's test script

    Disclaimer: Do to varying market conditions there may be situations where the script reports an error on the values expected to bve returned by functions.
                it is the testers responsibility to manually check to see if expected values on the test script should be updated or not when an error is announced.
    """

import datetime

import Stock as Stock
import ray


def main():
    """
    This is a unit test for the Stock Class
    This tests all available getter methods to make sure they are returning the appropriate data types
    The Test also displays the execution time in seconds to store and get all attributes to create the stock class
    """
    # initialize ray
    ray.init(ignore_reinit_error=True)

    # set the number of errors in code to 0
    ErrorCount = 0

    # testing with a large cap stock that has a dividend
    ticker = "aapl"
    begin_time = datetime.datetime.now()
    s1 = Stock.Stock(ticker)
    execution_time_apple_stock = (
                datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time

    # make sure the getter method for stock price return the correct data type
    if type(s1.get_stock_price()) != float:
        print(
            "Error in returned data type of get_stock_price() method for " + ticker + " should return float but got " + type(
                s1.get_stock_price()))
        ErrorCount += 1

    # check if the returned price of the stock is within a valid range. (aapl is usually within the 100 to 150 dollar range)
    if not 100 < s1.get_stock_price() < 150:
        print("Error in returned value of get_stock_price() method for " + ticker)
        ErrorCount += 1

    # make sure the getter method for stock market cap return the correct data type
    if type(s1.get_market_cap()) != str:
        print(
            "Error in returned data type of get_market_cap() method for " + ticker + " should return str but got " + type(
                s1.get_market_cap()))
        ErrorCount += 1

    # make sure the getter method for stock company name returns the correct data type
    if type(s1.get_stock_company_name()) != str:
        print(
            "Error in returned data type of get_stock_company_name() method for " + ticker + " should return str but got " + type(
                s1.get_stock_company_name()))
        ErrorCount += 1

    # make sure the getter method for stock volume returns the correct data type
    if type(s1.get_volume()) != float:
        print(
            "Error in returned data type of get_volume() method for " + ticker + " should return float but got " + type(
                s1.get_volume()))
        ErrorCount += 1

    # check if the returned volume of the stock is within a valid range. (aapl is usually within the 50,105,050 to 350,752,167 volume range)
    if not 50105050 < s1.get_volume() < 350752167:
        print("Error in returned value of get_volume() method for " + ticker)
        ErrorCount += 1

    # make sure the get_three_month_volume() name returns the correct data type
    if type(s1.get_three_month_volume()) != str:
        print(
            "Error in returned data type of get_three_month_volume() method for " + ticker + " should return str but got " + type(
                s1.get_three_month_volume()))
        ErrorCount += 1

    # make sure the get_eps() returns the correct data type
    if type(s1.get_eps()) != float:
        print("Error in returned data type of get_eps() method for " + ticker + " should return float but got " + type(
            s1.get_eps()))
        ErrorCount += 1

    # check if the returned eps of the stock is within a valid range. (aapl is usually within the 3 to 4 eps range)
    if not 3 < s1.get_eps() < 4:
        print("Error in returned value of get_eps() method for " + ticker)
        ErrorCount += 1

    # make sure the get_pe_ratio() returns the correct data type
    if type(s1.get_pe_ratio()) != float:
        print(
            "Error in returned data type of get_pe_ratio() method for " + ticker + " should return float but got " + type(
                s1.get_pe_ratio()))
        ErrorCount += 1

    # check if the returned pe_ratio of the stock is within a valid range. (nndm is usually within the 20 to 40 pe range)
    if not 20 < s1.get_pe_ratio() < 40:
        print("Error in returned value of get_pe_ratio() method for " + ticker)
        ErrorCount += 1

    # make sure the get_beta() returns the correct data type
    if type(s1.get_beta()) != float:
        print(
            "Error in returned data type of get_beta() method for " + ticker + " should return float but got " + type(
                s1.get_beta()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (aapl is usually within the 1 to 2 beta range)
    if not 1 < s1.get_beta() < 2:
        print("Error in returned value of get_beta() method for " + ticker)
        ErrorCount += 1

    # make sure the get_open() returns the correct data type
    if type(s1.get_open()) != float:
        print(
            "Error in returned data type of get_open() method for " + ticker + " should return float but got " + type(
                s1.get_open()))
        ErrorCount += 1

    # check if the returned get_open() of the stock is within a valid range. (nndm is usually within the 100 to 150 dollar open range)
    if not 100 < s1.get_open() < 150:
        print("Error in returned value of get_open() method for " + ticker)
        ErrorCount += 1

    # make sure the get_previous_close() returns the correct data type
    if type(s1.get_previous_close()) != float:
        print(
            "Error in returned data type of get_previous_close() method for " + ticker + " should return float but got " + type(
                s1.get_previous_close()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (aapl is usually within the 5 to 30 dollar range)
    if not 100 < s1.get_previous_close() < 150:
        print("Error in returned value of get_previous_close() method for " + ticker)
        ErrorCount += 1

    # make sure the get_bid() returns the correct data type
    if type(s1.get_bid()) != str:
        print(
            "Error in returned data type of get_bid() method for " + ticker + " should return str but got " + type(
                s1.get_bid()))
        ErrorCount += 1

    # make sure the get_ask() returns the correct data type
    if type(s1.get_ask()) != str:
        print(
            "Error in returned data type of get_ask() method for" + ticker + " should return str but got " + type(
                s1.get_ask()))
        ErrorCount += 1

    # make sure the get_fifty_two_week_range() returns the correct data type
    if type(s1.get_fifty_two_week_range()) != str:
        print(
            "Error in returned data type of get_fifty_two_week_range() method for " + ticker + " should return str but got " + type(
                s1.get_fifty_two_week_range()))
        ErrorCount += 1

    # make sure the get_daily_range() returns the correct data type
    if type(s1.get_daily_range()) != str:
        print(
            "Error in returned data type of get_daily_range() method for " + ticker + " should return str but got " + type(
                s1.get_daily_range()))
        ErrorCount += 1

    # make sure the get_earnings_date() returns the correct data type
    if type(s1.get_earnings_date()) != str:
        print(
            "Error in returned data type of get_earnings_date() method for " + ticker + " should return str but got " + type(
                s1.get_earnings_date()))
        ErrorCount += 1

    # make sure the get_one_year_estimate() returns the correct data type
    if type(s1.get_one_year_estimate()) != float:
        print(
            "Error in returned data type of get_one_year_estimate() method for " + ticker + " should return float but got " + type(
                s1.get_one_year_estimate()))
        ErrorCount += 1

    # check if the returned get_one_year_estimate() of the stock is within a valid range. (aapl should be within the 100 to 200 dollar range in 1 year)
    if not 100 < s1.get_one_year_estimate() < 200:
        print("Error in returned value of get_one_year_estimate() method for " + ticker)
        ErrorCount += 1

    # check if aapl has dividend which it should
    if not s1.has_dividend():
        print("Error in returned value of has_dividend() method " + ticker + "should have a dividend")

    try:
        # try to get dividend info. the methods throw exception when trying to get dividend from stock that has no dividend
        forward_annual_dividend_rate = s1.get_forward_annual_dividend_rate()
        dividend_yield = s1.get_dividend_yield()
        dividend_date = s1.get_dividend_date()
        ex_dividend = s1.get_ex_dividend()

        # make sure the get_forward_annual_dividend_rate() returns the correct data type
        if type(forward_annual_dividend_rate) != str:
            print(
                "Error in returned data type of get_forward_annual_dividend_rate() method for " + ticker + " should return str  but got " + type(
                    forward_annual_dividend_rate))
            ErrorCount += 1

        # make sure the get_dividend_yield() returns the correct data type
        if type(dividend_yield) != str:
            print(
                "Error in returned data type of get_dividend_yield() method for " + ticker + " should return str but got " + type(
                    s1.get_dividend_yield()))
            ErrorCount += 1

        # make sure the get_dividend_yield() returns the correct data type
        if type(dividend_date) != str:
            print(
                "Error in returned data type of get_dividend_date() method for " + ticker + " should return str but got " + type(
                    s1.get_dividend_date()))
            ErrorCount += 1

        # make sure the get_ex_dividend() returns the correct data type
        if type(ex_dividend) != str:
            print(
                "Error in returned data type of get_ex_dividend() method for " + ticker + " should return str but got " + type(
                    s1.get_ex_dividend()))
            ErrorCount += 1

    except RuntimeError as err:
        # exception thrown when it should not have
        print("Error in dividend methods for " + ticker + ", throwing exception when they should not have ")

    # manually test the news class to see if articles out put correctly
    print(s1.get_news().news_tostring())


                                            # New stock to test
################################################################################################################################################
################################################################################################################################################



    # testing with a smaller cap stock
    print("\n\n\n\n")
    ticker = "nndm"
    begin_time = datetime.datetime.now()
    s2 = Stock.Stock(ticker)
    execution_time_nndm_stock = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time

    # make sure the getter method for stock price return the correct data type
    if type(s2.get_stock_price()) != float:
        print(
            "Error in returned data type of get_stock_price() method for " + ticker + " should return float but got " + type(
                s2.get_stock_price()))
        ErrorCount += 1

    # check if the returned price of the stock is within a valid range. (nndm is usually within the 5 to 30 dollar range)
    if not 5 < s2.get_stock_price() < 30:
        print("Error in returned value of get_stock_price() method for " + ticker)
        ErrorCount += 1

    # make sure the getter method for stock market cap return the correct data type
    if type(s2.get_market_cap()) != str:
        print(
            "Error in returned data type of get_market_cap() method for " + ticker + " should return str but got " + type(
                s2.get_market_cap()))
        ErrorCount += 1

    # make sure the getter method for stock company name returns the correct data type
    if type(s2.get_stock_company_name()) != str:
        print(
            "Error in returned data type of get_stock_company_name() method for " + ticker + " should return str but got " + type(
                s2.get_stock_company_name()))
        ErrorCount += 1

    # make sure the getter method for stock volume returns the correct data type
    if type(s2.get_volume()) != float:
        print(
            "Error in returned data type of get_volume() method for " + ticker + " should return float but got " + type(
                s2.get_volume()))
        ErrorCount += 1

    # check if the returned volume of the stock is within a valid range. (nndm is usually within the 10,982,626 to 30,982,626 volume range)
    if not 10982626 < s2.get_volume() < 30982626:
        print("Error in returned value of get_volume() method for " + ticker)
        ErrorCount += 1

    # make sure the get_three_month_volume() name returns the correct data type
    if type(s2.get_three_month_volume()) != str:
        print(
            "Error in returned data type of get_three_month_volume() method for " + ticker + " should return str but got " + type(
                s2.get_three_month_volume()))
        ErrorCount += 1

    # make sure the get_eps() returns the correct data type
    if type(s2.get_eps()) != float:
        print("Error in returned data type of get_eps() method for " + ticker + " should return float but got " + type(
            s2.get_eps()))
        ErrorCount += 1

    # check if the returned eps of the stock is within a valid range. (nndm is usually within the -3 to 4 eps range)
    if not -3 < s2.get_eps() < 4:
        print("Error in returned value of get_eps() method for " + ticker)
        ErrorCount += 1

    # make sure the get_pe_ratio() returns the correct data type
    if type(s2.get_pe_ratio()) != float:
        print(
            "Error in returned data type of get_pe_ratio() method for " + ticker + " should return float but got " + type(
                s2.get_pe_ratio()))
        ErrorCount += 1

    # make sure the get_beta() returns the correct data type
    if type(s2.get_beta()) != float:
        print(
            "Error in returned data type of get_beta() method for " + ticker + " should return float but got " + type(
                s2.get_beta()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (nndm is usually within the 1 to 3 beta range)
    if not 1 < s2.get_beta() < 3:
        print("Error in returned value of get_beta() method for " + ticker)
        ErrorCount += 1

    # make sure the get_open() returns the correct data type
    if type(s2.get_open()) != float:
        print(
            "Error in returned data type of get_open() method for " + ticker + " should return float but got " + type(
                s2.get_open()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (nndm is usually within the 5 to 30 dollar open range)
    if not 5 < s2.get_open() < 30:
        print("Error in returned value of get_open() method for " + ticker)
        ErrorCount += 1

    # make sure the get_previous_close() returns the correct data type
    if type(s2.get_previous_close()) != float:
        print(
            "Error in returned data type of get_previous_close() method for " + ticker + " should return float but got " + type(
                s2.get_previous_close()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (aapl is usually within the 5 to 30 dollar range)
    if not 5 < s2.get_previous_close() < 30:
        print("Error in returned value of get_previous_close() method for " + ticker)
        ErrorCount += 1

    # make sure the get_bid() returns the correct data type
    if type(s2.get_bid()) != str:
        print(
            "Error in returned data type of get_bid() method for " + ticker + " should return str but got " + type(
                s2.get_bid()))
        ErrorCount += 1

    # make sure the get_ask() returns the correct data type
    if type(s2.get_ask()) != str:
        print(
            "Error in returned data type of get_ask() method for" + ticker + " should return str but got " + type(
                s2.get_ask()))
        ErrorCount += 1

    # make sure the get_fifty_two_week_range() returns the correct data type
    if type(s2.get_fifty_two_week_range()) != str:
        print(
            "Error in returned data type of get_fifty_two_week_range() method for " + ticker + " should return str but got " + type(
                s2.get_fifty_two_week_range()))
        ErrorCount += 1

    # make sure the get_daily_range() returns the correct data type
    if type(s2.get_daily_range()) != str:
        print(
            "Error in returned data type of get_daily_range() method for " + ticker + " should return str but got " + type(
                s2.get_daily_range()))
        ErrorCount += 1

    # make sure the get_earnings_date() returns the correct data type
    if type(s2.get_earnings_date()) != str:
        print(
            "Error in returned data type of get_earnings_date() method for " + ticker + " should return str but got " + type(
                s2.get_earnings_date()))
        ErrorCount += 1

    # make sure the get_one_year_estimate() returns the correct data type
    if type(s2.get_one_year_estimate()) != float:
        print(
            "Error in returned data type of get_one_year_estimate() method for " + ticker + " should return float but got " + type(
                s2.get_one_year_estimate()))
        ErrorCount += 1

    # check if the returned get_one_year_estimate() of the stock is within a valid range. (nndm should be within the 5 to 30 dollar range in 1 year)
    if not 5 < s2.get_one_year_estimate() < 30:
        print("Error in returned value of get_one_year_estimate() method for " + ticker)
        ErrorCount += 1

    # check if nndm has dividend which it should not
    if s2.has_dividend():
        print("Error in returned value of has_dividend() method " + ticker + "should not have a dividend")

    try:
        # try to get dividend info. the methods throw exception when trying to get dividend from stock that has no dividend
        forward_annual_dividend_rate = s2.get_forward_annual_dividend_rate()
        dividend_yield = s2.get_dividend_yield()
        dividend_date = s2.get_dividend_date()
        ex_dividend = s2.get_ex_dividend()

        print("Error exception not thrown when it should have")

    except RuntimeError as err:
        # exception should be thrown since nndm has no divided
        pass

    # manually test the news class to see if articles out put correctly
    print(s2.get_news().news_tostring())



                                                # New stock to test
################################################################################################################################################
################################################################################################################################################

    # testing with a spac stock
    print("\n\n\n\n")
    ticker = "stpk"
    begin_time = datetime.datetime.now()
    s3 = Stock.Stock(ticker)
    execution_time_stpk_stock = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time

    # make sure the getter method for stock price return the correct data type
    if type(s3.get_stock_price()) != float:
        print(
            "Error in returned data type of get_stock_price() method for " + ticker + " should return float but got " + type(
                s3.get_stock_price()))
        ErrorCount += 1

    # check if the returned price of the stock is within a valid range. (stpk is usually within the 15 to 50 dollar range)
    if not 15 < s3.get_stock_price() < 50:
        print("Error in returned value of get_stock_price() method for " + ticker)
        ErrorCount += 1

    # make sure the getter method for stock market cap return the correct data type
    if type(s3.get_market_cap()) != str:
        print(
            "Error in returned data type of get_market_cap() method for " + ticker + " should return str but got " + type(
                s3.get_market_cap()))
        ErrorCount += 1

    # make sure the getter method for stock company name returns the correct data type
    if type(s3.get_stock_company_name()) != str:
        print(
            "Error in returned data type of get_stock_company_name() method for " + ticker + " should return str but got " + type(
                s3.get_stock_company_name()))
        ErrorCount += 1

    # make sure the getter method for stock volume returns the correct data type
    if type(s3.get_volume()) != float:
        print(
            "Error in returned data type of get_volume() method for " + ticker + " should return float but got " + type(
                s3.get_volume()))
        ErrorCount += 1

    # check if the returned volume of the stock is within a valid range. (stpk is usually within the 100000 to 4299056 volume range)
    if not 100000 < s3.get_volume() < 4299056:
        print("Error in returned value of get_volume() method for " + ticker)
        ErrorCount += 1

    # make sure the get_three_month_volume() name returns the correct data type
    if type(s3.get_three_month_volume()) != str:
        print(
            "Error in returned data type of get_three_month_volume() method for " + ticker + " should return str but got " + type(
                s3.get_three_month_volume()))
        ErrorCount += 1

    # make sure the get_eps() returns the correct data type
    if type(s3.get_eps()) != float:
        print("Error in returned data type of get_eps() method for " + ticker + " should return float but got " + type(
            s3.get_eps()))
        ErrorCount += 1

    # make sure the get_pe_ratio() returns the correct data type
    if type(s3.get_pe_ratio()) != float:
        print(
            "Error in returned data type of get_pe_ratio() method for " + ticker + " should return float but got " + type(
                s3.get_pe_ratio()))
        ErrorCount += 1

    # make sure the get_beta() returns the correct data type
    if type(s3.get_beta()) != float:
        print(
            "Error in returned data type of get_beta() method for " + ticker + " should return float but got " + type(
                s3.get_beta()))
        ErrorCount += 1

    # make sure the get_open() returns the correct data type
    if type(s3.get_open()) != float:
        print(
            "Error in returned data type of get_open() method for " + ticker + " should return float but got " + type(
                s3.get_open()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (stpk is usually within the 15 to 50 dollar open range)
    if not 15 < s3.get_open() < 50:
        print("Error in returned value of get_open() method for " + ticker)
        ErrorCount += 1

    # make sure the get_previous_close() returns the correct data type
    if type(s3.get_previous_close()) != float:
        print(
            "Error in returned data type of get_previous_close() method for " + ticker + " should return float but got " + type(
                s3.get_previous_close()))
        ErrorCount += 1

    # check if the returned get_beta() of the stock is within a valid range. (stpk is usually within the 15 to 30 dollar range)
    if not 15 < s3.get_previous_close() < 50:
        print("Error in returned value of get_previous_close() method for " + ticker)
        ErrorCount += 1

    # make sure the get_bid() returns the correct data type
    if type(s3.get_bid()) != str:
        print(
            "Error in returned data type of get_bid() method for " + ticker + " should return str but got " + type(
                s3.get_bid()))
        ErrorCount += 1

    # make sure the get_ask() returns the correct data type
    if type(s3.get_ask()) != str:
        print(
            "Error in returned data type of get_ask() method for" + ticker + " should return str but got " + type(
                s3.get_ask()))
        ErrorCount += 1

    # make sure the get_fifty_two_week_range() returns the correct data type
    if type(s3.get_fifty_two_week_range()) != str:
        print(
            "Error in returned data type of get_fifty_two_week_range() method for " + ticker + " should return str but got " + type(
                s3.get_fifty_two_week_range()))
        ErrorCount += 1

    # make sure the get_daily_range() returns the correct data type
    if type(s3.get_daily_range()) != str:
        print(
            "Error in returned data type of get_daily_range() method for " + ticker + " should return str but got " + type(
                s3.get_daily_range()))
        ErrorCount += 1

    # make sure the get_one_year_estimate() returns the correct data type
    if type(s3.get_one_year_estimate()) != float:
        print(
            "Error in returned data type of get_one_year_estimate() method for " + ticker + " should return float but got " + type(
                s3.get_one_year_estimate()))
        ErrorCount += 1

    # check if nndm has dividend which it should not
    if s3.has_dividend():
        print("Error in returned value of has_dividend() method " + ticker + "should not have a dividend")

    try:
        # try to get dividend info. the methods throw exception when trying to get dividend from stock that has no dividend
        forward_annual_dividend_rate = s3.get_forward_annual_dividend_rate()
        dividend_yield = s3.get_dividend_yield()
        dividend_date = s3.get_dividend_date()
        ex_dividend = s3.get_ex_dividend()

        print("Error exception not thrown when it should have")

    except RuntimeError as err:
        # exception should be thrown since nndm has no divided
        pass

    # manually test the news class to see if articles out put correctly
    print(s3.get_news().news_tostring())

                                        # New stock to test
################################################################################################################################################
################################################################################################################################################

    # testing with creating a stock using an invalid ticker
    try:
        print("\n\n\n\n")
        ticker = "blahblah"
        s3 = Stock.Stock(ticker)

        # using an invalid ticker and still managed to create stock so display warning
        print("Error " + ticker + " should not be a valid ticker but a stock was still created")

    except RuntimeError as err:
        # we should expect a RuntimeError when an invalid ticker is used
        pass


    print("\n**** Testing Complete with " + str(ErrorCount) + " errors ****")
    print("Execution Time for " + s1.get_stock_ticker() + " Was: " + str(execution_time_apple_stock) + " seconds")
    print("Execution Time for " + s2.get_stock_ticker() + " Was: " + str(execution_time_nndm_stock) + " seconds")
    print("Execution Time for " + s3.get_stock_ticker() + " Was: " + str(execution_time_stpk_stock) + " seconds")


if __name__ == "__main__":
    main()



#ignore this info below

# print(s1.get_stock_price())
    # print(s1.get_market_cap())
    # print(s1.get_stock_company_name())
    # print(s1.get_volume())
    # print(s1.get_three_month_volume())
    # print(s1.get_eps())
    # print(s1.get_pe_ratio())
    # print(s1.get_beta())
    # print(s1.get_open())
    # print(s1.get_previous_close())
    # print(s1.get_bid())
    # print(s1.get_ask())
    # print(s1.get_fifty_two_week_range())
    # print(s1.get_daily_range())
    # print(s1.get_earnings_date())
    # print(s1.get_one_year_estimate())
    # print(s1.has_dividend())
    # print(s1.get_forward_annual_dividend_rate())
    # print(s1.get_dividend_yield())
    # print(s1.get_dividend_date())
    # print(s1.get_ex_dividend())