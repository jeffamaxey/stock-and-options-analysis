from model.Option import Option
from model.Valuation import Valuation
import yfinance as yf

########################################################################
#user clicks expiration than the ITMATMOTM shows (5 market prices) the 2 closest ITM and 2 closest OTM Strike Prices as well as ATM price
#Each expiration will be the ID, each expiration will have 2-ITM 1-ATM 2-OTM associated with it giving results for (strike, T, & sigma)
########################################################################
#strike impliedVolatility expirationDate    T   optionType
# (ITM Call) if the currentPriceOfTheUnderlyingAsset > Strike Price of the call option
# (ATM Call) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (OTM Call) if the Call strike price is > the the current price of the underlying asset
# (OTM Put) if the Put strike price is < the current price of the underlying asset
# (ATM Put) if the currentPriceOfTheUnderlyingAsset = Strike Price of the option
# (ITM Put) if the currentPriceOfTheUnderlyingAsset < Strike Price of the put option

##### IN Option.py
##### NEED TO UPDATE LINES IN OPTION.PY SO-> if dic[key]==value and dic['CALL'] == True and dic['expirationDate'] == self.chosenExpiration
##### NEED TO UPDATE LINES IN OPTION.PY So user selects the restraint of an expiration date


def get_ticker_symbol(tickerSymbol):
    ticker = yf.Ticker(tickerSymbol)
    return ticker


# Adjust in the future as needed
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
        ticker = tickerSymbol
    except RuntimeError:    # This exception is thrown when ticker is invalid
        return None

    finalDict = {}
    option = Option(tickerSymbol)

    try:
        expirationDate = expiration_date
        optionStyle = option_style
        itmAtmOtm = itm_atm_otm
    except RuntimeError:    # This exception is thrown when the expiration, style or itm_atm_otm_strike is invalid
        return None

    optionType = option_type
    dataSource = data_source
    riskFreeRate = option.get_riskFreeRate()
    currentUnderlyingPrice = option.get_currentPriceOfTheUnderlyingAsset()
    timeToExpiration = finalDict['Time-to-expiration']
    volatility = finalDict['Sigma']
    strike = finalDict['Strike']
    #option_chain = option.get_entire_sorted_options_chain()

    # FIRST TICKER PARAMETER MIGHT BE WRONG
    # N, ticker, r, s, x, T, sigma, optionType, iterations
    valuation = Valuation(40, tickerSymbol, riskFreeRate, currentUnderlyingPrice, strike, timeToExpiration, volatility, optionType, 50)

    # USER SELECTS PUT or CALL, USER SELECTS EXPIRATION, USER SELECTS ITMATMOTM
    # Once user selects expiration it narrows down the potential fields to five different itmAtmOtm = ['itm+1', 'itm', 'atm', 'otm', 'otm+1']
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
    #if optionType == "Call":
        #step = DictCalls
    #elif optionType == "Put":
        #step = DictPuts
    #for x in step:
        #ITMATMOTM = step[x][0]+step[x][1]+step[x][2]+step[x][3]+step[x][4]
        #if step[x] == expirationDate[x]:
            #return expirationDate[x]
        #x += 1

    # NOT SURE IF THIS WORKS
    #ITMATMOTM = {}
    #for i, dic in enumerate(ITMATMOTM):
        #return ITMATMOTM == ITMATMOTM[i]
    #strike = ITMATMOTM[0]


    #print(finalDict)
    #chosenExpiration = expirationDate
    #strikeMatchChosenExpiration = chosenExpiration
    #TmatchChosen = chosenExpiration
    #sigmaMatchedChosen = chosenExpiration

    analysis = {
        "variables": {"risk_free_rate_r": riskFreeRate,
                      "underlying_s": currentUnderlyingPrice,
                      #"chosen_expiration": chosenExpiration,
                      #"strike_x": strikeMatchChosenExpiration,
                      #"time_to_maturity_T": TmatchChosen,
                      #"return_volatility": sigmaMatchedChosen,
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


#tickerSymbol, expirationDate, optionStyle, optionType, data_source, itmAtmOtm
#print(get_quantitative_analysis(get_ticker_symbol("TSLA"), get_expiration_date_list(get_ticker_symbol("TSLA")), get_option_style_list(), get_option_type_list(), get_data_source_list(), get_itm_atm_otm_list()))




