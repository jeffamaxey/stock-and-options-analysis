"""
  The modules used in the file are shown below
  :The News module is a class used to fetch news relating to a stock
  :The Fundamental module is a class used to fetch stock fundamentals
  :The BalanceSheet module is a class used to fetch BalanceSheet information of the stock
  :The CashFlow module is a class used to fetch CashFlow information of the stock
  :The yahoo_fin module is used to fetch stock metrics
  """

from model import ValidTicker as validTicker
from model.News import News
from model.Fundamental import Fundamental
from model.BalanceSheet import BalanceSheet
from model.IncomeStatement import IncomeStatement
from model.CashFlow import CashFlow
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
            raise RuntimeError("This is not a valid ticker symbol")

        # update ticker symbol within the class
        self.ticker = ticker

        # these variables will hold all information from api call
        self._stock_quote = si.get_quote_table(self.ticker)
        self.stock_enhanced_quote = si.get_stats(self.ticker)

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
            
            self._has_dividend is a boolean which determines if the stock has a dividend
            self._forward_annual_dividend_rate is the  projection of a company's yearly dividend
            self._dividendYield is a financial ratio that shows how much a company pays out in dividends each year relative to its stock price
            self._dividendDate is the date that the dividend is paid
            self._exDividend is a date where if you purchase a stock on its exDividend date or after, you will not receive the next dividend payment
            self._news is a News object containing articles relating to the stock
            self._fundamental is the Fundamental object containing methods to obtain a stocks fundamental information
            self._balance_sheet is the BalanceSheet  object containing methods to obtain a stocks balanceSheet information
            self._income_statement is the IncomeStatement object containing methods to obtain a stocks income statement information
            self._cash_flow is the CashFlow object containing methods to obtain a stocks cashFlow information
            
         """

        # declare all stock variables and get associated values from api call to yahoo finance
        self._companyName = validTicker.get_ticker_company(self.ticker)
        self._pricePerShare = round(self.get_stock_quote()['Quote Price'], 2)
        self._marketCap = self.get_stock_quote()['Market Cap']
        self._volume = self.get_stock_quote()['Volume']
        self._threeMonthAvgVolume = self.get_enhanced_quote().at[
            16, "Value"]  # index 16 of the pandas dataframe corresponds to the three_month_volume
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
        self._one_year_estimate = round(self.get_stock_quote()['1y Target Est'], 2)

        # dividend info of stock
        self._has_dividend = self.get_stock_quote()['Forward Dividend & Yield'] != "N/A (N/A)"  # if we can pull the dividend yield we know the stock has a dividend; the dividend yield from API returns N/A (N/A) if stock does not have a dividend

        self._forward_annual_dividend_rate = self.stock_enhanced_quote.at[
            27, "Value"]  # index 27 of the pandas dataframe corresponds to the Forward Annual Dividend Rate
        self._dividendYield = self.stock_enhanced_quote.at[
            28, "Value"]  # index 28 of the pandas dataframe corresponds to the Forward Annual Dividend Yield
        self._dividendDate = self.stock_enhanced_quote.at[
            33, "Value"]  # index 33 of the pandas dataframe corresponds to the Dividend Date
        self._exDividend = self.stock_enhanced_quote.at[
            34, "Value"]  # index 34 of the pandas dataframe corresponds to the Ex-Dividend Date

        # Automatically  gets news, fundamental, balance sheet, income statement, cash flow related to the stock
        self._news = News(self.ticker)
        self._fundamental = Fundamental(self.ticker)
        self._balance_sheet = BalanceSheet(self.ticker)
        self._income_statement = IncomeStatement(self.ticker)
        self._cash_flow = CashFlow(self.ticker)

    def get_stock_quote(self):
        """
        Gets a quote of the stock of the stock
        :return a quote of the stock as a python dictionary
        """
        return self._stock_quote

    def get_enhanced_quote(self):
        """
        Gets an enhanced quote of the stock which has more information
        :return a quote of the stock as a python dictionary
        """
        return self.stock_enhanced_quote

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
        return self._has_dividend

    def get_forward_annual_dividend_rate(self):
        """
        Get the forward_annual_dividend_rate of the stock
        :return a forward_annual_dividend_rate of stock as a floating point value
        """
        return self._forward_annual_dividend_rate

    def get_dividend_yield(self):
        """
        Get the dividend yield of the stock
        :precond stock must have dividend
        :throws RuntimeError if stock does not have a dividend
        :return a dividend yield of stock as a floating point value
        """
        if not self.has_dividend():
            raise RuntimeError("This stock does not have dividend")

        return self._dividendYield

    def get_dividend_date(self):
        """
        Get the dividend date of the stock
        :precond stock must have dividend
        :throws RuntimeError if stock does not have a dividend
        :return a dividend date of stock as a string
        """
        if not self.has_dividend():
            raise RuntimeError("This stock does not have dividend")

        return self._dividendDate

    def get_ex_dividend(self):
        """
        Get the exDividend date of the stock
        :precond stock must have dividend
        :throws RuntimeError if stock does not have a dividend
        :return a exDividend date of stock as a string
        """
        if not self.has_dividend():
            raise RuntimeError("This stock does not have dividend")

        return self._exDividend

    def get_news(self):
        """
        Get a News class object relating to the stock
        The news object has two methods that can be used by the user such as
        get_news_as_list() which returns article objects within a python list
        news_tostring() which will return a nicely formatted string representation of all news articles

        :return a News object relating to the stock
        """
        return self._news

    def get_fundamental(self):
        """
        Get a Fundamental class object relating to the stock
        The Fundamental  has methods that can be used by the user such as
        get_priceFairValueTTM(), get_debtEquityRatioTTM,etc

        :return a Fundamental object relating to the stock
        """
        return self._fundamental

    def get_balance_sheet(self):
        """
        Get a BalanceSheet class object relating to the stock
        The BalanceSheet has methods that can be used by the user such as
        get_totalCurrentAssets(), get_totalNonCurrentAssets(),etc

        :return a BalanceSheet object relating to the stock
        """
        return self._balance_sheet

    def get_income_statement(self):
        """
        Get a IncomeStatement class object relating to the stock
        The IncomeStatement has methods that can be used by the user such as
        getRevenue(), getIncomeTaxExpense(),etc

        :return a BalanceSheet object relating to the stock
        """
        return self._income_statement

    def get_cash_flow(self):
        """
        Get a CashFlow class object relating to the stock
        The CashFlow has methods that can be used by the user such as
        getNetCashProvidedByOperatingActivities(), getNetCashUsedForInvestingActivites,etc

        :return a CashFlow object relating to the stock
        """
        return self._cash_flow