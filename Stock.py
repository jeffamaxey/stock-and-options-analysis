from yahoo_fin import stock_info as si
import pandas_datareader as web

class Stock:
    """
    The stock class represents a stock of a company.
    @param ticker is the ticker symbol of the Stock
    """
    def __init__(self, ticker):
        # stock information
        self.ticker = ticker
        self._pricePerShare = 0
        self._marketCap = 0
        self._volume = 0
        self._threeMonthAvgVolume = 0
        self._EPS = 0
        self._PeRatio = 0
        self._Beta = 0
        self._Open = 0
        self._Close = 0
        self._Bid = 0
        self._Ask = 0
        self._Low = 0
        self._High = 0
        self._EarningsDate = " "
        self._Fifty_Two_week_low = 0
        self._Fifty_Two_week_high = 0
        self._one_year_estimate = 0

        # dividend info
        self._has_dividend = False
        self._dividendFrequency = 0
        self._dividendAmount = 0
        self._dividendDate = 0
        self._exDividend = 0

    def stock_price(self):
        """
         A function used to get the current stock price using yahoo finance
        @return price of the stock as an integer
        """
        self._pricePerShare = si.get_live_price(self.ticker)  # gets current live price of the stock
        return self._pricePerShare

        # current_date = date.today()
        # pull_date = current_date
        #
        # if current_date.weekday() == 5:
        #     pull_date = current_date - timedelta(1)
        #
        # if current_date.weekday() == 6:
        #     pull_date = current_date - timedelta(2)
        #
        # price = pn.data.get(self.ticker,  pull_date)
        # return price

    def marketCap(self):
        """
        Gets the current MarketCap of a stock
        @return marketCap of stock as an integer
        """
        self._marketCap =  web.get_quote_yahoo(self.ticker)['marketCap'][
            0]  # index 0 to ignore excess ticker output

        return self._marketCap

    def stats(self):
        """
        Gets a summary of stats of the stock
        @return summary of the stocks stats
        """

        return si.get_stats(self.ticker)


s1 = Stock("aapl")

print(s1.stock_price())
print(s1.marketCap())
print(s1.stats())
#
# print(si.get_holders("aapl"))
# print(si.get_analysts_info("aapl"))