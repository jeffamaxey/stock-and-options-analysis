# This is a testing file for testing the Valuation Class
from model.Valuation import Valuation as val
import time

#
# INCOMPLETE, NEED TO FINISH TESTING THE VALUATION MODELS
#


if __name__ == "__main":
    def acceptableMarginOfError(a, b, tolerance):
        """
        Check if 2 float values are within range to prove the financial model is doesnt have significant errors
        Pre-Conditions:
            :param a: a float value
            :param b: a float value
            :param tolerance: a reasonable range for model error as a positive float
        :return True if the difference between a and b is insignificant
        """
        return abs(a - b) < tolerance

    ticker = "AAPL"
    r = 0.01
    s = 30.0
    x = 40.0
    T = 240.0/365.0
    sigma = 0.30
    optionType = "Call"
    iterations = 100
    N = 100

    #
    test_item = ''
    data_in = 0
    expected = 0
    reason = ''

    # call the operation
    test = val.blackScholes()
    test.add(data_in)
    result =
    if not acceptableMarginOfError(expected, result, 0.1):
        print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


    # Testing Black Scholes execution time
    # Begin timer for execution
    t1 = time.time()
    financialModel = val(N, ticker, r, s, x, T, sigma, optionType, iterations)
    # End timer for execution
    t2 = time.time()
    print("Time to calculate black scholes in seconds = " + str(t2 - t1))
    expected = 10.0 # UPDATE THIS TO FIND OTHER MODEL PRICES ONLINE, FOR OTHER TESTS HAVE marginOfError function
    # Determine if the calculated value is within a margin of error of the black scholes price from another source
    if financialModel.blackScholes() != expected:
        print("Error: blackScholes() method is incorrect and does not equal ", expected, " as shown by secondary resource "
              "current value is " + str(financialModel.blackScholes()))



    # Testing Binomial Model execution time & correctness

    # Testing Monte Carlo Simulation execution time & correctness

    # Testing Implied Volatility execution time & correctness



    # Round to 2 decimal places and print
    black_scholes_price = financialModel.blackScholes()
    round(black_scholes_price, 2)
    print("Black Scholes Price: ", black_scholes_price)

    #binomial_price = financialModel.binomialModel()
    #round(binomial_price), 2
    #print("Binomial Price: ", binomial_price)

    monte_carlo_price = financialModel.monteCarloSimulation()
    round(monte_carlo_price), 2
    print("Monte-Carlo Simulation Price: ", monte_carlo_price)

    intrinsic_value = financialModel.intrinsicValue()
    round(intrinsic_value), 2
    print("Intrinsic Value: ", intrinsic_value)

    speculative_premium = financialModel.speculativePremium()
    round(speculative_premium), 2
    print("Speculative Premium: ", speculative_premium)

    delta = financialModel.delta()
    round(delta), 2
    print("Delta: ", delta)

    gamma = financialModel.gamma()
    round(gamma), 2
    print("Gamma: ", gamma)

    charm = financialModel.charm()
    round(charm), 2
    print("Charm: ", charm)

    vega = financialModel.vega()
    round(vega), 2
    print("Vega: ", vega)

    theta = financialModel.theta()
    round(theta), 2
    print("Theta: ", theta)

    rho = financialModel.rho()
    round(rho), 2
    print("Rho: ", rho)

    implied_volatility = financialModel.impliedVolatility()
    round(implied_volatility), 2
    print("Implied Volatility: ", implied_volatility)

    risk_free_rate = r
    print("Risk Free Rate: ", risk_free_rate)

    current_stock_price = s
    print("Current Stock Price: ", current_stock_price)

    current_strike_price = x
    print("Option Strike Price: ", current_strike_price)

    time_to_maturity = T
    print("Time to Maturity: ", time_to_maturity)

    volatility_sigma = sigma
    print("Volatility: ", volatility_sigma)



