import requests


def get_ticker_company(ticker):
    """
    Get the company name of the ticker symbol
    :param ticker is the ticker symbol to get the company name
    :throws a ProcessLookupError exception if a company name of a ticker is not found
    :return a string of the company name
    """
    # call the yahoo finance api and store the stock information as json into result list
    ticker = ticker.upper()
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    result = requests.get(url).json()

    # go through the list and see if the ticker symbol is found and if so return the name of the company
    for x in result['ResultSet']['Result']:
        if x['symbol'] == ticker:
            return x['name']

    # if the company name is not found then a ProcessLookupError exception is thrown
    raise ProcessLookupError('company name of stock not found')


def valid_ticker(ticker):
    """
    Check whether given ticker is a valid stock symbol.
    We assume that the ticker is valid if yahoo finance can return a stock for the ticker

    :param ticker is the ticker symbol to check if it is a valid stock
    :return a boolean true or false if the stock is a valid ticker
    """
    try:
        # try to get the company name of the ticker and if an exception is not thrown then return true
        get_ticker_company(ticker)
        return True

    except ProcessLookupError as err:
        # exception thrown so the ticker is invalid and we return false
        return False

    # print(get_ticker_company("sklz"))
    # print(valid_ticker("nasdgfs"))
    # print(valid_ticker("stpk"))
