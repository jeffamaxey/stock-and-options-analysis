from model import Stock
import csv

class exportToCSV:
    def __init__(self, object):
        self._stock = None
        self._valuation = None
        # checking if the passed in object is actually equivalent to a Stock.Stock type
        if type(object) == Stock.Stock:
            self._stock = object
            exportToCSV.exportFundamental(self)

    def exportFundamental(self):
        """
        This class exports the Fundamentals (Fundamental Ratios, Balance sheet, Income Statement, and Cash Flow) of a
        company into a csv file
        """
        # create a new csv file and enable writing
        with open("view/static/export/Fundamental.csv", "w", newline='') as f:
            # headers for Fundamental Ratios
            headers = ['Fundamental Ratios', 'priceFairValueTTM', 'debtEquityRatioTTM', 'priceToBookRatioTTM',
                       'returnOnEquityTTM', 'priceEarningsToGrowthRatioTTM', 'returnOnAssetsTTM',
                       'returnOnCapitalEmployedTTM', 'currentRatioTTM']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            # writing the data to a csv for Fundamental Ratios
            writer.writerow({"Fundamental Ratios": '',
                             'priceFairValueTTM': str(self._stock.get_fundamental().get_priceFairValueTTM()),
                             'debtEquityRatioTTM': str(self._stock.get_fundamental().get_debtEquityRatioTTM()),
                             'priceToBookRatioTTM': str(self._stock.get_fundamental().get_priceToBookRatioTTM()),
                             'returnOnEquityTTM': str(self._stock.get_fundamental().get_returnOnEquityTTM()),
                             'priceEarningsToGrowthRatioTTM': str(self._stock.get_fundamental().get_priceEarningsToGrowthRatioTTM()),
                             'returnOnAssetsTTM': str(self._stock.get_fundamental().get_returnOnAssetsTTM()),
                             'returnOnCapitalEmployedTTM': str(self._stock.get_fundamental().get_returnOnCapitalEmployedTTM()),
                             'currentRatioTTM': str(self._stock.get_fundamental().get_currentRatioTTM())})
            # writing a newline for formatting purposes
            writer.writerow({})
            headers = ['Balance Sheet', 'totalCurrentAssets', 'totalNonCurrentAssets',
                       'totalAssets', 'totalCurrentLiabilities', 'totalNonCurrentLiabilities', 'totalLiabilities',
                       'totalStockholdersEquity', 'totalLiabilitiesAndStockholdersEquity']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            # writing the data to a csv for Balance Sheet
            writer.writerow({"Balance Sheet": '',
                             'totalCurrentAssets': str(self._stock.get_balance_sheet().get_totalCurrentAssets()),
                             'totalNonCurrentAssets': str(self._stock.get_balance_sheet().get_totalNonCurrentAssets()),
                             'totalAssets': str(self._stock.get_balance_sheet().get_totalAssets()),
                             'totalCurrentLiabilities': str(self._stock.get_balance_sheet().get_totalCurrentLiabilities()),
                             'totalNonCurrentLiabilities': str(self._stock.get_balance_sheet().get_totalNonCurrentLiabilities()),
                             'totalLiabilities': str(self._stock.get_balance_sheet().get_totalLiabilities()),
                             'totalStockholdersEquity': str(self._stock.get_balance_sheet().get_totalStockholdersEquity()),
                             'totalLiabilitiesAndStockholdersEquity': str(self._stock.get_balance_sheet().get_totalLiabilitiesAndStockholdersEquity())})
            # writing a newline for formatting purposes
            writer.writerow({})
            headers = ['Income Statement', 'revenue', 'ebitda', 'incomeTaxExpense',
                       'netIncome', 'grossProfit']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            # writing the data to a csv for Income statement
            writer.writerow({"Income Statement": '',
                             'revenue': str(self._stock.get_income_statement().getRevenue()),
                             'ebitda': str(self._stock.get_income_statement().getEbitda()),
                             'incomeTaxExpense': str(self._stock.get_income_statement().getIncomeTaxExpense()),
                             'netIncome': str(self._stock.get_income_statement().getNetIncome()),
                             'grossProfit': str(self._stock.get_income_statement().getGrossProfit())})
            # writing a newline for formatting purposes
            writer.writerow({})
            headers = ['Cash Flow', 'netCashProvidedByOperatingActivities', 'netCashUsedForInvestingActivites',
                       'netCashUsedProvidedByFinancingActivities', 'freeCashFlow']
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            # writing the data to a csv for Cash Flow
            writer.writerow({"Cash Flow": '',
                             'netCashProvidedByOperatingActivities': str(self._stock.get_cash_flow().getNetCashProvidedByOperatingActivities()),
                             'netCashUsedForInvestingActivites': str(self._stock.get_cash_flow().getNetCashUsedForInvestingActivites()),
                             'netCashUsedProvidedByFinancingActivities': str(self._stock.get_cash_flow().getNetCashUsedProvidedByFinancingActivities()),
                             'freeCashFlow': str(self._stock.get_cash_flow().getFreeCashFlow())})

# for testing purposes
# e = exportToCSV(Stock.Stock("PRTS"))
# e.exportFundamental()
