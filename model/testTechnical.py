
"""
Test Script written by Bathiya Ranasinghe for the Technical Class
Errors within the methods will be printed out to console

A test complete message will be printed at the end along with the time to execute getting the data
The script prints output to the console and it is necessary to manually manually check on external sources to verify
the data since technical analysis information rapidly changes due to market conditions.
"""
from model.Technical import Technical
import ray

# initialize multiprocessing
ray.init(ignore_reinit_error=True)

# testing with a big cap stock from nasdaq exchange
ticker1 = "aapl"
tech1 = Technical(ticker1)
print('Testing ticker ' + ticker1)
print(tech1.to_string_summary())

# testing with a big cap stock from nyse exchange
ticker2 = "baba"
print('Testing ticker ' + ticker2)
tech2 = Technical(ticker1)
print(tech2.to_string_summary())

# testing with a small cap stock from nasdaq exchange
ticker3 = "VXRT"
tech3 = Technical(ticker1)
print('Testing ticker ' + ticker3)
print(tech3.to_string_summary())

# testing with a small cap stock from nyse exchange
ticker4 = "avlr"
print('Testing ticker ' + ticker4)
tech4 = Technical(ticker4)
print(tech4.to_string_summary())

# testing with a spac stock
ticker5 = "stpk"
print('Testing ticker ' + ticker5)
tech5 = Technical(ticker5)
print(tech5.to_string_summary())