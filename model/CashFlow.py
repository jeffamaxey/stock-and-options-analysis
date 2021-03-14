import json
from urllib.request import urlopen
from model import ValidTicker


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
        # get the attributes of the underlying stock and check if they're valid
        try:
            json_data = get_jsonparsed_data(ticker)
            self.netCashProvidedByOperatingActivities = round(json_data[0]["netCashProvidedByOperatingActivities"], 2)
            self.netCashUsedForInvestingActivites = round(json_data[0]["netCashUsedForInvestingActivites"], 2)
            self.netCashUsedProvidedByFinancingActivities = round(json_data[0]["netCashUsedProvidedByFinancingActivities"], 2)
            self.freeCashFlow = round(json_data[0]["freeCashFlow"], 2)

        except Exception as err:
            # if exception is thrown this is because the api cannot fetch information from this stock and we have to return empty value
            self.netCashProvidedByOperatingActivities = None
            self.netCashUsedForInvestingActivites = None
            self.netCashUsedProvidedByFinancingActivities = None
            self.freeCashFlow = None

    def getNetCashProvidedByOperatingActivities(self):
        """
        returns the Net Cash Provided By Operating Activities of the company
        """
        return self.netCashProvidedByOperatingActivities

    def getNetCashUsedForInvestingActivites(self):
        """
        returns the Net Cash used By investing Activities of the company
        """
        return self.netCashUsedForInvestingActivites

    def getNetCashUsedProvidedByFinancingActivities(self):
        """
        returns the Net Cash used provided By financing Activities of the company
        """
        return self.netCashUsedProvidedByFinancingActivities

    def getFreeCashFlow(self):
        """
        returns the free Cash flow of the company
        """
        return self.freeCashFlow

#
# test1 = CashFlow("AAPL")
# print(test1.getNetCashProvidedByOperatingActivities())
# print(test1.getNetCashUsedForInvestingActivites())
# print(test1.getNetCashUsedProvidedByFinancingActivities())
# print(test1.getFreeCashFlow())
