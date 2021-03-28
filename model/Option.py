import yfinance as yf
import datetime
from model import ValidTicker as validTicker
from model.organizeOptionData import get_finalDict
#import pandas as pd
#import numpy as np


class Option:
    def __init__(self, tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm):
        """
        Attributes:
        self.tickerSymbol:         ex.'TSLA'        -is the _ticker tickerSymbol of the underlying asset
            self.expiration_date:  ex.'2023-03-17'  -expiration date (year/month/day)
            self.option_style:     ex.'American'    -American or European
            self.option_type:      ex.'Call'        -Call or Put
            self.data_source:      ex.'Yahoo'       -Yahoo or other
            self.itm_atm_otm:      ex.'atm'         -itm+1, itm, atm, otm, otm+1
        """
        #if not validTicker.valid_ticker(tickerSymbol):
        #raise RuntimeError("This is not a valid ticker symbol")

        # update ticker symbol within the class
        self.tickerSymbol = tickerSymbol

        #get_options_chain(self.tickerSymbol)
        self.expiration_date = expiration_date
        self.option_style = option_style
        self.option_type = option_type
        self.data_source = data_source
        self.itm_atm_otm = itm_atm_otm

        #Call the organized final dictionary of the data
        get_finalDict(self.tickerSymbol, self.option_type, self.itm_atm_otm, self.expiration_date)

    def get_currentPriceOfTheUnderlyingAsset(self):
        tickerData = yf.Ticker(self.tickerSymbol)
        today = datetime.datetime.today().isoformat()
        # First ten characters are the actual date
        tickerDataFrame = tickerData.history(period='1d', start='2021-1-1', end=today[:10])
        currentPriceOfUnderlyingAsset = tickerDataFrame['Close'].iloc[-1]
        return currentPriceOfUnderlyingAsset

    def get_riskFreeRate(self):
        # Can use the what most finance research papers use, i.e. the risk-free rate from the Kenneth French data library.
        # http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
        # The rates are annual. So if you want log returns just take the log of 1+rft and divide by 365
        #
        # You should use the return of the less risky government bond of the area you're studying,
        # as the US _T-Bill for North America option market
        # the rate depends on the time to expiration
        #
        # Hull himself suggests using a fixed risk-free rate equal to 3%
        # Often times we use less than that like 1%, sometimes 5% or 7%
        # should redo this method to calculate the risk free rate based on _T(timeToExpiration) and the _T-Bills
        return 0.01

    #def get_entire_sorted_options_chain(self):
    #print(get_options_chain(self))
    #return organizeOptionData.get_options_chain(self)

    def get_expirations(self):
        tickerData = yf.Ticker(self)
        # Expiration dates
        optionExpirations = tickerData.options
        return optionExpirations
