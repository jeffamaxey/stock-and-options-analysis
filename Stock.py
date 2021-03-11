import pandas_datareader as web
import ValidTicker as validTicker
import yfinance as yf
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

        # stock information
        self.ticker = ticker
        self._companyName = None
        self._pricePerShare = None
        self._marketCap = None
        self._volume = None
        self._threeMonthAvgVolume = None
        self._EPS = None
        self._PeRatio = None
        self._Beta = None
        self._Open = None
        self._Close = None
        self._Bid = None
        self._Ask = None
        self._Low = None
        self._High = None
        self._EarningsDate = None
        self._Fifty_Two_week_low = None
        self._Fifty_Two_week_high = None
        self._one_year_estimate = None
        self._stock_stats = None

        # call function to automatically set all the stock info
        self.set_all_stock_info()

        # gets news related to the stock
        self.news = News(self.ticker)

        # dividend info
        self._has_dividend = False
        self._dividendFrequency = None
        self._dividendAmount = None
        self._dividendDate = None
        self._exDividend = None

    def set_stock_stats(self):
        """
        Sets a summary of stats of the stock
        This uses pandas dataFrame objects to store stock info from yahoo finance stored
        """
        self._stock_stats = si.get_stats(self.ticker)

    def get_stock_stats(self):
        """
        Gets a summary of stats of the stock
        :return a pandas dataFrame objects which has stock info from yahoo finance stored
        """

        return self._stock_stats

    def set_stock_company_name(self):
        """
        A function used to set the company name of the stock
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
        THe method does not include after hours or pre-market price
        """
        self._pricePerShare = si.get_live_price(self.ticker)  # gets current live price of the stock

    def get_stock_price(self):
        """
        A function used to get the current stock price using yahoo finance
        THe methoed does not include after hours or pre-market price
        :return price of the stock as an integer
        """
        self._pricePerShare = si.get_live_price(self.ticker)  # gets current live price of the stock
        return self._pricePerShare

    def set_market_cap(self):
        """
        Sets the current MarketCap of a stock
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
        This uses yf finance module which requires a history period when pulling data.
        We index -1 to get the latest volume value
        """
        self._volume = yf.Ticker(self.get_stock_ticker()).history(period ="1d")['Volume'][-1]

    def get_volume(self):
        """
        Gets the current Volume of a stock
        :return volume of stock as an integer
        """
        return self._volume

    def set_three_month_volume(self):
        """
        Sets the three month average Volume of a stock
        This uses pandas data structure to read the the data into the instance variable
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
        """

        self._EPS = si.get_quote_table(self.ticker)['EPS (TTM)']

    def get_eps(self):
        """
        Gets the 12 month EPS value of a stock
        :return EPS of a stock as a integer
        """
        return self._EPS

    def set_Pe_Ratio(self):
        """
        Sets the 12 month Pe-Ratio value of a stock
        """

        self._PeRatio = si.get_quote_table(self.ticker)['PE Ratio (TTM)']

    def get_Pe_Ratio(self):
        """
        Gets the 12 month Pe-Ratio value of a stock
        :return Pe-Ratio of a stock as a float value
        """
        return self._PeRatio

    def set_Beta(self):
        """
        Sets the 5Y Monthly Beta value of a stock
        """

        self._Beta = si.get_quote_table(self.ticker)['Beta (5Y Monthly)']

    def get_Beta(self):
        """
        Gets the 5Y Monthly Beta value of a stock
        :return Beta of a stock as a float value
        """
        return self._Beta


    def set_all_stock_info(self):
        """
        Call all appropriate methods to set the values of the attributes of the stock class
        """
        self.set_stock_stats()
        self.set_stock_company_name()
        self.set_stock_price()
        self.set_market_cap()
        self.set_volume()
        self.set_three_month_volume()
        self.set_eps()
        self.set_Pe_Ratio()
        self.set_Beta()




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
print(s1.get_Pe_Ratio())
print(s1.get_Beta())
# print(s1.stats())
# print(s1.getNews().news_tostring())

#
# print(si.get_holders("aapl"))
# print(si.get_analysts_info("aapl"))
