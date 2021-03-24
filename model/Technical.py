from model import ValidTicker as validTicker


from tradingview_ta import TA_Handler, Interval, Exchange
from yahoo_fin import stock_info as si




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





    # def Datapull(self):
    #     try:
    #         df = (pd.io.data.DataReader(self.ticker,'yahoo',start='01/01/2010'))
    #         return df
    #         print 'Retrieved', Stock
    #         time.sleep(5)
    #     except Exception, e:
    #         print 'Main Loop', str(e)
    #
    #
    # def RSIfun(price, n=14):
    #     delta = price['Close'].diff()
    #
    #     dUp, dDown = delta.copy(), delta.copy()
    #     dUp[dUp < 0] = 0
    #     dDown[dDown > 0] = 0
    #
    #     RolUp = pd.rolling_mean(dUp, n)
    #     RolDown = pd.rolling_mean(dDown, n).abs()
    #
    #     RS = RolUp / RolDown
    #
    #     rsi = 100.0 - (100.0 / (1.0 + RS))
    #     return rsi
    #
    # Stock='AAPL'
    # df=Datapull(Stock)
    # RSIfun(df)

tesla = TA_Handler(
    symbol="tsla",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_MINUTE
)
rsi = tesla.get_analysis().indicators.get("RSI")
print(rsi)
print(tesla.get_analysis().indicators)

validTicker.get_ticker_company("aapl")