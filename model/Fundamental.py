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
    url = ("https://financialmodelingprep.com/api/v3/ratios-ttm/" + ticker +
           "?apikey=" + api_key)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class Fundamental:

    def __init__(self, ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError
        # get the attributes of the underlying stock and check if they're valid
        try:
            # Stock ticker
            json_data = get_jsonparsed_data(ticker)
            # priceFairValueTTM for the underlying stock
            self.priceFairValueTTM = round(json_data[0]["priceFairValueTTM"], 2)
            # debtEquityRatioTTM for the underlying stock
            self.debtEquityRatioTTM = round(json_data[0]["debtEquityRatioTTM"], 2)
            # priceToBookRatioTTM for the underlying stock
            self.priceToBookRatioTTM = round(json_data[0]["priceToBookRatioTTM"], 2)
            # returnOnEquityTTM for the underlying stock
            self.returnOnEquityTTM = round(json_data[0]["returnOnEquityTTM"], 2)
            # priceEarningsToGrowthRatioTTM for the underlying stock
            self.priceEarningsToGrowthRatioTTM = round(json_data[0]["priceEarningsToGrowthRatioTTM"], 2)
            # returnOnAssetsTTM for the underlying stock
            self.returnOnAssetsTTM = round(json_data[0]["returnOnAssetsTTM"], 2)
            # returnOnCapitalEmployedTTM for the underlying stock
            self.returnOnCapitalEmployedTTM = round(json_data[0]["returnOnCapitalEmployedTTM"], 2)
            # currentRatioTTM for the underlying stock
            self.currentRatioTTM = round(json_data[0]["currentRatioTTM"], 2)

        except Exception as err:
            # if exception is thrown this is because the api cannot fetch information from this stock and we have to return empty value
            self.priceFairValueTTM = None
            self.debtEquityRatioTTM = None
            self.priceToBookRatioTTM = None
            self.returnOnEquityTTM = None
            self.priceEarningsToGrowthRatioTTM = None
            self.returnOnAssetsTTM = None
            self.returnOnCapitalEmployedTTM = None
            self.currentRatioTTM = None

    def get_priceFairValueTTM(self):
        """
        returns the price fair value TTM of the company
        """
        return self.priceFairValueTTM

    def get_debtEquityRatioTTM(self):
        """
        returns the debt equity ratio TTM of the company
        """
        return self.debtEquityRatioTTM

    def get_priceToBookRatioTTM(self):
        """
        returns the price to book ratio TTM of the company
        """
        return self.priceToBookRatioTTM

    def get_returnOnEquityTTM(self):
        """
        returns the return on equity TTM of the company
        """
        return self.returnOnEquityTTM

    def get_priceEarningsToGrowthRatioTTM(self):
        """
        returns the price earnings to growth ratio TTM of the company
        """
        return self.priceEarningsToGrowthRatioTTM

    def get_returnOnAssetsTTM(self):
        """
        returns the return on assets TTM of the company
        """
        return self.returnOnAssetsTTM

    def get_returnOnCapitalEmployedTTM(self):
        """
        returns the return on capital employed TTM of the company
        """
        return self.returnOnCapitalEmployedTTM

    def get_currentRatioTTM(self):
        """
        returns the current ratio TTM of the company
        """
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
