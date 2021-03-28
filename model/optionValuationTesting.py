# This is a testing file for testing the Valuation Class
from control import controller
from model import organizeOptionData
from model.OptionValuation import Valuation
#import time

#
# INCOMPLETE, NEED TO FINISH CALIBRATING THE FINANCIAL MODELS
#


def main():
    def acceptableMarginOfError(a, b, tolerance):
        """
        Check if 2 float values are within range to prove the financial model is doesnt have significant errors
        Pre-Conditions:
            :param a: a float value
            :param b: a float value
            :param tolerance: a reasonable range for model error as a positive float
        :return True if the difference between a and b is insignificant
        """
        return #abs(a - b) < tolerance

    r = 0.01
    s = 30.0
    x = 40.0
    T = 240.0/365.0
    sigma = 0.30
    optionType = "Call"
    iterations = 100
    N = 100
    ticker = "AAPL"

    financialModel = Valuation(N, ticker, r, s, x, T, sigma, optionType, iterations)

    #test_item = ''
    #data_in = 0
    #expected = 0
    #reason = ''

    # call the operation
    #test = val.blackScholes()
    #test.add(data_in)
    #result = 10
    #if not acceptableMarginOfError(expected, result, 0.1):
    #print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

    # Testing Black Scholes execution time
    # Begin timer for execution
    #t1 = time.time()
    #financialModel = val(_N, _ticker, _r, _s, _x, _T, _sigma, optionType, iterations)
    # End timer for execution
    #t2 = time.time()
    #print("Time to calculate black scholes in seconds = " + str(t2 - t1))
    #expected = 10.0 # UPDATE THIS TO FIND OTHER MODEL PRICES ONLINE, FOR OTHER TESTS HAVE marginOfError function
    # Determine if the calculated value is within a margin of error of the black scholes price from another source
    #if financialModel.blackScholes() != expected:
    #print("Error: blackScholes() method is incorrect and does not equal ", expected, " as shown by secondary resource "
    #"current value is " + str(financialModel.blackScholes()))

    # Testing Binomial Model execution time & correctness

    # Testing Monte Carlo Simulation execution time & correctness

    # Testing Implied Volatility execution time & correctness

    # Round to 2 decimal places and print
    black_scholes_price = financialModel.blackScholes()
    print("Black Scholes Price: ", black_scholes_price)

    #binomial_price = financialModel.binomialModel()
    #round(binomial_price), 2
    #print("Binomial Price: ", binomial_price)

    monte_carlo_price = financialModel.monteCarloSimulation()
    print("Monte-Carlo Simulation Price: ", monte_carlo_price)

    intrinsic_value = financialModel.intrinsicValue()
    print("Intrinsic Value: ", intrinsic_value)

    speculative_premium = financialModel.speculativePremium()
    print("Speculative Premium: ", speculative_premium)

    delta = financialModel.delta()
    print("Delta: ", delta)

    gamma = financialModel.gamma()
    print("Gamma: ", gamma)

    charm = financialModel.charm()
    print("Charm: ", charm)

    vega = financialModel.vega()
    print("Vega: ", vega)

    theta = financialModel.theta()
    print("Theta: ", theta)

    rho = financialModel.rho()
    print("Rho: ", rho)

    #implied_volatility = financialModel.impliedVolatility()
    #print("Implied Volatility: ", implied_volatility)

    risk_free_rate = r
    print("Risk Free Rate: ", risk_free_rate)

    current_stock_price = s
    print("Current Stock Price: ", current_stock_price)

    current_strike_price = x
    print("Option Strike Price: ", current_strike_price)

    time_to_maturity = T
    print("Time to Maturity: ", time_to_maturity)

    #volatility_sigma = _sigma
    #print("Volatility: ", volatility_sigma)


# run test
if __name__ == "__main__":
    main()


















# Sees if two valuation classes are equal (can compare any attributes)
# If you dont override it compares memory location
#def __eq__(self, other):
    #if self._ticker == other._ticker and self._dataSource == other._dataSource and self._optionType == other._optionType:
        #return True
    #return False


# Override the String Method
#def __str__(self):
    #return self._ticker +" " + self._dataSource + " " + self.expiration + " " + self._optionStyle + " " + self._optionType + " " + self._ITMATMOTM + " " + self.longShort
