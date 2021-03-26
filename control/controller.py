from model.Option import Option
from model.Valuation import Valuation

########################################################################
#user clicks expiration than the ITMATMOTM shows (5 market prices) the 2 closest ITM and 2 closest OTM Strike Prices as well as ATM price
#we need to find the record first based on the expiration and second based on the closest Strike prices to the current asset price
#Each expiration will be the ID, each expiration will have 2-ITM 1-ATM 2-OTM strike prices associated with it
########################################################################
#strike impliedVolatility expirationDate    T   optionType

# TRYING TO ADJUST YFINANCE INTERPRETATION OF (ITM ATM OTM)
# (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
# (ATM Call) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (OTM Call) if the Call strike price is > the the current price of the underlying asset
# (OTM Put) if the Put strike price is < the current price of the underlying asset
# (ATM Put) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option
# ALLOW THEM TO SELECT A STRIKE PRICE

##### IN Option.py
##### NEED TO UPDATE LINES IN OPTION.PY SO-> if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == self.chosenExpiration
##### NEED TO UPDATE LINES IN OPTION.PY So user selects the restraint of an expiration date
##### UI IS AFFECTING THE DATA RETRIEVAL FOR THIS PART
#self.optionExpirations = yf.Ticker(self).options
#self.chosenExpiration = '2023-01-20' # User Must select an expiration date immediately after selecting a ticker

def input_quantitative_analysis(tickerSymbol, expirationDate, optionStyle, optionType, dataSource, ITMATMOTM):
    """
    returns the quantitative analysis 'inputs' as a dictionary
    """
    try:
        option = Option(tickerSymbol)
    except RuntimeError:    # This exception is thrown when the ticker is invalid
        return None
    # User Inputs
    expirationDate = option.get_expirations()
    optionStyle = "American"
    optionType = "Call"
    dataSource = "Yahoo"
    step = {}


    # USER SELECTS PUT or CALL, USER SELECTS EXPIRATION, USER SELECTS ITMATMOTM
    # Once user selects expiration it narrows down the potential fields to five different ITMATMOTM

    DictCalls = {expirationDate[0]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[1]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[2]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[3]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[4]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[5]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[6]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[7]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[8]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[9]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                        'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                        'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                        'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                        'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[10]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[11]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[12]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[13]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[14]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[15]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 expirationDate[16]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                         'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                         'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                         'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                         'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}}}


    DictPuts = {expirationDate[0]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[1]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[2]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[3]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[4]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[5]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[6]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[7]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[8]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[9]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                       'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                       'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                       'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                       'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[10]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[11]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[12]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[13]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[14]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[15]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                expirationDate[16]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                        'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                        'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                        'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                        'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}}}
    # Not sure how well this works
    if optionType == "Call":
        step = DictCalls
    elif optionType == "Put":
        step = DictPuts
    for x in step:
        ITMATMOTM = step[x][0]+step[x][1]+step[x][2]+step[x][3]+step[x][4]
        if step[x] == expirationDate[x]:
            return expirationDate[x]
        x += 1

    return tickerSymbol, expirationDate, optionStyle, optionType, dataSource, ITMATMOTM

def display_quantitative_analysis(tickerSymbol, expirationDate, optionStyle, optionType, dataSource, ITMATMOTM):
    """
    returns the quantitative analysis 'outputs' as a dictionary
    """
    try:
        option = Option(tickerSymbol)
        riskFreeRate = option.get_riskFreeRate()
        currentUnderlyingPrice = option.get_currentPriceOfTheUnderlyingAsset()
        option_chain = option.get_entire_sorted_options_chain()
        valuation = Valuation(tickerSymbol)
    except RuntimeError:    # This exception is thrown when the ticker is invalid
        return None

    # User Inputs
    expirationDate = option.get_expirations()
    optionStyle = "American"
    optionType = "Call"
    dataSource = "Yahoo"

    # NOT SURE IF THIS WORKS
    ITMATMOTM = {}
    for i, dic in enumerate(ITMATMOTM):
        return ITMATMOTM == ITMATMOTM[i]
    strike = ITMATMOTM[0]


    #chosenExpiration = expirationDate
    #strikeMatchChosenExpiration = chosenExpiration
    #TmatchChosen = chosenExpiration
    #sigmaMatchedChosen = chosenExpiration

    analysis = {
        "variables": {"(r)risk_free_rate": riskFreeRate,
                      "(s)current_underlying_price": currentUnderlyingPrice,
                      #"chosen_expiration": chosenExpiration,
                      #"(x)strike_market_price_match_chosen_expiration": strikeMatchChosenExpiration,
                      #"(T)Time_to_expiration_match_chosen": TmatchChosen,
                      #"(sigma)implied_volatility_match_chosen": sigmaMatchedChosen,
                      "intrinsic_value": valuation.intrinsicValue(),
                      "speculative_premium": valuation.speculativePremium()},
        "valuations": {"black_scholes": valuation.blackScholes(),
                       "binomial": valuation.binomialModel(),
                       "average_price": valuation.monteCarloSimulation(),
                       #"market_price": strikeMatchChosenExpiration(),
                       "implied_volatility": valuation.impliedVolatility()},
        "the_greeks": {"delta": valuation.delta(),
                       "gamma": valuation.gamma(),
                       "theta": valuation.theta(),
                       "vega": valuation.vega(),
                       "rho": valuation.rho(),
                       "charm": valuation.charm()}, }
    return analysis

#print(input_quantitative_analysis("TSLA"))
#print(display_quantitative_analysis("TSLA"))




