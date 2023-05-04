"""
Test Script written by Bathiya Ranasinghe for the Technical Class

A test complete message will be printed at the end along with the time to execute getting the data
The script prints output to the console and it is necessary to manually manually check on external sources to verify
the data since technical analysis information rapidly changes due to market conditions.
"""
import datetime
from model.Technical import Technical
import ray


def main():
    # initialize ray if it wasn't previously initialized
    if not ray.is_initialized():
        ray.init()

    # testing with a big cap stock from nasdaq exchange

    ticker1 = "aapl"
    begin_time = datetime.datetime.now()
    tech1 = Technical(ticker1)
    execution_time_tech1 = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time

    print(f'Testing ticker {ticker1}')
    print(tech1.to_string_summary())

    # testing with a big cap stock from nyse exchange
    ticker2 = "baba"
    print(f'Testing ticker {ticker2}')
    begin_time = datetime.datetime.now()
    tech2 = Technical(ticker1)
    execution_time_tech2 = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time
    print(tech2.to_string_summary())

    # testing with a small cap stock from nasdaq exchange
    ticker3 = "VXRT"
    begin_time = datetime.datetime.now()
    tech3 = Technical(ticker1)
    execution_time_tech3 = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time
    print(f'Testing ticker {ticker3}')
    print(tech3.to_string_summary())

    # testing with a small cap stock from nyse exchange
    ticker4 = "avlr"
    print(f'Testing ticker {ticker4}')
    begin_time = datetime.datetime.now()
    tech4 = Technical(ticker4)
    execution_time_tech4 = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time
    print(tech4.to_string_summary())

    # testing with a spac stock
    ticker5 = "stpk"
    print(f'Testing ticker {ticker5}')
    begin_time = datetime.datetime.now()
    tech5 = Technical(ticker5)
    execution_time_tech5 = (
            datetime.datetime.now() - begin_time).total_seconds()  # begin timer for execution time
    print(tech5.to_string_summary())

    # testing complete messege along with execution times
    print("\n**** Testing Complete ****")
    print(f'Execution time for {ticker1} {str(execution_time_tech1)} seconds')
    print(f'Execution time for {ticker2} {str(execution_time_tech2)} seconds')
    print(f'Execution time for {ticker3} {str(execution_time_tech3)} seconds')
    print(f'Execution time for {ticker4} {str(execution_time_tech4)} seconds')
    print(f'Execution time for {ticker5} {str(execution_time_tech5)} seconds')

# run test
if __name__ == "__main__":
    main()
