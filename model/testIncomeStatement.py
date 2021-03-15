from model.Stock import Stock
import time

# testing for a ultra cap stock
ticker = "AAPL"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_income_statement(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve AAPL stock data in seconds = " + str(t2 - t1))
# testing if all the values retrieved are equivalent to the ratios in financial statements of apple
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements
if stock1.getRevenue() != 111439000000:
    print("Error: AAPL stock getRevenue() method is incorrect and does not equal 111439000000 as shown in sec.gov, "
          "current value is " + str(stock1.getRevenue()))

if stock1.getEbitda() != 36883000000:
    print("Error: AAPL stock getEbitda() method is incorrect and does not equal 36883000000 as shown in sec.gov, "
          "current value is " + str(stock1.getEbitda()))

if stock1.getIncomeTaxExpense() != 4824000000:
    print("Error: AAPL stock getIncomeTaxExpense() method is incorrect and does not equal 4824000000 as shown in sec.gov, "
          "current value is " + str(stock1.getIncomeTaxExpense()))

if stock1.getNetIncome() != 28755000000:
    print("Error: AAPL stock getNetIncome() method is incorrect and does not equal 28755000000 as shown in sec.gov, "
          "current value is " + str(stock1.getNetIncome()))

if stock1.getGrossProfit() != 44328000000:
    print("Error: AAPL stock getGrossProfit() method is incorrect and does not equal 44328000000 as shown in sec.gov, "
          "current value is " + str(stock1.getGrossProfit()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of carparts.com
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a small cap stock
ticker = "PRTS"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_income_statement(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve PRTS stock data in seconds = " + str(t2 - t1))
if stock1.getRevenue() != 117406000:
    print("Error: PRTS stock getRevenue() method is incorrect and does not equal 117406000 as shown in sec.gov, "
          "current value is " + str(stock1.getRevenue()))

if stock1.getEbitda() != 3498000.0:
    print("Error: PRTS stock getEbitda() method is incorrect and does not equal 3498000.0 as shown in sec.gov, "
          "current value is " + str(stock1.getEbitda()))

if stock1.getIncomeTaxExpense() != 45000.0:
    print("Error: PRTS stock getIncomeTaxExpense() method is incorrect and does not equal 45000.0 as shown in sec.gov, "
          "current value is " + str(stock1.getIncomeTaxExpense()))

if stock1.getNetIncome() != 1385000.0:
    print("Error: PRTS stock getNetIncome() method is incorrect and does not equal 1385000.0 as shown in sec.gov, "
          "current value is " + str(stock1.getNetIncome()))

if stock1.getGrossProfit() != 43121000:
    print("Error: PRTS stock getGrossProfit() method is incorrect and does not equal 43121000 as shown in sec.gov, "
          "current value is " + str(stock1.getGrossProfit()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of Cabot Microelectronics
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a medium cap stock
ticker = "CCMP"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_income_statement(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve CCMP stock data in seconds = " + str(t2 - t1))
if stock1.getRevenue() != 287863000:
    print("Error: CCMP stock getRevenue() method is incorrect and does not equal 287863000 as shown in sec.gov, "
          "current value is " + str(stock1.getRevenue()))

if stock1.getEbitda() != 87922000:
    print("Error: CCMP stock getEbitda() method is incorrect and does not equal 87922000 as shown in sec.gov, "
          "current value is " + str(stock1.getEbitda()))

if stock1.getIncomeTaxExpense() != 7546000.0:
    print(
        "Error: CCMP stock getIncomeTaxExpense() method is incorrect and does not equal 7546000.0 as shown in sec.gov, "
        "current value is " + str(stock1.getIncomeTaxExpense()))

if stock1.getNetIncome() != 31530000:
    print("Error: CCMP stock getNetIncome() method is incorrect and does not equal 31530000 as shown in sec.gov, "
          "current value is " + str(stock1.getNetIncome()))

if stock1.getGrossProfit() != 122904000:
    print(
        "Error: CCMP stock getGrossProfit() method is incorrect and does not equal 1120808000 as shown in sec.gov, "
        "current value is " + str(stock1.getGrossProfit()))
