
"""
Test Script written by Bathiya Ranasinghe for the Technical Class
Errors within the methods will be printed out to console

A test complete message will be printed at the end along with the time to execute getting the data
The script uses a range of values for certain tests and these ranges can change depending on current market conditions
So if an error is reported on data output it is also necessary to manually check on external sources to verify if the error
is valid or if there was a change in market conditions.

"""

from model.Technical import Technical
import ray

# initialize multiprocessing
ray.init(ignore_reinit_error=True)

ticker = "aapl"
tech = Technical(ticker)
print(tech.to_string_summary())

