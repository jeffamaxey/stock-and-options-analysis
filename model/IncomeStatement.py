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
    url = ("https://financialmodelingprep.com/api/v3/income-statement/" + ticker +
           "?period=quarter&limit=400&apikey=" + api_key)

    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class IncomeStatement:
    def __init__(self, ticker):
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError
        # get the attributes of the underlying stock and check if they're valid
        try:
            #Stock ticker
            json_data = get_jsonparsed_data(ticker)
            # revenue for the underlying stock
            self.revenue = json_data[0]["revenue"]
            # ebitda for the underlying stock
            self.ebitda = json_data[0]["ebitda"]
            # incomeTaxExpense for the underlying stock
            self.incomeTaxExpense = json_data[0]["incomeTaxExpense"]
            # netIncome for the underlying stock
            self.netIncome = json_data[0]["netIncome"]
            # grossProfit for the underlying stock
            self.grossProfit = json_data[0]["grossProfit"]

        except Exception as err:
            # if exception is thrown this is because the api cannot fetch information from this stock and we have to return empty value
            self.revenue = None
            self.ebitda = None
            self.incomeTaxExpense = None
            self.netIncome = None
            self.grossProfit = None

    def getRevenue(self):
        """
        returns the revenue of the company
        """
        return self.revenue

    def getEbitda(self):
        """
        returns the EBITDA of the company
        """
        return self.ebitda

    def getIncomeTaxExpense(self):
        """
        returns the income tax expense of the company
        """
        return self.incomeTaxExpense

    def getNetIncome(self):
        """
        returns the net income of the company
        """
        return self.netIncome

    def getGrossProfit(self):
        """
        returns the gross profit of the company
        """
        return self.grossProfit

# test1 = IncomeStatement("AAPL")
# print(test1.getRevenue())
# print(test1.getEbitda())
# print(test1.getIncomeTaxExpense())
# print(test1.getNetIncome())
# print(test1.getGrossProfit())
