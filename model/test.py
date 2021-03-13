import ValidTicker
import json
from urllib.request import urlopen

# api key obtained from https://financialmodelingprep.com/developer/docs/
api_key = "ef50942d7567387062ceb4e67b4da6cb"
ticker = str(input("Ticker: "))
ticker = ticker.upper()
url = ("https://financialmodelingprep.com/api/v3/ratios-ttm/" + ticker +
       "?apikey=" + api_key)


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.
    Parameters
    ----------
    url : str
    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class Fundamental:
    def __init__(self):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError
        self.priceFairValueTTM = get_jsonparsed_data(url)[0]["priceFairValueTTM"]
        self.debtEquityRatioTTM = get_jsonparsed_data(url)[0]["debtEquityRatioTTM"]
        self.priceToBookRatioTTM = get_jsonparsed_data(url)[0]["priceToBookRatioTTM"]
        self.returnOnEquityTTM = get_jsonparsed_data(url)[0]["returnOnEquityTTM"]
        self.priceEarningsToGrowthRatioTTM = get_jsonparsed_data(url)[0]["priceEarningsToGrowthRatioTTM"]
        self.returnOnAssetsTTM = get_jsonparsed_data(url)[0]["returnOnAssetsTTM"]
        self.returnOnCapitalEmployedTTM = get_jsonparsed_data(url)[0]["returnOnCapitalEmployedTTM"]
        self.currentRatioTTM = get_jsonparsed_data(url)[0]["currentRatioTTM"]

    def get_priceFairValueTTM(self):
        return self.priceFairValueTTM

    def get_debtEquityRatioTTM(self):
        return self.debtEquityRatioTTM

    def get_priceToBookRatioTTM(self):
        return self.priceToBookRatioTTM

    def get_returnOnEquityTTM(self):
        return self.returnOnEquityTTM

    def get_priceEarningsToGrowthRatioTTM(self):
        return self.priceEarningsToGrowthRatioTTM

    def get_returnOnAssetsTTM(self):
        return self.returnOnAssetsTTM

    def get_returnOnCapitalEmployedTTM(self):
        return self.returnOnCapitalEmployedTTM

    def get_currentRatioTTM(self):
        return self.currentRatioTTM


test1 = Fundamental()
print(test1.get_priceFairValueTTM())
print(test1.get_debtEquityRatioTTM())
print(test1.get_priceToBookRatioTTM())
print(test1.get_returnOnEquityTTM())
print(test1.get_priceEarningsToGrowthRatioTTM())
print(test1.get_returnOnAssetsTTM())
print(test1.get_returnOnCapitalEmployedTTM())
print(test1.get_currentRatioTTM())
