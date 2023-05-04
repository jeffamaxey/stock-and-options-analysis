"""
Author: Ramtin Mahdavifar
"""
from model.Stock import Stock
import time


def main():
    # begin timer for execution
    t1 = time.time()
    ticker = "AAPL"
    stock1 = Stock.get_cash_flow(Stock(ticker))
    # end timer for execution
    t2 = time.time()
    print(f"Time to retrieve AAPL stock data in seconds = {str(t2 - t1)}")
    # testing if all the values retrieved are equivalent to the ratios in financial statements of apple
    # all these numbers are gotten from sec.gov where one can view the papers of public financial statements
    if stock1.getNetCashProvidedByOperatingActivities() != 38763000000:
        print(
            f"Error: AAPL stock getNetCashProvidedByOperatingActivities() method is incorrect and does not equal 38763000000 as shown in sec.gov, current value is {str(stock1.getNetCashProvidedByOperatingActivities())}"
        )

    if stock1.getNetCashUsedForInvestingActivites() != -8584000000:
        print(
            f"Error: AAPL stock getNetCashUsedForInvestingActivites() method is incorrect and does not equal -8584000000 as shown in sec.gov, current value is {str(stock1.getNetCashUsedForInvestingActivites())}"
        )

    if stock1.getNetCashUsedProvidedByFinancingActivities() != -32249000000:
        print(
            f"Error: AAPL stock getNetCashUsedProvidedByFinancingActivities() method is incorrect and does not equal -32249000000 as shown in sec.gov, current value is {str(stock1.getNetCashUsedProvidedByFinancingActivities())}"
        )

    if stock1.getFreeCashFlow() != 35263000000:
        print(
            f"Error: AAPL stock getFreeCashFlow() method is incorrect and does not equal 35263000000 as shown in sec.gov, current value is {str(stock1.getFreeCashFlow())}"
        )

    # testing if all the values retrieved are equivalent to the ratios in financial statements of carparts.com
    # all these numbers are gotten from sec.gov where one can view the papers of public financial statements

    # testing for a small cap stock
    ticker = "PRTS"
    # begin timer for execution
    t1 = time.time()
    stock1 = Stock.get_cash_flow(Stock(ticker))
    # end timer for execution
    t2 = time.time()
    print(f"Time to retrieve PRTS stock data in seconds = {str(t2 - t1)}")
    if stock1.getNetCashProvidedByOperatingActivities() != -19068000:
        print(
            f"Error: PRTS stock getNetCashProvidedByOperatingActivities() method is incorrect and does not equal -19068000 as shown in sec.gov, current value is {str(stock1.getNetCashProvidedByOperatingActivities())}"
        )

    if stock1.getNetCashUsedForInvestingActivites() != -9758000.0:
        print(
            f"Error: PRTS stock getNetCashUsedForInvestingActivites() method is incorrect and does not equal -9758000.0 as shown in sec.gov, current value is {str(stock1.getNetCashUsedForInvestingActivites())}"
        )

    if stock1.getNetCashUsedProvidedByFinancingActivities() != 62361000:
        print(
            f"Error: PRTS stock getNetCashUsedProvidedByFinancingActivities() method is incorrect and does not equal 62361000 as shown in sec.gov, current value is {str(stock1.getNetCashUsedProvidedByFinancingActivities())}"
        )

    if stock1.getFreeCashFlow() != -28725000:
        print(
            f"Error: PRTS stock getFreeCashFlow() method is incorrect and does not equal -28725000 as shown in sec.gov, current value is {str(stock1.getFreeCashFlow())}"
        )

    # testing if all the values retrieved are equivalent to the ratios in financial statements of Cabot Microelectronics
    # all these numbers are gotten from sec.gov where one can view the papers of public financial statements

    # testing for a medium cap stock
    ticker = "CCMP"
    # begin timer for execution
    t1 = time.time()
    stock1 = Stock.get_cash_flow(Stock(ticker))
    # end timer for execution
    t2 = time.time()
    print(f"Time to retrieve CCMP stock data in seconds = {str(t2 - t1)}")
    if stock1.getNetCashProvidedByOperatingActivities() != 54038000:
        print(
            f"Error: CCMP stock getNetCashProvidedByOperatingActivities() method is incorrect and does not equal 54038000 as shown in sec.gov, current value is {str(stock1.getNetCashProvidedByOperatingActivities())}"
        )

    if stock1.getNetCashUsedForInvestingActivites() != -11586000:
        print(
            f"Error: CCMP stock getNetCashUsedForInvestingActivites() method is incorrect and does not equal -11586000 as shown in sec.gov, current value is {str(stock1.getNetCashUsedForInvestingActivites())}"
        )

    if stock1.getNetCashUsedProvidedByFinancingActivities() != -25364000:
        print(
            f"Error: CCMP stock getNetCashUsedProvidedByFinancingActivities() method is incorrect and does not equal -25364000 as shown in sec.gov, current value is {str(stock1.getNetCashUsedProvidedByFinancingActivities())}"
        )

    if stock1.getFreeCashFlow() != 42099000:
        print(
            f"Error: CCMP stock getFreeCashFlow() method is incorrect and does not equal 181346000 as shown in sec.gov, current value is {str(stock1.getFreeCashFlow())}"
        )


if __name__ == "__main__":
    main()
