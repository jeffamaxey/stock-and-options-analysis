import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from model import ValidTicker as validTicker


def get_options_chain(tickerSymbol):
    tickerData = yf.Ticker(tickerSymbol)
    # Expiration dates
    optionExpirations = tickerData.options

    # Get options for each expiration
    options = pd.DataFrame()
    for e in optionExpirations:
        opt = tickerData.option_chain(e)
        opt = pd.DataFrame().append(opt.calls).append(opt.puts)
        opt['expirationDate'] = e
        options = options.append(opt, ignore_index=True)

    # Use expiration date and current date to calculate _T time to maturity
    # Can adjust data source after hours to get the correct expiration date using + datetime.timedelta(days = 1)
    options['expirationDate'] = pd.to_datetime(options['expirationDate'])
    # Multiplied by np.abs because I was getting a negative result for all of my _T values (Parentheses were needed to work properly)
    options['T'] = np.abs(((options['expirationDate'] - datetime.datetime.today()).dt.days) / (365))

    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)

    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mid'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask

    # Drop columns that are not needed
    options = options.drop(columns=['contractSymbol', 'contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice', 'inTheMoney', 'bid', 'ask', 'volume', 'mid', 'openInterest'])

    today = datetime.datetime.today().isoformat()
    # First ten characters are the actual date
    tickerDataFrame = tickerData.history(period='5d', start='2021-1-1', end=today[:10])
    currentPriceOfUnderlyingAsset = tickerDataFrame['Close'].iloc[-1]

    # dropping null value columns to avoid errors, converting data frame to dictionary record
    options.dropna(inplace=True)
    options_record = options.to_dict(orient='records')

    # TRYING TO ADJUST YFINANCE INTERPRETATION OF (ITM ATM OTM)
    # (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
    # (ATM Call) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
    # (OTM Call) if the Call strike price is > the the current price of the underlying asset
    # (OTM Put) if the Put strike price is < the current price of the underlying asset
    # (ATM Put) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
    # (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option

    #####
    #####NEED TO UPDATE THESE SO if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == self.chosenExpiration
    #####
    #Search for the dictionary of the strike price closest to the market price
    def find_atm_call(options_record, key, value):
        for i, dic in enumerate(options_record):
            if dic[key] == value and dic['CALL'] is True: # and dic['expirationDate'] == controller.expiration_date:
                return i
    ATM = 40 #find_atm_call(options_record, "strike", int(currentPriceOfUnderlyingAsset))
    atm_call = options_record[ATM]
    otm_call = options_record[ATM+1]
    otm_call_plus = options_record[ATM+2]
    itm_call = options_record[ATM-1]
    itm_call_minus = options_record[ATM-2]

    #Search for target Puts
    def find_atm_put(options_record, key, value):
        for i, dic in enumerate(options_record):
            if dic[key] == value and dic['CALL'] is False:
                return i
    ATM_put = 42 #find_atm_put(options_record, "strike", int(currentPriceOfUnderlyingAsset))
    atm_put = options_record[ATM_put]
    itm_put = options_record[ATM_put+1]
    itm_put_plus = options_record[ATM_put+2]
    otm_put = options_record[ATM_put-1]
    otm_put_minus = options_record[ATM_put-2]

    Calls = [itm_call_minus, itm_call, atm_call, otm_call, otm_call_plus]
    Puts = [otm_put_minus, otm_put, atm_put, itm_put, itm_put_plus]
    return Calls, Puts


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

        # convert passed in _ticker to all upper case
        #if not validTicker.valid_ticker(tickerSymbol):
            #raise RuntimeError("This is not a valid _ticker symbol")

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

    def get_entire_sorted_options_chain(self):
        #print(get_options_chain(self))
        return get_options_chain(self)

    def get_expirations(self):
        tickerData = yf.Ticker(self)
        # Expiration dates
        optionExpirations = tickerData.options
        return optionExpirations


# CALLS
    # Calls = [itm_call_minus, itm_call, atm_call, otm_call, otm_call_plus]
    # Puts = [otm_put_minus, otm_put, atm_put, itm_put, itm_put_plus]
    # strike impliedVolatility expirationDate    T   optionType

    def get_atm_call_strike(self):
        return get_options_chain(self)[0][2]['strike']

    def get_atm_call_T(self):
        return get_options_chain(self)[0][2]['T']

    def get_atm_call_sigma(self):
        return get_options_chain(self)[0][2]['impliedVolatility']

    def get_itm_call_strike(self):
        return get_options_chain(self)[0][1]['strike']

    def get_itm_call_T(self):
        return get_options_chain(self)[0][1]['T']

    def get_itm_call_sigma(self):
        return get_options_chain(self)[0][1]['impliedVolatility']

    def get_itm_call_minus_strike(self):
        return get_options_chain(self)[0][0]['strike']

    def get_itm_call_minus_T(self):
        return get_options_chain(self)[0][0]['T']

    def get_itm_call_minus_sigma(self):
        return get_options_chain(self)[0][0]['impliedVolatility']

    def get_otm_call_strike(self):
        return get_options_chain(self)[0][3]['strike']

    def get_otm_call_T(self):
        return get_options_chain(self)[0][3]['T']

    def get_otm_call_sigma(self):
        return get_options_chain(self)[0][3]['impliedVolatility']

    def get_otm_call_plus_strike(self):
        return get_options_chain(self)[0][4]['strike']

    def get_otm_call_plus_T(self):
        return get_options_chain(self)[0][4]['T']

    def get_otm_call_plus_sigma(self):
        return get_options_chain(self)[0][4]['impliedVolatility']

#PUTS###############################################################

    def get_atm_put_strike(self):
        return get_options_chain(self)[1][2]['strike']

    def get_atm_put_T(self):
        return get_options_chain(self)[1][2]['T']

    def get_atm_put_sigma(self):
        return get_options_chain(self)[1][2]['impliedVolatility']

    def get_otm_put_strike(self):
        return get_options_chain(self)[1][1]['strike']

    def get_otm_put_T(self):
        return get_options_chain(self)[1][1]['T']

    def get_otm_put_sigma(self):
        return get_options_chain(self)[1][1]['impliedVolatility']

    def get_otm_put_plus_strike(self):
        return get_options_chain(self)[1][0]['strike']

    def get_otm_put_plus_T(self):
        return get_options_chain(self)[1][0]['T']

    def get_otm_put_plus_sigma(self):
        return get_options_chain(self)[1][0]['impliedVolatility']

    def get_itm_put_strike(self):
        return get_options_chain(self)[1][3]['strike']

    def get_itm_put_T(self):
        return get_options_chain(self)[1][3]['T']

    def get_itm_put_sigma(self):
        return get_options_chain(self)[1][3]['impliedVolatility']

    def get_itm_put_minus_strike(self):
        return get_options_chain(self)[1][4]['strike']

    def get_itm_put_minus_T(self):
        return get_options_chain(self)[1][4]['T']

    def get_itm_put_minus_sigma(self):
        return get_options_chain(self)[1][4]['impliedVolatility']



