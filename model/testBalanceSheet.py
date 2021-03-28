from model.Stock import Stock
import time


def main():
    # testing for a ultra cap stock
    ticker = "AAPL"
    # begin timer for execution
    t1 = time.time()
    stock1 = Stock.get_balance_sheet(Stock(ticker))
    # end timer for execution
    t2 = time.time()
    print("Time to retrieve AAPL stock data in seconds = " + str(t2 - t1))
    # testing if all the values retrieved are equivalent to the ratios in financial statements of apple
    # all these numbers are gotten from sec.gov where one can view the papers of public financial statements
    if stock1.get_totalCurrentAssets() != 143713000000:
        print("Error: AAPL stock get_totalCurrentAssets() method is incorrect and does not equal 143713000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalCurrentAssets()))

    if stock1.get_totalNonCurrentAssets() != 180175000000:
        print("Error: AAPL stock get_totalNonCurrentAssets() method is incorrect and does not equal 180175000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalNonCurrentAssets()))

    if stock1.get_totalAssets() != 323888000000:
        print("Error: AAPL stock get_totalAssets() method is incorrect and does not equal 323888000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalAssets()))

    if stock1.get_totalCurrentLiabilities() != 105392000000:
        print("Error: AAPL stock get_totalCurrentLiabilities() method is incorrect and does not equal 105392000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalCurrentLiabilities()))

    if stock1.get_totalNonCurrentLiabilities() != 153157000000:
        print("Error: AAPL stock get_totalNonCurrentLiabilities() method is incorrect and does not equal 153157000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalNonCurrentLiabilities()))

    if stock1.get_totalLiabilities() != 258549000000:
        print("Error: AAPL stock get_totalLiabilities() method is incorrect and does not equal 258549000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalLiabilities()))

    if stock1.get_totalStockholdersEquity() != 65339000000:
        print("Error: AAPL stock get_totalStockholdersEquity() method is incorrect and does not equal 65339000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalStockholdersEquity()))

    if stock1.get_totalLiabilitiesAndStockholdersEquity() != 323888000000:
        print("Error: AAPL stock get_totalLiabilitiesAndStockholdersEquity() method is incorrect and does not equal 323888000000 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalLiabilitiesAndStockholdersEquity()))

    # testing if all the values retrieved are equivalent to the ratios in financial statements of carparts.com
    # all these numbers are gotten from sec.gov where one can view the papers of public financial statements

    # testing for a small cap stock
    ticker = "PRTS"
    # begin timer for execution
    t1 = time.time()
    stock1 = Stock.get_balance_sheet(Stock(ticker))
    # end timer for execution
    t2 = time.time()
    print("Time to retrieve PRTS stock data in seconds = " + str(t2 - t1))
    if stock1.get_totalCurrentAssets() != 139375.0:
        print("Error: PRTS stock get_totalCurrentAssets() method is incorrect and does not equal 139375.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalCurrentAssets()))

    if stock1.get_totalNonCurrentAssets() != 14742.0:
        print("Error: PRTS stock get_totalNonCurrentAssets() method is incorrect and does not equal 14742.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalNonCurrentAssets()))

    if stock1.get_totalAssets() != 186973.0:
        print("Error: PRTS stock get_totalAssets() method is incorrect and does not equal 186973.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalAssets()))

    if stock1.get_totalCurrentLiabilities() != 71979.0:
        print("Error: PRTS stock get_totalCurrentLiabilities() method is incorrect and does not equal 71979.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalCurrentLiabilities()))

    if stock1.get_totalNonCurrentLiabilities() != 4031.0:
        print("Error: PRTS stock get_totalNonCurrentLiabilities() method is incorrect and does not equal 4031.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalNonCurrentLiabilities()))

    if stock1.get_totalLiabilities() != 103484.0:
        print("Error: PRTS stock get_totalLiabilities() method is incorrect and does not equal 103484.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalLiabilities()))

    if stock1.get_totalStockholdersEquity() != 83489.0:
        print("Error: PRTS stock get_totalStockholdersEquity() method is incorrect and does not equal 83489.0 as shown in sec.gov, "
              "current value is " + str(stock1.get_totalStockholdersEquity()))

    if stock1.get_totalLiabilitiesAndStockholdersEquity() != 186973.0:
        print("Error: PRTS stock get_totalLiabilitiesAndStockholdersEquity() method is incorrect and does not equal 186973.0 as shown in sec.gov, "
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


if __name__ == "__main__":
    main()
