import pandas_datareader as web
import ValidTicker as validTicker
import convertStringToInteger as convert

from News import News
from yahoo_fin import stock_info as si

class Stock:
    """
    The stock class represents a stock of a company.
    :param ticker is the ticker symbol of the Stock
    :thrown RuntimeError if ticker is invalid
    """
    def __init__(self, ticker):
        # if the ticker is not valid an exception is thrown
        if not validTicker.valid_ticker(ticker):
            raise RuntimeError

        """
        Variables to store the stock information as provided below
        The are initialized to empty None values before the API calls to get and store the information
        
        Attributes:
            self.ticker: is the ticker symbol of a stock ex (MSFT,AAPL,etc)
            self._companyName: is the company name of a stock ex (Microsoft, Apple, etc)
            self._pricePerShare: is the current live price per 1 share of the stock
            self._marketCap: is the current Market capitalization which refers to the total dollar market value of a company's outstanding shares of stock
            self._volume is the current Volume of the stock which is the number of shares traded 
            self._threeMonthAvgVolume is the average volume of the stocks within the last 3 months
            self._EPS is the Earnings per share of the stock
            self._PeRatio is the price to earnings ratio of the stock
            self._Beta is the measurement of a stock's volatility in relation to the overall market
            self._Open is the opening price of the stock when the market opened on regular trading hours
            self._previous_close is the previous closing price of the stock
            self._bid is the highest price that someone is willing to pay for a share of the stock
            self._ask is the lowest price that someone is willing to pay for a share of the stock
            self._Fifty_Two_week_low  is the lowest price of the stock within a 52 week period
            self._Fifty_Two_week_high  is the highest price of the stock within a 52 week period
            self._EarningsDate is the estimated rage of dates that the companies earnings report will be released
            self._one_year_estimate is the estimated price per share of the stock after 1 year
            
            
         """

        self.ticker = ticker
        # declare all stock variables
        self._companyName = None
        self._pricePerShare = None
        self._marketCap = None
        self._volume = None
        self._threeMonthAvgVolume = None
        self._EPS = None
        self._PeRatio = None
        self._Beta = None
        self._Open = None
        self._previous_close = None
        self._bid = None
        self._ask = None
        self._EarningsDate = None
        self._Fifty_Two_week_low = None
        self._Fifty_Two_week_high = None
        self._one_year_estimate = None

        # dividend info of stock
        self._has_dividend = False
        self._dividendFrequency = None
        self._dividendAmount = None
        self._dividendDate = None
        self._exDividend = None

        # call function to automatically set all the stock info
        self.set_all_stock_info()

        # Automatically  gets news related to the stock
        self.news = News(self.ticker)


    def set_stock_stats(self):
        """
        Sets a summary of stats of the stock
        This uses pandas dataFrame objects to store stock info from yahoo finance stored
        """
        self._stock_stats = si.get_stats(self.ticker)

    def set_stock_quote(self):
        """
        Sets a quote of the stock of the stock
        This gets a quote from yahoo finance and the data is stored into a python dictionary
        """
        self._stock_quote = si.get_quote_table(self.ticker)

    def get_stock_quote(self):
        """
        Gets a quote of the stock of the stock
        :return a quote of the stock as a python dictionary
        """
        return self._stock_quote


    def get_stock_stats(self):
        """
        Gets a summary of stats of the stock
        :return a pandas dataFrame objects which has stock info from yahoo finance stored
        """
        return self._stock_stats

    def set_stock_company_name(self):
        """
        A function used to set the company name of the stock
        Calls the validTicker script to get the company name returned as a string
        :throws a ProcessLookupError exception if a company name of a ticker is not found
        """
        self._companyName = validTicker.get_ticker_company(self.ticker)

    def get_stock_company_name(self):
        """
        A function used to get the company name of the stock
        :return company name of stock as a a string
        """
        return self._companyName

    def get_stock_ticker(self):
        """
        A function used to get the ticker of the stock
        :return the ticker of the stock
        """
        return self.ticker

    def set_stock_price(self):
        """
        A function used to set the current stock price using yahoo finance
        The method does not include after hours or pre-market price
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin

        """
        self._pricePerShare = self.get_stock_quote()['Quote Price']  # gets current live price of the stock

    def get_stock_price(self):
        """
        A function used to get the current stock price using yahoo finance
        THe method does not include after hours or pre-market price
        :return price of the stock as an floating point number
        """
        return self._pricePerShare

    def set_market_cap(self):
        """
        Sets the current MarketCap of a stock
        For this method we are using a pandas web call to get the marketCap as an integer from yahoo finance
        """
        self._marketCap = web.get_quote_yahoo(self.ticker)['marketCap'][0]  # index 0 to ignore excess ticker output


    def get_market_cap(self):
        """
        Gets the current MarketCap of a stock
        :return marketCap of stock as an integer
        """
        return self._marketCap

    def set_volume(self):
        """
        Sets the current Volume of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._volume = self.get_stock_quote()['Volume']

    def get_volume(self):
        """
        Gets the current Volume of a stock
        :return volume of stock as an integer
        """
        return self._volume

    def set_three_month_volume(self):
        """
        Sets the three month average Volume of a stock
        This uses pandas data structure given by our api call to read the the data into the instance variable
        """

        self._threeMonthAvgVolume = self.get_stock_stats().at[16, "Value"]# index 16 of the pandas dataframe corresponds to the three_month_volume
        # since dataframe returns information as a string we must convert to integer
        self._threeMonthAvgVolume = convert.convertStringToInteger(self._threeMonthAvgVolume)

    def get_three_month_volume(self):
        """
        Gets the three month average Volume of a stock
        :return three month average Volume of a stock as a string
        """
        return self._threeMonthAvgVolume

    def set_eps(self):
        """
        Sets the 12 month EPS value of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """

        self._EPS = self.get_stock_quote()['EPS (TTM)']

    def get_eps(self):
        """
        Gets the 12 month EPS value of a stock
        :return EPS of a stock as a integer
        """
        return self._EPS

    def set_pe_ratio(self):
        """
        Sets the 12 month Pe-Ratio value of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """

        self._PeRatio = self.get_stock_quote()['PE Ratio (TTM)']

    def get_pe_ratio(self):
        """
        Gets the 12 month Pe-Ratio value of a stock
        :return Pe-Ratio of a stock as a float value
        """
        return self._PeRatio

    def set_beta(self):
        """
        Sets the 5Y Monthly Beta value of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """

        self._Beta = self.get_stock_quote()['Beta (5Y Monthly)']

    def get_beta(self):
        """
        Gets the 5Y Monthly Beta value of a stock
        :return Beta of a stock as a float value
        """
        return self._Beta

    def set_open(self):
        """
        Sets the open price of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._Open = self.get_stock_quote()['Open']

    def get_open(self):
        """
        Gets the open price of a stock
        :return open price of a stock as a float value
        """
        return self._Open

    def set_previous_close(self):
        """
        Sets the previous close price of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._previous_close = self.get_stock_quote()['Previous Close']

    def get_previous_close(self):
        """
        Gets  the previous close price of a stock
        :return the previous close price of a stock as a floating point number
        """
        return self._previous_close

    def set_bid(self):
        """
        Sets the current bid of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._bid = self.get_stock_quote()['Bid']

    def get_bid(self):
        """
        Gets current bid price of a stock
        :return the current bid of a stock as a string
        """
        return self._bid

    def set_ask(self):
        """
        Sets the current ask price of a stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._ask = self.get_stock_quote()['Ask']

    def get_ask(self):
        """
        Gets current ask price of a stock
        :return the current ask of a stock as a string
        """
        return self._ask

    def set_fifty_two_week_low(self):
        """
        Sets the 52 week low price of a stock
        For this method we are indexing from our pandas dataframe given from api call to yahoo_fin
        """
        self._Fifty_Two_week_low = self.get_stock_stats().at[13, "Value"]# index 13 of the pandas dataframe corresponds to the 52 week low

    def get_fifty_two_week_low(self):
        """
        Gets the 52 week low price of a stock
        :return the the 52 week low price of a stock as a floating point number
        """
        return self._Fifty_Two_week_low

    def set_fifty_two_week_high(self):
        """
        Sets the 52 week high price of a stock
        For this method we are indexing from our pandas dataframe given from api call to yahoo_fin
        """
        self._Fifty_Two_week_high = self.get_stock_stats().at[12, "Value"]  # index 12 of the pandas dataframe corresponds to the 52 week high

    def get_fifty_two_week_high(self):
        """
        Gets the 52 week high price of a stock
        :return the the 52 week low price of a stock as a floating point number
        """
        return self._Fifty_Two_week_high

    def set_earnings_date(self):
        """
        Sets the earnings dates of the stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._EarningsDate = self.get_stock_quote()['Earnings Date']

    def get_earnings_date(self):
        """
        Gets the earnings dates of the stock
        :return the earnings dates of the stock as a string
        """
        return self._EarningsDate

    def set_one_year_estimate(self):
        """
        Sets the one_year_estimate price of the stock
        For this method we are indexing from our python dictionary which is returned by our previous API call to yahoo-fin
        """
        self._one_year_estimate = self.get_stock_quote()['1y Target Est']

    def get_one_year_estimate(self):
        """
        Gets the  one_year_estimate price of the stock
        :return the one_year_estimate price of the stock as a float
        """
        return self._one_year_estimate


    def set_all_stock_info(self):
        """
        Call all appropriate setter methods to set the values of the attributes of the stock class
        """
        self.set_stock_stats()
        self.set_stock_quote()
        self.set_stock_company_name()
        self.set_stock_price()
        self.set_market_cap()
        self.set_volume()
        self.set_three_month_volume()
        self.set_eps()
        self.set_pe_ratio()
        self.set_beta()
        self.set_open()
        self.set_previous_close()
        self.set_bid()
        self.set_ask()
        self.set_fifty_two_week_low()
        self.set_fifty_two_week_high()
        self.set_earnings_date()
        self.set_one_year_estimate()




    def getNews(self):
        """
        Get a News class object relating to the stock
        The news object has two methods that can be used by the user such as
        get_news_as_list() which returns article objects within a python list
        news_tostring() which will return a nicely formatted string representation of all news articles

        :return a list of article objects relating to the stock
        """
        return self.news


s1 = Stock("aapl")

print(s1.get_stock_price())
print(s1.get_market_cap())
print(s1.get_stock_company_name())
print(s1.get_volume())
print(s1.get_three_month_volume())
print(s1.get_eps())
print(s1.get_pe_ratio())
print(s1.get_beta())
print(s1.get_open())
print(s1.get_previous_close())
print(s1.get_bid())
print(s1.get_ask())
print(s1.get_fifty_two_week_low())
print(s1.get_fifty_two_week_high())
print(s1.get_earnings_date())
print(s1.get_one_year_estimate())
# print(s1.stats())
# print(s1.getNews().news_tostring())

#
# print(si.get_holders("aapl"))
# print(si.get_analysts_info("aapl"))
