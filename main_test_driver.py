"""
Author: Sahngwoo Kim
Description:
This module runs all of the unit test drivers and integration test driver at once.
Especially useful for regression testing.
"""

from model import testBalanceSheet, testCashFlow, testFundamental, testIncomeStatement, testNewsAndStock, testTechnical
from control import controller_test_driver


def main():
    print("-------------------------------test result for testBalanceSheet:------------------------------------------")
    testBalanceSheet.main()

    print("-------------------------------test result for testCashFlow:----------------------------------------------")
    testCashFlow.main()

    print("-------------------------------test result for testFundamental:-------------------------------------------")
    testFundamental.main()

    print("-------------------------------test result for testIncomeStatement:---------------------------------------")
    testIncomeStatement.main()

    print("-------------------------------test result for testNewsAndStock:------------------------------------------")
    testNewsAndStock.main()

    print("-------------------------------test result for testTechnical:---------------------------------------------")
    testTechnical.main()

    print("-------------------------------test result for controller_test_driver:------------------------------------")
    controller_test_driver.main()


if __name__ == "__main__":
    main()
