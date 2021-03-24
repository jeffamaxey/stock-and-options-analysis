from aiohttp import web
from finta.utils import resample


from model import ValidTicker as validTicker
from finta import TA
import yfinance as yahoo_finance
import datetime



# ___library_import_statements___
import pandas as pd
# make pandas to print dataframes nicely
pd.set_option('expand_frame_repr', False)
import pandas_datareader.data as web

#newest yahoo API
import yfinance as yahoo_finance

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
        ohlc = web.get_data_yahoo(self.ticker, start=start_time, end=end_time)

        # calculate all values necessary for technical analysis
        self._RSI = round(float(TA.RSI(ohlc).values[-1]), 2) # convert to float from numpy and round to 2 decimal places
        self._MACD = str(TA.MACD(ohlc).values[-1]) # get a string representation of the MACD

        simple_moving_average_30_day = round(float(TA.SMA(ohlc,30).values[-1],), 2) # convert simple 30 day moving average to float and round to 2 decimal places
        simple_moving_average_10_day = round(float(TA.SMA(ohlc, 10).values[-1], ),
                                             2)  # convert simple 10 day moving average to float and round to 2 decimal places

        self._simple_moving_average_range_30_10 = str(simple_moving_average_30_day) + " : " + str(simple_moving_average_10_day) # set up a range of the 30 and 10 day moving average as a string
        self._pivot_fib = TA.PIVOT_FIB(ohlc).values[-1][-4:] # get the last 4 latest fibonacci pivot points



        print(self._RSI)
        print(self._MACD)
        print(self._simple_moving_average_range_30_10)
        print(self._pivot_fib)




stock = Technical("aapl")

