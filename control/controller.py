from model.Option import Option
from model.Valuation import Valuation
import yfinance as yf

########################################################################
#user clicks expiration than the ITMATMOTM shows (5 market prices) the 2 closest ITM and 2 closest OTM Strike Prices as well as ATM price
#Each expiration will be the ID, each expiration will have 2-ITM 1-ATM 2-OTM associated with it giving results for (strike, _T, & _sigma)
########################################################################
#strike impliedVolatility expirationDate    _T   optionType
# (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
# (ATM Call) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (OTM Call) if the Call strike price is > the the current price of the underlying asset
# (OTM Put) if the Put strike price is < the current price of the underlying asset
# (ATM Put) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option

##### IN Option.py
##### NEED TO UPDATE LINES IN OPTION.PY SO-> if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == self.chosenExpiration
##### NEED TO UPDATE LINES IN OPTION.PY So user selects the restraint of an expiration date


def get_expiration_date_list():
    return ['2021-04-01', '2021-04-09', '2021-04-16', '2021-04-23', '2021-04-30',
            '2021-05-21', '2021-06-18', '2021-07-16', '2021-09-17', '2021-12-17',
            '2022-01-21', '2022-03-18', '2022-06-17', '2022-09-16', '2023-01-20', '2023-03-17']


def get_option_type_list():
    return ['American', 'European']


def get_option_style_list():
    return ['Call', 'Put']


def get_data_source_list():
    return ['Yahoo', 'Other']


def get_itm_atm_otm_list():
    return ['itm+1', 'itm', 'atm', 'otm', 'otm+1']


def get_quantitative_analysis(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm):
    """
    returns the quantitative analysis 'outputs' as a dictionary
    """
    try:
        option = Option(tickerSymbol, expiration_date, option_style, option_type, data_source, itm_atm_otm)
    except RuntimeError:    # This exception is thrown when Option class parameters is invalid
        return None

    finalDict = {}
    riskFreeRate = option.get_riskFreeRate()
    currentUnderlyingPrice = option.get_currentPriceOfTheUnderlyingAsset()
    timeToExpiration = finalDict['Time-to-expiration']
    volatility = finalDict['Sigma']
    strike = finalDict['Strike']
    available_expirations = get_expiration_date_list()

    try:
        valuation = Valuation(40, tickerSymbol, riskFreeRate, currentUnderlyingPrice, strike, timeToExpiration, volatility, option_type, 50)
    except RuntimeError:    # This exception is thrown when Option class parameters is invalid
        return None

    # USER SELECTS PUT or CALL, USER SELECTS EXPIRATION, USER SELECTS ITMATMOTM
    # Once user selects expiration it narrows down the potential fields to five different itm_atm_otm = ['itm+1', 'itm', 'atm', 'otm', 'otm+1']


    DictCalls = {available_expirations[0]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[1]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[2]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[3]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[4]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[5]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[6]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[7]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[8]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[9]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                     'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                     'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                     'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                     'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[10]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[11]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[12]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[13]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[14]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[15]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}},
                 available_expirations[16]: {'ITM_Call': {'Strike': option.get_itm_call_strike(), "Time-to-expiration": option.get_itm_call_T, "Sigma": option.get_itm_call_sigma, 'OptionType': 'Call'},
                                      'OTM_Call': {'Strike': option.get_otm_call_strike(), "Time-to-expiration": option.get_otm_call_T, "Sigma": option.get_otm_call_sigma, 'OptionType': 'Call'},
                                      'ATM_Call': {'Strike': option.get_atm_call_strike(), "Time-to-expiration": option.get_atm_call_T, "Sigma": option.get_atm_call_sigma, 'OptionType': 'Call'},
                                      'ITM_Call+1': {'Strike': option.get_itm_call_minus_strike(), "Time-to-expiration": option.get_itm_call_minus_T, "Sigma": option.get_itm_call_minus_sigma, 'OptionType': 'Call'},
                                      'OTM_Call+1': {'Strike': option.get_otm_call_plus_strike(), "Time-to-expiration": option.get_otm_call_plus_T, "Sigma": option.get_otm_call_plus_sigma, 'OptionType': 'Call'}}}


    DictPuts = {available_expirations[0]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[1]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[2]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[3]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[4]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[5]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[6]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[7]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[8]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[9]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                    'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                    'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                    'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                    'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[10]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[11]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[12]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[13]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[14]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[15]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}},
                available_expirations[16]: {'ITM_Put': {'Strike': option.get_itm_put_strike(), "Time-to-expiration": option.get_itm_put_T, "Sigma": option.get_itm_put_sigma, 'OptionType': 'Put'},
                                     'OTM_Put': {'Strike': option.get_otm_put_strike(), "Time-to-expiration": option.get_otm_put_T, "Sigma": option.get_otm_put_sigma, 'OptionType': 'Put'},
                                     'ATM_Put': {'Strike': option.get_atm_put_strike(), "Time-to-expiration": option.get_atm_put_T, "Sigma": option.get_atm_put_sigma, 'OptionType': 'Put'},
                                     'ITM_Put+1': {'Strike': option.get_itm_put_minus_strike(), "Time-to-expiration": option.get_itm_put_minus_T, "Sigma": option.get_itm_put_minus_sigma, 'OptionType': 'Put'},
                                     'OTM_Put+1': {'Strike': option.get_otm_put_plus_strike(), "Time-to-expiration": option.get_otm_put_plus_T, "Sigma": option.get_otm_put_plus_sigma, 'OptionType': 'Put'}}}

    if option_type == "Call":
        finalDict = DictCalls[expiration_date][itm_atm_otm]

    elif option_type == "Put":
        finalDict = DictPuts[expiration_date][itm_atm_otm]

    chosenExpiration = expiration_date
    strikeMatchChosenExpiration = finalDict["Strike"]
    TmatchChosen = finalDict["Time-to-expiration"]
    sigmaMatchedChosen = finalDict["Sigma"]

    analysis = {
        "variables": {"risk_free_rate_r": riskFreeRate,
                      "underlying_s": currentUnderlyingPrice,
                      "chosen_expiration": chosenExpiration,
                      "strike_x": strikeMatchChosenExpiration,
                      "time_to_maturity_T": TmatchChosen,
                      "return_volatility": sigmaMatchedChosen,
                      "intrinsic_value": valuation.intrinsicValue(),
                      "speculative_premium": valuation.speculativePremium()},
        "valuations": {"black_scholes": valuation.blackScholes(),
                       "binomial": valuation.binomialModel(),
                       "average_price": valuation.monteCarloSimulation(),
                       "market_price": strikeMatchChosenExpiration(),
                       "implied_volatility": valuation.impliedVolatility()},
        "the_greeks": {"delta": valuation.delta(),
                       "gamma": valuation.gamma(),
                       "theta": valuation.theta(),
                       "vega": valuation.vega(),
                       "rho": valuation.rho(),
                       "charm": valuation.charm()}, }
    return analysis


#tickerSymbol, expirationDate, optionStyle, optionType, data_source, itmAtmOtm
#print(tickerSymbol, get_quantitative_analysis(get_expiration_date_list(), get_option_style_list(), get_option_type_list(), get_data_source_list(), get_itm_atm_otm_list()))




