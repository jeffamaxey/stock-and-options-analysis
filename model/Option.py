import pandas as pd
import numpy as np
import yfinance as yf
import datetime

def options_chain(tickerSymbol):

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

    # Use expiration date and current date to calculate T time to maturity
    # Can adjust data source to get the correct expiration date using + datetime.timedelta(days = 1)
    options['expirationDate'] = pd.to_datetime(options['expirationDate'])
    options['T'] = (options['expirationDate'] - datetime.datetime.today()).dt.days / 365

    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)

    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mid'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask

    # Drop columns that are not needed
    options = options.drop(columns=['contractSymbol', 'contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice', 'bid', 'ask', 'volume', 'mid', 'openInterest'])

    today = datetime.datetime.today().isoformat()
    # First ten characters are the actual date
    tickerDataFrame = tickerData.history(period='1d', start='2021-1-1', end=today[:10])
    currentPriceOfUnderlyingAsset = tickerDataFrame['Close'].iloc[-1]
    #print(optionExpirations, "\n")
    #print(str(currentPriceOfUnderlyingAsset), "\n")

    # TRYING TO ADJUST YFINANCE INTERPRETATION OF (ITM ATM OTM)
    # (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
    # (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option
    # (ATM) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
    # (OTM Call) if the Call strike price is > the the current price of the underlying asset
    # (OTM Put) if the Put strike price is < the current price of the underlying asset
    # ALLOW THEM TO SELECT A STRIKE PRICE
    #def __eq__(options):
    #if options['CALL'] == True and currentPriceOfUnderlyingAsset > options['strike']:
    #   return options['inTheMoney'] == True
    #elif options['CALL'] == False and currentPriceOfUnderlyingAsset < options['strike']:
    #   return options['inTheMoney'] == True
    #elif options['strike'] == currentPriceOfUnderlyingAsset:
    #   return options['inTheMoney'] == str('At-The-Money')
    #else:
    #   return options['inTheMoney']==False
    #__eq__(options)

    # orient: String value, (‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’) Defines which dtype to convert Columns(series into).
    # For example, ‘list’ would return a dictionary of lists with Key=Column name and Value=List (Converted series).
    # into: class, can pass an actual class or instance. For example in case of defaultdict instance of class can be passed.
    # Default value of this parameter is dict.
    # dropping null value columns to avoid errors
    options.dropna(inplace = True)
    options_record = options.to_dict(orient='records')

    ########################################################################
    #user clicks expiration than the ITMATMOTM shows (5 market prices) the 2 closest ITM and 2 closest OTM Strike Prices as well as ATM price
    #we need to find the record first based on the expiration and second based on the closest Strike prices to the current asset price
    #Each expiration will be the ID, each expiration will have 2-ITM 1-ATM 2-OTM strike prices associated with it
    ########################################################################
    #strike impliedVolatility inTheMoney expirationDate    T   optionType

    #return options #to just return the dataframe
    return options_record #to return the dataframe as a record dictionary




#################################################################################
# MOVE TO TESTING ###############################################################
#################################################################################

#Adjustments so print shows all columns and more rows of the dataframe
desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 12)

# to display more than 10 rows when the dataframe is truncated set min_rows greater than 10
# with more than 200 rows if max_rows is 200 and min_rows is 20, 10 from the head and 10 from the tail are displayed
# with more than 200 rows of data if max_rows is 200 and min_rows is none 100 from the head and 100 from the tail will be displayed
pd.set_option("display.max_rows", 200)
pd.set_option("display.min_rows", None)


#options_chain("TSLA")
print(options_chain("TSLA"))

# ALTERNATIVE APPROACH FOR PRINTING DATAFRAME CONTENTS
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#print(options_chain("TSLA"))

#################################################################################
# MOVE TO TESTING ###############################################################
#################################################################################

