"""
  The modules used in the file are shown below
  :The finta module is used to compute technical analysis indicators
  :The valid ticker is used to check the validity of a stocks ticker
  :The datetime module is used to get the current date and a range of dates
  :The pandas_datareader.data is used to get history of stock data for technical analysis from yahoo fina
  :The tradingview_ta module is used to get analys opinions from trading view
  :The ray module is used for parallel processing
  """
from model import ValidTicker as validTicker
from finta import TA
import datetime
import pandas_datareader.data as web
from tradingview_ta import TA_Handler, Interval, Exchange
import ray


class Technical:
    """
    The Technical class represents technical analysis of a stock
    :param ticker is the ticker symbol of the Stock
    :thrown RuntimeError if ticker is invalid
    """

    def __init__(self, ticker):
        # convert passed in ticker to all upper case
        ticker = ticker.upper()
        # update ticker symbol within the class
        self.ticker = ticker

        # if the ticker is not valid an exception is thrown
        if not validTicker.valid_ticker(ticker):
            raise RuntimeError("This is not a valid ticker symbol")

        # set end time to me the current date
        end_time = datetime.datetime.now().date().isoformat()
        # set start time to be 60 days prior to today's date for more accurate analysis
        start_time = (datetime.date.today() - datetime.timedelta(60)).isoformat()

        # save a ohlc DataFrame which is returned from yahoo finance
        self.ohlc = web.get_data_yahoo(self.ticker, start=start_time, end=end_time)

        # initialize multiprocessing
        ray.init(ignore_reinit_error=True)

        # using parallel processing to get quotes of stock
        ret_id1 = self.set_rsi.remote(self)
        ret_id2 = self.set_macd.remote(self)
        ret_id3 = self.set_simple_moving_average_range_30_10.remote(self)
        ret_id4 = self.set_pivot_fib.remote(self)
        ret_id5 = self.set_Momentum_Breakout_Bands.remote(self)
        ret_id6 = self.set_tradingview_Quote.remote(self)

        # get all values necessary for technical analysis
        self._RSI, self._MACD, self._simple_moving_average_range_30_10, self._pivot_fib, self._Momentum_Breakout_Bands, self.trading_view_quote = ray.get(
            [ret_id1, ret_id2, ret_id3, ret_id4, ret_id5, ret_id6])

    @ray.remote
    def set_tradingview_Quote(self):
        """
        Sets a quote from trading view on whether the stock is a buy or sell
        :return quote from tradingview
         """
        try:
            analysis = \
            TA_Handler(symbol=self.ticker, screener="america", exchange=validTicker.get_exchange(self.ticker),
                       interval=Interval.INTERVAL_1_MINUTE
                       ).get_analysis().summary["RECOMMENDATION"]

            return analysis

        except Exception:
            return "There is no recommendation"

    @ray.remote
    def set_rsi(self):
        """
        Sets the rsi of a stock
        :return rsi of a stock as a floating point number
        """
        return round(float(TA.RSI(self.ohlc).values[-1]),
                     2)  # convert to float from numpy and round to 2 decimal places

    @ray.remote
    def set_macd(self):
        """
        Sets the MACD of a stock
        :return MACD of a stock as a numpy array
        """
        return TA.MACD(self.ohlc).values[-1]

    @ray.remote
    def set_simple_moving_average_range_30_10(self):
        """
        Sets the simple_moving_average_range_30_10 of a stock
        :return simple_moving_average_range_30_10 of a stock as a string
        """
        simple_moving_average_30_day = round(float(TA.SMA(self.ohlc, 30).values[-1], ),
                                             2)  # convert simple 30 day moving average to float and round to 2 decimal places
        simple_moving_average_10_day = round(float(TA.SMA(self.ohlc, 10).values[-1], ),
                                             2)  # convert simple 10 day moving average to float and round to 2 decimal places

        return str(simple_moving_average_30_day) + " : " + str(
            simple_moving_average_10_day)  # set up a range of the 30 and 10 day moving average as a string

    @ray.remote
    def set_pivot_fib(self):
        """
        Sets the pivot_fib of a stock
        :return pivot_fib of a stock as a string
        """
        return str(TA.PIVOT_FIB(self.ohlc).values[-1][-4:])  # get the last 4 latest fibonacci pivot points

    @ray.remote
    def set_Momentum_Breakout_Bands(self):
        """
        Sets the Momentum Breakout Bands of a stock
        :return Momentum Breakout Bands as numpy array
        """
        return TA.MOBO(self.ohlc).values[-1]  # convert to float from numpy and round to 2 decimal places

    def get_rsi(self):
        """
        Gets the rsi of a stock
        :return rsi of a stock as a floating point number
        """
        return self._RSI

    def get_macd(self):
        """
        Gets the MACD of a stock
        :return MACD of a stock as numpy array
        """
        return self._MACD

    def get_simple_moving_average_range_30_10(self):
        """
        Gets the simple_moving_average_range_30_10 of a stock
        :return simple_moving_average_range_30_10 of a stock as a string
        """
        return self._simple_moving_average_range_30_10

    def get_pivot_fib(self):
        """
        Gets the pivot_fib of a stock
        :return pivot_fib of a stock as a string
        """
        return self._pivot_fib

    def get_momentum_breakout_bands(self):
        """
        Gets the Momentum Breakout Bands of a stock
        :return Momentum Breakout Bands of a stock as a numpy array
        """
        return self._Momentum_Breakout_Bands

    def to_string_summary(self):
        """
        Get a string representation of the technicals analysis which provides a small summary of details
        :return string containing summary of analysis
        """
        rsi = self.get_rsi()
        MACD = self.get_macd()
        positive_momentum = True  # assume we have positive momentum

        String = "The current RSI of the stock is " + str(rsi) + " "
        if rsi > 70:
            String += "which indicates the stock is overbought.\n\n"
        elif rsi < 30:
            String += "which indicates the stock is oversold.\n\n"
        else:
            String += "which indicates the stock is neutral.\n\n"

        String += "The current MACD of the stock is " + str(MACD)

        # go through mac d values and see if they are both in negative range indicating negative momentum
        for i in MACD:
            if i < 0:
                positive_momentum = False

        if positive_momentum:
            String += " which may indicate positive momentum.\n\n"
        else:
            String += " which may indicate negative momentum.\n\n"

        String += "The Momentum Breakout Bands of the stock are " + str(
            self.get_momentum_breakout_bands()) + " when stock price \nbreaks out of these regions it can " \
                                                  "signify a trend move or price spike worth trading.\n\n"
        String += "The Fibonacci pivots of the stock are " + str(
            self.get_pivot_fib()) + " which are used  to \nidentify key support and resistance levels to determine the trend or to enter and exit trades.\n\n"

        String += "The simple moving average for 30 and 10 days is " + self.get_simple_moving_average_range_30_10() + " which can be used to  identify\ncurrent price trends and potential for a change in the trend.\n"

        String += "\nThe current recommendation by analysts for the stock  is: " + str(self.trading_view_quote)
        return String



