import ValidTicker
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
    url = ("https://financialmodelingprep.com/api/v3/ratios-ttm/" + ticker +
           "?apikey=" + api_key)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class Fundamental:

    def __init__(self, ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError

        json_data = get_jsonparsed_data(ticker)

        self.priceFairValueTTM = json_data[0]["priceFairValueTTM"]
        self.debtEquityRatioTTM = json_data[0]["debtEquityRatioTTM"]
        self.priceToBookRatioTTM = json_data[0]["priceToBookRatioTTM"]
        self.returnOnEquityTTM = json_data[0]["returnOnEquityTTM"]
        self.priceEarningsToGrowthRatioTTM = json_data[0]["priceEarningsToGrowthRatioTTM"]
        self.returnOnAssetsTTM = json_data[0]["returnOnAssetsTTM"]
        self.returnOnCapitalEmployedTTM = json_data[0]["returnOnCapitalEmployedTTM"]
        self.currentRatioTTM = json_data[0]["currentRatioTTM"]

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

# test1 = Fundamental("aapl")
# print(test1.get_priceFairValueTTM())
# print(test1.get_debtEquityRatioTTM())
# print(test1.get_priceToBookRatioTTM())
# print(test1.get_returnOnEquityTTM())
# print(test1.get_priceEarningsToGrowthRatioTTM())
# print(test1.get_returnOnAssetsTTM())
# print(test1.get_returnOnCapitalEmployedTTM())
# print(test1.get_currentRatioTTM())
