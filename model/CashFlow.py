import json
from urllib.request import urlopen
import ValidTicker



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
    url = ("https://financialmodelingprep.com/api/v3/cash-flow-statement/" + ticker +
           "?period=quarter&limit=400&apikey=" + api_key)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class CashFlow:
    def __init__(self,ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError

        json_data = get_jsonparsed_data(ticker)

        self.netCashProvidedByOperatingActivities = json_data[0]["netCashProvidedByOperatingActivities"]
        self.netCashUsedForInvestingActivites = json_data[0]["netCashUsedForInvestingActivites"]
        self.netCashUsedProvidedByFinancingActivities = json_data[0]["netCashUsedProvidedByFinancingActivities"]
        self.freeCashFlow = json_data[0]["freeCashFlow"]

    def getNetCashProvidedByOperatingActivities(self):
        return self.netCashProvidedByOperatingActivities

    def getNetCashUsedForInvestingActivites(self):
        return self.netCashUsedForInvestingActivites

    def getNetCashUsedProvidedByFinancingActivities(self):
        return self.netCashUsedProvidedByFinancingActivities

    def getFreeCashFlow(self):
        return self.freeCashFlow


# test1 = CashFlow()
# print(test1.getNetCashProvidedByOperatingActivities())
# print(test1.getNetCashUsedForInvestingActivites())
# print(test1.getNetCashUsedProvidedByFinancingActivities())
# print(test1.getFreeCashFlow())
