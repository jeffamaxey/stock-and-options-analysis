from model.Stock import Stock
import time

# testing for a ultra cap stock
ticker = "AAPL"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_cash_flow(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve AAPL stock data in seconds = " + str(t2 - t1))
# testing if all the values retrieved are equivalent to the ratios in financial statements of apple
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements
if stock1.getNetCashProvidedByOperatingActivities() != 143713000000:
    print("Error: AAPL stock getNetCashProvidedByOperatingActivities() method is incorrect and does not equal 143713000000 as shown in sec.gov, "
          "current value is " + str(stock1.getNetCashProvidedByOperatingActivities()))

if stock1.getNetCashUsedForInvestingActivites() != 180175000000:
    print("Error: AAPL stock getNetCashUsedForInvestingActivites() method is incorrect and does not equal 180175000000 as shown in sec.gov, "
          "current value is " + str(stock1.getNetCashUsedForInvestingActivites()))

if stock1.getNetCashUsedProvidedByFinancingActivities() != 323888000000:
    print("Error: AAPL stock getNetCashUsedProvidedByFinancingActivities() method is incorrect and does not equal 323888000000 as shown in sec.gov, "
          "current value is " + str(stock1.getNetCashUsedProvidedByFinancingActivities()))

if stock1.getFreeCashFlow() != 105392000000:
    print("Error: AAPL stock getFreeCashFlow() method is incorrect and does not equal 105392000000 as shown in sec.gov, "
          "current value is " + str(stock1.getFreeCashFlow()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of carparts.com
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a small cap stock
ticker = "PRTS"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_cash_flow(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve PRTS stock data in seconds = " + str(t2 - t1))
if stock1.get_totalCurrentAssets() != 62373000:
    print("Error: PRTS stock get_totalCurrentAssets() method is incorrect and does not equal 62373000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalCurrentAssets()))

if stock1.get_totalNonCurrentAssets() != 25573000:
    print("Error: PRTS stock get_totalNonCurrentAssets() method is incorrect and does not equal 25573000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalNonCurrentAssets()))

if stock1.get_totalAssets() != 87946000:
    print("Error: PRTS stock get_totalAssets() method is incorrect and does not equal 87946000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalAssets()))

if stock1.get_totalCurrentLiabilities() != 59946000:
    print("Error: PRTS stock get_totalCurrentLiabilities() method is incorrect and does not equal 59946000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalCurrentLiabilities()))

if stock1.get_totalNonCurrentLiabilities() != 15620000:
    print("Error: PRTS stock get_totalNonCurrentLiabilities() method is incorrect and does not equal 15620000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalNonCurrentLiabilities()))

if stock1.get_totalLiabilities() != 75566000:
    print("Error: PRTS stock get_totalLiabilities() method is incorrect and does not equal 75566000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalLiabilities()))

if stock1.get_totalStockholdersEquity() != 12380000:
    print("Error: PRTS stock get_totalStockholdersEquity() method is incorrect and does not equal 12380000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalStockholdersEquity()))

if stock1.get_totalLiabilitiesAndStockholdersEquity() != 87946000:
    print("Error: PRTS stock get_totalLiabilitiesAndStockholdersEquity() method is incorrect and does not equal 1.9 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalLiabilitiesAndStockholdersEquity()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of Cabot Microelectronics
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a medium cap stock
ticker = "CCMP"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_balance_sheet(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve CCMP stock data in seconds = " + str(t2 - t1))
if stock1.get_totalCurrentAssets() != 577069000:
    print("Error: CCMP stock get_totalCurrentAssets() method is incorrect and does not equal None as shown in sec.gov, "
          "current value is " + str(stock1.get_totalCurrentAssets()))

if stock1.get_totalNonCurrentAssets() != 1799398000:
    print("Error: CCMP stock get_totalNonCurrentAssets() method is incorrect and does not equal 1799398000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalNonCurrentAssets()))

if stock1.get_totalAssets() != 2376467000:
    print(
        "Error: CCMP stock get_totalAssets() method is incorrect and does not equal 2376467000 as shown in sec.gov, "
        "current value is " + str(stock1.get_totalAssets()))

if stock1.get_totalCurrentLiabilities() != 181346000:
    print("Error: CCMP stock get_totalCurrentLiabilities() method is incorrect and does not equal 181346000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalCurrentLiabilities()))

if stock1.get_totalNonCurrentLiabilities() != 1120808000:
    print(
        "Error: CCMP stock get_totalNonCurrentLiabilities() method is incorrect and does not equal 1120808000 as shown in sec.gov, "
        "current value is " + str(stock1.get_totalNonCurrentLiabilities()))

if stock1.get_totalLiabilities() != 1302154000:
    print("Error: CCMP stock get_totalLiabilities() method is incorrect and does not equal 1302154000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalLiabilities()))

if stock1.get_totalStockholdersEquity() != 1074313000:
    print(
        "Error: CCMP stock get_totalStockholdersEquity() method is incorrect and does not equal 1074313000 as shown in sec.gov, "
        "current value is " + str(stock1.get_totalStockholdersEquity()))

if stock1.get_totalLiabilitiesAndStockholdersEquity() != 2376467000:
    print("Error: CCMP stock get_totalLiabilitiesAndStockholdersEquity() method is incorrect and does not equal 2376467000 as shown in sec.gov, "
          "current value is " + str(stock1.get_totalLiabilitiesAndStockholdersEquity()))
