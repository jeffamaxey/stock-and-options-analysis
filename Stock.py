import datetime
import ValidTicker as validTicker


from News import News
from yahoo_fin import stock_info as si


class Stock:
    """
    The stock class represents a stock of a company.
    :param ticker is the ticker symbol of the Stock
    :thrown RuntimeError if ticker is invalid
    """

    def __init__(self, ticker):
        # convert passed in ticker to all upper case
        ticker = ticker.upper()

        # if the ticker is not valid an exception is thrown
        if not validTicker.valid_ticker(ticker):
            raise RuntimeError

        self.ticker = ticker
        # this variables will hold all information from api call
        self._stock_quote = si.get_quote_table(self.ticker)

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
            self._daily_range  is the range of the stock price between the lowest price and the highest price of the stock within the day
            self._fifty_two_Week_Range  is the range of the stock price between the lowest price and the highest price of the stock within a 52 week period
            self._EarningsDate is the estimated rage of dates that the companies earnings report will be released
            self._one_year_estimate is the estimated price per share of the stock after 1 year


         """

        # declare all stock variables and get associated values from api call to yahoo finance
        self._companyName = validTicker.get_ticker_company(self.ticker)
        self._pricePerShare = self.get_stock_quote()['Quote Price']
        self._marketCap = self.get_stock_quote()['Market Cap']
        self._volume = self.get_stock_quote()['Volume']
        # self._threeMonthAvgVolume = convert.convertStringToInteger(self.get_stock_stats().at[16, "Value"] )
        self._EPS = self.get_stock_quote()['EPS (TTM)']
        self._PeRatio = self.get_stock_quote()['PE Ratio (TTM)']
        self._Beta = self.get_stock_quote()['Beta (5Y Monthly)']
        self._Open = self.get_stock_quote()['Open']
        self._previous_close = self.get_stock_quote()['Previous Close']
        self._bid = self.get_stock_quote()['Bid']
        self._ask = self.get_stock_quote()['Ask']

        self._daily_range = self.get_stock_quote()["Day's Range"]
        self._fifty_two_Week_Range = self.get_stock_quote()['52 Week Range']
        self._EarningsDate = self.get_stock_quote()['Earnings Date']
        self._one_year_estimate = self.get_stock_quote()['1y Target Est']

        # dividend info of stock
        self._has_dividend = self.has_dividend()
        self._dividendFrequency = None
        self._dividendAmount = None
        self._dividendDate = None
        self._exDividend = None

        # Automatically  gets news related to the stock
        self.news = News(self.ticker)

    def get_stock_quote(self):
        """
        Gets a quote of the stock of the stock
        :return a quote of the stock as a python dictionary
        """
        return self._stock_quote

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

    def get_stock_price(self):
        """
        A function used to get the current stock price using yahoo finance
        THe method does not include after hours or pre-market price
        :return price of the stock as an floating point number
        """
        return self._pricePerShare

    def get_market_cap(self):
        """
        Gets the current MarketCap of a stock
        :return marketCap of stock as an integer
        """
        return self._marketCap

    def get_volume(self):
        """
        Gets the current Volume of a stock
        :return volume of stock as an integer
        """
        return self._volume

    def get_three_month_volume(self):
        """
        Gets the three month average Volume of a stock
        :return three month average Volume of a stock as a string
        """
        return self._threeMonthAvgVolume

    def get_eps(self):
        """
        Gets the 12 month EPS value of a stock
        :return EPS of a stock as a integer
        """
        return self._EPS

    def get_pe_ratio(self):
        """
        Gets the 12 month Pe-Ratio value of a stock
        :return Pe-Ratio of a stock as a float value
        """
        return self._PeRatio

    def get_beta(self):
        """
        Gets the 5Y Monthly Beta value of a stock
        :return Beta of a stock as a float value
        """
        return self._Beta

    def get_open(self):
        """
        Gets the open price of a stock
        :return open price of a stock as a float value
        """
        return self._Open

    def get_previous_close(self):
        """
        Gets  the previous close price of a stock
        :return the previous close price of a stock as a floating point number
        """
        return self._previous_close

    def get_bid(self):
        """
        Gets current bid price of a stock
        :return the current bid of a stock as a string
        """
        return self._bid

    def get_ask(self):
        """
        Gets current ask price of a stock
        :return the current ask of a stock as a string
        """
        return self._ask

    def get_fifty_two_week_range(self):
        """
        Gets the 52 week range of the stock price
        :return the the 52 week range of the stock price as a string
        """
        return self._fifty_two_Week_Range

    def get_daily_range(self):
        """
        Gets the daily range of the stock price
        :return the the daily range of the stock price as a string
        """
        return self._daily_range

    def get_earnings_date(self):
        """
        Gets the earnings dates of the stock
        :return the earnings dates of the stock as a string
        """
        return self._EarningsDate

    def get_one_year_estimate(self):
        """
        Gets the  one_year_estimate price of the stock
        :return the one_year_estimate price of the stock as a float
        """
        return self._one_year_estimate

    def has_dividend(self):
        """
        Check whether the stock has a dividend
        :return a boolean true or false depending on whether the stock has a dividend or not
        """
        # if we can pull the dividend yield we know the stock has a dividend
        # the dividend yield from API returns N/A (N/A) if stock does not have a dividend
        return self.get_stock_quote()['Forward Dividend & Yield'] != "N/A (N/A)"

    def get_news(self):
        """
        Get a News class object relating to the stock
        The news object has two methods that can be used by the user such as
        get_news_as_list() which returns article objects within a python list
        news_tostring() which will return a nicely formatted string representation of all news articles

        :return a list of article objects relating to the stock
        """
        return self.news


begin_time = datetime.datetime.now()
s1 = Stock("aapl")

print(s1.get_stock_price())
print(s1.get_market_cap())
print(s1.get_stock_company_name())
print(s1.get_volume())
# print(s1.get_three_month_volume())
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
print(datetime.datetime.now() - begin_time)

# print(s1.stats())
# print(s1.getNews().news_tostring())

#
# print(si.get_holders("aapl"))
# print(si.get_analysts_info("aapl"))
