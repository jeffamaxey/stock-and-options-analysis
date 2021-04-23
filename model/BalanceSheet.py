"""
Author: Ramtin Mahdavifar
"""
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
    def __init__(self, ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError
        # get the attributes of the underlying stock and check if they're valid
        try:
            # ticker for the underlying stock
            json_data = get_jsonparsed_data(ticker)
            # totalCurrentAssets for the underlying stock
            self._totalCurrentAssets = round(json_data[0]["totalCurrentAssets"], 2)
            # totalNonCurrentAssets for the underlying stock
            self._totalNonCurrentAssets = round(json_data[0]["totalNonCurrentAssets"], 2)
            # totalAssets for the underlying stock
            self._totalAssets = round(json_data[0]["totalAssets"], 2)
            # totalCurrentLiabilities for the underlying stock
            self._totalCurrentLiabilities = round(json_data[0]["totalCurrentLiabilities"], 2)
            # totalNonCurrentLiabilities for the underlying stock
            self._totalNonCurrentLiabilities = round(json_data[0]["totalNonCurrentLiabilities"], 2)
            # totalLiabilities for the underlying stock
            self._totalLiabilities = round(json_data[0]["totalLiabilities"], 2)
            # totalStockholdersEquity for the underlying stock
            self._totalStockholdersEquity = round(json_data[0]["totalStockholdersEquity"], 2)
            # totalLiabilitiesAndStockholdersEquity for the underlying stock
            self._totalLiabilitiesAndStockholdersEquity = round(json_data[0]["totalLiabilitiesAndStockholdersEquity"], 2)

        except Exception as err:
            # if exception is thrown this is because the api cannot fetch information from this stock and we have to return empty value
            self._totalCurrentAssets = None
            self._totalNonCurrentAssets = None
            self._totalAssets = None
            self._totalCurrentLiabilities = None
            self._totalNonCurrentLiabilities = None
            self._totalLiabilities = None
            self._totalStockholdersEquity = None
            self._totalLiabilitiesAndStockholdersEquity = None

    def get_totalCurrentAssets(self):
        """
        returns the total current assets of the company
        """
        return self._totalCurrentAssets

    def get_totalNonCurrentAssets(self):
        """
        returns the total non_current assets of the company
        """
        return self._totalNonCurrentAssets

    def get_totalAssets(self):
        """
        returns the total_assets of the company
        """
        return self._totalAssets

    def get_totalCurrentLiabilities(self):
        """
        returns the total_current_liabilities of the company
        """
        return self._totalCurrentLiabilities

    def get_totalNonCurrentLiabilities(self):
        """
        returns the total non_current liabilities of the company
        """
        return self._totalNonCurrentLiabilities

    def get_totalLiabilities(self):
        """
        returns the total liabilities of the company
        """
        return self._totalLiabilities

    def get_totalStockholdersEquity(self):
        """
        returns the total StockholdersEquity of the company
        """
        return self._totalStockholdersEquity

    def get_totalLiabilitiesAndStockholdersEquity(self):
        """
        returns the total LiabilitiesAndStockholdersEquity of the company
        """
        return self._totalLiabilitiesAndStockholdersEquity
