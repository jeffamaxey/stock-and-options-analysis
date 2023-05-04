import pandas as pd
import numpy as np
import yfinance as yf
import datetime


def get_options_chain(tickerSymbol, expiration_date):
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
    options['T'] = np.abs(
        (options['expirationDate'] - datetime.datetime.now()).dt.days / 365
    )

    # Boolean column if the option is a CALL
    options['CALL'] = options['contractSymbol'].str[4:].apply(lambda x: "C" in x)

    options[['bid', 'ask', 'strike']] = options[['bid', 'ask', 'strike']].apply(pd.to_numeric)
    options['mid'] = (options['bid'] + options['ask']) / 2 # Calculate the midpoint of the bid-ask

    # Drop columns that are not needed
    options = options.drop(columns=['contractSymbol', 'contractSize', 'currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice', 'inTheMoney', 'bid', 'ask', 'volume', 'mid', 'openInterest'])

    today = datetime.datetime.now().isoformat()
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
    #####NEED TO UPDATE THESE SO if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == ticker_symbol.chosenExpiration
    #####
    #Search for the dictionary of the strike price closest to the market price
    def find_atm_call(options_record, key, value):
        for i, dic in enumerate(options_record):
            if dic[key] == value and dic['CALL'] is True and dic['expirationDate'] == expiration_date:
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
            if dic[key] == value and dic['CALL'] is False and dic['expirationDate'] == expiration_date:
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


def get_finalDict(ticker_symbol, option_type, itm_atm_otm, expiration_date):
    # instead of ticker_symbol it was working with (self) before
    # USER SELECTS PUT or CALL, USER SELECTS EXPIRATION, USER SELECTS ITMATMOTM
    # Once user selects expiration it narrows down the potential fields to five different itm_atm_otm = ['itm+1', 'itm', 'atm', 'otm', 'otm+1']

    # get_itm_atm_otm_list():
    # ['itm+1', 'itm', 'atm', 'otm', 'otm+1'
    #itm_atm_otm
    finalDict = {}
    if option_type == 'Call':
        if itm_atm_otm == 'itm+1':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[0][0]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[0][0]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[0][0]['impliedVolatility'], 'OptionType': 'Call'}
        elif itm_atm_otm == 'itm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[0][1]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[0][1]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[0][1]['impliedVolatility'], 'OptionType': 'Call'}
        elif itm_atm_otm == 'atm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[0][2]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[0][2]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[0][2]['impliedVolatility'], 'OptionType': 'Call'}
        elif itm_atm_otm == 'otm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[0][3]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[0][3]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[0][3]['impliedVolatility'], 'OptionType': 'Call'}
        elif itm_atm_otm == 'otm+1':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[0][4]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[0][4]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[0][4]['impliedVolatility'], 'OptionType': 'Call'}

    elif ticker_symbol.option_type == "Put":
        if itm_atm_otm == 'itm+1':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[1][4]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[1][4]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[1][4]['impliedVolatility'], 'OptionType': 'Put'}
        elif itm_atm_otm == 'itm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[1][3]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[1][3]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[1][3]['impliedVolatility'], 'OptionType': 'Put'}
        elif itm_atm_otm == 'atm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[1][2]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[1][2]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[1][2]['impliedVolatility'], 'OptionType': 'Put'}
        elif itm_atm_otm == 'otm':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[1][1]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[1][1]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[1][1]['impliedVolatility'], 'OptionType': 'Put'}
        elif itm_atm_otm == 'otm+1':
            finalDict = {'Strike': get_options_chain(ticker_symbol, expiration_date)[1][0]['strike'], "Time-to-expiration": get_options_chain(ticker_symbol, expiration_date)[1][0]['T'], "Sigma": get_options_chain(ticker_symbol, expiration_date)[1][0]['impliedVolatility'], 'OptionType': 'Put'}

    timeToExpiration = finalDict['Time-to-expiration']
    volatility = finalDict['Sigma']
    strike = finalDict['Strike']

    return finalDict
