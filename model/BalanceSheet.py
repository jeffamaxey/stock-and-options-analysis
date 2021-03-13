from model import ValidTicker
import json
from urllib.request import urlopen


def get_jsonparsed_data(ticker):
    """
    Receive the content of ``url``, parse it as JSON and return the object.
    Parameters
    ----------
    url : str
    Returns
    -------
    dict
    """
    # api key obtained from https://financialmodelingprep.com/developer/docs/
    api_key = "ef50942d7567387062ceb4e67b4da6cb"
    ticker = ticker.upper()
    url = ("https://financialmodelingprep.com/api/v3/balance-sheet-statement/" + ticker +
           "?limit=120&apikey=" + api_key)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class BalanceSheet:
    """
    The balance sheet of the company
    """
    def __init__(self,ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError

        json_data = get_jsonparsed_data(ticker)

        self.totalCurrentAssets = json_data [0]["totalCurrentAssets"]
        self.totalNonCurrentAssets = json_data [0]["totalNonCurrentAssets"]
        self.totalAssets = json_data [0]["totalAssets"]
        self.totalCurrentLiabilities = json_data [0]["totalCurrentLiabilities"]
        self.totalNonCurrentLiabilities = json_data [0]["totalNonCurrentLiabilities"]
        self.totalLiabilities = json_data [0]["totalLiabilities"]
        self.totalStockholdersEquity = json_data [0]["totalStockholdersEquity"]
        self.totalLiabilitiesAndStockholdersEquity = json_data [0]["totalLiabilitiesAndStockholdersEquity"]

    def get_totalCurrentAssets(self):
        return self.totalCurrentAssets

    def get_totalNonCurrentAssets(self):
        return self.totalNonCurrentAssets

    def get_totalAssets(self):
        return self.totalAssets

    def get_totalCurrentLiabilities(self):
        return self.totalCurrentLiabilities

    def get_totalNonCurrentLiabilities(self):
        return self.totalNonCurrentLiabilities

    def get_totalLiabilities(self):
        return self.totalLiabilities

    def get_totalStockholdersEquity(self):
        return self.totalStockholdersEquity

    def get_totalLiabilitiesAndStockholdersEquity(self):
        return self.totalLiabilitiesAndStockholdersEquity
