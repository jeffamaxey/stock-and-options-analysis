import numpy as np
from scipy.stats import norm
import time

from model import ValidTicker


class Valuation:
    def __init__(self, N, ticker, r, s, x, T, sigma, optionType, iterations):
        """
        Attributes:
            self.N:          ex.10000      -the number of periods for the binomial model
            self.ticker:     ex.AAPL      -is the ticker tickerSymbol of the underlying asset
            self.r:          ex.0.01       -risk-free interest rate (annual rate expressed in terms of continuous compounding)
            self.s:          ex.30.0       -(SO or C) Spot price of the underlying asset (stock price)
            self.x:          ex.40.0       -(sometimes called k) market strike price of the option (Also called the Exercise Price)
            self.T:          ex.40.0/365.0 -time until expiration out of a year 40/365 is 40 days to expiration often shown as (T-t)
            self.sigma:      ex.0.30       -_volatility of returns can also be known as the standard deviation of the underlying asset
            self._optionType: ex."Call" or "Put"
            self.iterations: ex.1000000    -how many prices to simulate for the Binomial Model & monte carlo simulation
        :thrown RuntimeError if ticker is invalid
        # NOTE Can change all norm.pdf to norm._pdf and change all norm.cdf to ndtr() for a performance boost
        """
        self.N = N
        self.ticker = ticker
        self.r = r
        self.s = s
        self.x = x
        self.T = T
        self.sigma = sigma
        self.optionType = optionType
        self.iterations = iterations

        # If the ticker is not valid an exception is thrown
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError

    def blackScholes(self):
        # Compute the Black Scholes price for a call or put
        d1 = (np.log(self.s/self.x) + (self.r + 0.5 * (self.sigma**2))*self.T)/(self.sigma*np.sqrt(self.T))
        #d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        d2 = d1 - self.sigma*(np.sqrt(self.T))
        try:
            if self.optionType == "Call":
                # Cumulative distribution function centered around 0 standard deviation of 1, (d1, 0, 1) required by formula
                # Part of the equation x*np.exp(-r*T) is the discounted strike price
                blackScholesPrice = self.s*(norm.cdf(d1, 0, 1))-self.x*np.exp(-self.r*self.T)*(norm.cdf(d2, 0, 1))
            elif self.optionType == "Put":
                # The negative of a Call
                blackScholesPrice = self.x*np.exp(-self.r*self.T)*(norm.cdf(-d2, 0, 1))-self.s*(norm.cdf(-d1, 0, 1))
            return blackScholesPrice
        except:
            print("Review incorrect Black Scholes parameters")

    def intrinsicValue(self):
        # Find the intrinsic value of a call or put
        try:
            if self.optionType == "Call":
                # The intrinsic value of the call
                intrinsic = max(self.s-self.x, 0)
            elif self.optionType == "Put":
                # The intrinsic value of the put
                intrinsic = max(self.x-self.s, 0)
            return intrinsic
        except:
            print("Review incorrect intrinsic value parameters")

    def speculativePremium(self):
        # Find the speculative value of a call or put
        specPremium = self.blackScholes()-self.intrinsicValue()
        return specPremium

    def binomialModel(self):
        # Find the theoretical price of a call or put option using the binomial model
        deltaT = self.T/self.N                         # delta T
        u = np.exp(self.sigma * np.sqrt(deltaT))       # up factor
        d = 1/u                                        # down factor
        p = (1+self.r-d)/(u-d)                              # risk-neutral up probability
        q = 1-p                                        # risk-neutral down probability

        # Initialize the price vector
        binomialStock = np.zeros([self.N+1, self.N+1])
        for i in range(self.N+1):
            for y in range(i+1):
                binomialStock[y, i] = self.s*(u**(i-y))*(d**y)

        # Initialize the price vector & generate the option prices recursively
        binomialOption = np.zeros([self.N + 1, self.N + 1])
        binomialOption[:, self.N] = np.maximum(np.zeros(self.N + 1), (binomialStock[:, self.N]-self.x))
        for i in range(self.N-1, -1, -1):
            for y in range(0, i+1):
                binomialOption[y, i] = (1/(1+self.r) * (p*binomialOption[y, i+1] + q*binomialOption[y+1, i+1]))
        return binomialOption

    def monteCarloSimulation(self):
        # Find the theoretical price of a call or put option using a monte carlo simulation
        # 2 columns: (zeros & payoffs) for a call max(0,s-x)
        optionData = np.zeros([self.iterations, 2])

        # 1-dimensional array with items = number of iterations
        # mean 0 and variance 1
        rand = np.random.normal(0, 1, [1, self.iterations])

        # Formula for the stock price
        stockPrice = self.s*np.exp(self.T*(self.r-0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)

        try:
            if self.optionType == "Call":
                # Compute the payoff function
                optionData[:, 1] = stockPrice - self.x

            elif self.optionType == "Put":
                # Different payoff function for a put
                optionData[:, 1] = self.x - stockPrice

            # The average for the monte carlo method
            avg = np.sum(np.amax(optionData, axis=1))/float(self.iterations)

            # Using the exponential (continuously compounded) discount rate exp(-rT)
            # For the present value of the future cash flow
            simulation = np.exp(-1.0*self.r*self.T)*avg
            return simulation
        except:
            print("Review incorrect monte carlo simulation parameters")

    def n(self, d1):
        # Normal cumulative density function (can just use norm.cdf())
        n_cdf = norm.ndtr(d1)
        return n_cdf

    def phi(self, d1):
        # Phi helper function (can just use norm.pdf())
        phi = np.exp(-0.5 * d1 * d1) / (np.sqrt(2.0 * np.pi))
        return phi

    def delta(self):
        # Delta is the change in the option price with respect to a change in an underlying assets price
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        try:
            if self.optionType == "Call":
                # The delta of a call
                _delta = norm.cdf(d1, 0, 1)
            elif self.optionType == "Put":
                # The delta of a put
                _delta = norm.cdf(d1, 0, 1) - 1.0
            return _delta
        except:
            print("Review incorrect Delta parameters")

    def gamma(self):
        # Gamma is the rate of change for an options delta based on a single point move in the deltas price (highest when ATM)
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        _gamma = (norm.pdf(d1)) / (self.s * self.sigma * np.sqrt(self.T))
        return _gamma

    def charm(self):
        # Charm is the 'delta decay' the rate at which the delta of an option changes with respect to the passage of time
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        d2 = d1 - self.sigma*np.sqrt(self.T)
        _charm = -norm.pdf(d1, 0, 1)*(2*self.r*self.T-d2*self.sigma*np.sqrt(self.T))/(2*self.T*self.sigma*np.sqrt(self.T))
        return _charm

    def vega(self):
        # Vega is the sensitivity of the options price to the change in the underlying assets return _volatility
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        _vega = (self.s * norm.pdf(d1) * np.sqrt(self.T)) / 100.0
        return _vega

    def theta(self):
        # Theta is the change in the options price with respect to the passage of time as maturity becomes shorter
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        d2 = d1 - (self.sigma * np.sqrt(self.T))
        try:
            if self.optionType == "Call":
                # The theta of a call
                _theta = (-((self.s * norm.pdf(d1) * self.sigma) / (2.0 * np.sqrt(self.T))) - (self.r * self.x * np.exp(-self.r * self.T) * norm.cdf(d2, 0, 1))) / 365.0
            elif self.optionType == "Put":
                # The theta of a put
                _theta = (-((self.s * norm.pdf(d1) * self.sigma) / (2.0 * np.sqrt(self.T))) + (self.r * self.x * np.exp(-self.r * self.T) * norm.cdf(-d2, 0, 1))) / 365.0
            return _theta
        except:
            print("Review incorrect Theta parameters")

    def rho(self):
        # Rho is the options sensitivity to the change in the risk-free rate (r)
        d1 = (1.0/(self.sigma * np.sqrt(self.T))) * (np.log(self.s/self.x) + (self.r + 0.5 * self.sigma**2.0) * self.T)
        d2 = d1 - (self.sigma * np.sqrt(self.T))
        try:
            if self.optionType == "Call":
                # The rho of a call
                _rho = (self.x * self.T * np.exp(-self.r * self.T) * norm.cdf(d2, 0, 1)) / 100.0
            elif self.optionType == "Put":
                # The rho of a put
                _rho = (-self.x * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2, 0, 1)) / 100.0
            return _rho
        except:
            print("Review incorrect Rho parameters")

    def impliedVolatility(self):
        maxIter = 100          # computationally expensive keep maxIter low
        precise = 1.0e-5
        for m in range(0, maxIter):
            # Root objective function
            difference = self.x - self.blackScholes()
            if abs(difference) < precise:
                return self.sigma
            _sigma = self.sigma + difference/self.vega
        return _sigma


if __name__ == "__main__":

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


