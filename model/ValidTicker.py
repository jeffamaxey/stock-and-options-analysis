import requests


def get_ticker_company(ticker):
    """
<<<<<<< model/ValidTicker.py
    Get the company name of the _ticker tickerSymbol
    :param ticker is the _ticker tickerSymbol to get the company name
    :throws a ProcessLookupError exception if a company name of a _ticker is not found
=======
    Get the company name of the ticker symbol
    :param ticker is the ticker symbol to get the company name
    :throws a ProcessLookupError exception if a company name of a ticker is not found
>>>>>>> model/ValidTicker.py
    :return a string of the company name
    """
    # call the yahoo finance api and store the stock information as json into result list
    # some of the code for get_ticker_company is borrowed from https://stackoverflow.com/questions/38967533/retrieve-company-name-with-ticker-symbol-input-yahoo-or-google-api
    ticker = ticker.upper()
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    result = requests.get(url).json()

<<<<<<< model/ValidTicker.py
    # go through the list and see if the _ticker tickerSymbol is found and if so return the name of the company
    #for x in result['ResultSet']['Result']:
        #if x['tickerSymbol'] == ticker:
=======
    # go through the list and see if the ticker symbol is found and if so return the name of the company
    for x in result['ResultSet']['Result']:
        if x['symbol'] == ticker:
>>>>>>> model/ValidTicker.py
            return x['name']

    # if the company name is not found then a ProcessLookupError exception is thrown
    raise ProcessLookupError('company name of stock not found')


def valid_ticker(ticker):
    """
<<<<<<< model/ValidTicker.py
    Check whether given _ticker is a valid stock tickerSymbol.
    We assume that the _ticker is valid if yahoo finance can return a stock for the _ticker

    :param ticker is the _ticker tickerSymbol to check if it is a valid stock
    :return a boolean true or false if the stock is a valid _ticker
    """
    try:
        # try to get the company name of the _ticker and if an exception is not thrown then return true
=======
    Check whether given ticker is a valid stock symbol.
    We assume that the ticker is valid if yahoo finance can return a stock for the ticker

    :param ticker is the ticker symbol to check if it is a valid stock
    :return a boolean true or false if the stock is a valid ticker
    """
    try:
        # try to get the company name of the ticker and if an exception is not thrown then return true
>>>>>>> model/ValidTicker.py
        get_ticker_company(ticker)
        return True

    except ProcessLookupError as err:
<<<<<<< model/ValidTicker.py
        # exception thrown so the _ticker is invalid and we return false
        return False

    # print(get_ticker_company("sklz"))
    # print(valid_ticker("nasdgfs"))
    # print(valid_ticker("stpk"))
=======
        # exception thrown so the ticker is invalid and we return false
        return False


def get_exchange(ticker):
    """
    Get the stock exchange of the ticker
    Currently works with NYSE and Nasdaq
    :param ticker is the ticker symbol to get the exchange
    :throws a ProcessLookupError exception if a exchange name of a ticker is not found
    :return a string of the stock exchange
    """
    # call the yahoo finance api and store the stock information as json into result list
    # some of the code for get_exchange is borrowed from https://stackoverflow.com/questions/38967533/retrieve-company-name-with-ticker-symbol-input-yahoo-or-google-api
    ticker = ticker.upper()
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    result = requests.get(url).json()

    # go through the list and return stock exchange of stock
    for x in result['ResultSet']['Result']:
        if x['symbol'] == ticker:
            exchange = x["exch"]
            if exchange == "NYS":
                return "NYSE"
            if exchange == "NMS" or "NAS":
                return "NASDAQ"

            return exchange

    # if the exchange name is not found then a ProcessLookupError exception is thrown
    raise ProcessLookupError('exchange of stock not found')

# print(get_exchange("goog"))
>>>>>>> model/ValidTicker.py
