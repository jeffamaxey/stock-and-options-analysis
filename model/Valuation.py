import numpy as np
from scipy.stats import norm
import model.ValidTicker as validTicker
import yfinance as yf
import time


class Valuation:
    def __init__(self, N, ticker, r, s, x, T, sigma, optionType, iterations):
        """
        Attributes:
            self._N:          ex.10000      -the number of periods for the binomial model
            self._ticker:     ex.AAPL      -is the _ticker tickerSymbol of the underlying asset
            self._r:          ex.0.01       -risk-free interest rate (annual rate expressed in terms of continuous compounding)
            self._s:          ex.30.0       -(SO or C) Spot price of the underlying asset (stock price)
            self._x:          ex.40.0       -(sometimes called k) market strike price of the option (Also called the Exercise Price)
            self._T:          ex.40.0/365.0 -time until expiration out of a year 40/365 is 40 days to expiration often shown as (_T-t)
            self._sigma:      ex.0.30       -_volatility of returns can also be known as the standard deviation of the underlying asset
            self._optionType: ex."Call" or "Put"
            self._iterations: ex.1000000    -how many prices to simulate for the Binomial Model & monte carlo simulation
        :thrown RuntimeError if _ticker is invalid
        # NOTE Can change all norm.pdf to norm._pdf and change all norm.cdf to ndtr() for a performance boost
        """
        # convert passed in ticker to all upper case
        #ticker = ticker.upper()
        # update ticker symbol within the class
        self.tickerSymbol = yf.Ticker(ticker)

        # update _ticker symbol within the class
        # if the ticker is not valid an exception is thrown
        #if not validTicker.valid_ticker(ticker):
            #raise RuntimeError("This is not a valid ticker symbol")

        self._N = N
        self._ticker = ticker
        self._r = r
        self._s = s
        self._x = x
        self._T = T
        self._sigma = sigma
        self._optionType = optionType
        self._iterations = iterations

    def blackScholes(self):
        # Compute the Black Scholes price for a call or put
        d1 = (np.log(self._s / self._x) + (self._r + 0.5 * (self._sigma ** 2)) * self._T) / (self._sigma * np.sqrt(self._T))
        #d1 = (1.0/(self._sigma * np.sqrt(self._T))) * (np.log(self._s/self._x) + (self._r + 0.5 * self._sigma**2.0) * self._T)
        d2 = d1 - self._sigma * (np.sqrt(self._T))
        try:
            if self._optionType == "Call":
                # Cumulative distribution function centered around 0 standard deviation of 1, (d1, 0, 1) required by formula
                # Part of the equation _x*np.exp(-_r*_T) is the discounted strike price
                blackScholesPrice = self._s * (norm.cdf(d1, 0, 1)) - self._x * np.exp(-self._r * self._T) * (norm.cdf(d2, 0, 1))
            elif self._optionType == "Put":
                # The negative of a Call
                blackScholesPrice = self._x * np.exp(-self._r * self._T) * (norm.cdf(-d2, 0, 1)) - self._s * (norm.cdf(-d1, 0, 1))
            return blackScholesPrice
        except:
            print("Review incorrect Black Scholes parameters")

    def intrinsicValue(self):
        # Find the intrinsic value of a call or put
        try:
            if self._optionType == "Call":
                # The intrinsic value of the call
                intrinsic = max(self._s - self._x, 0)
            elif self._optionType == "Put":
                # The intrinsic value of the put
                intrinsic = max(self._x - self._s, 0)
            return intrinsic
        except:
            print("Review incorrect intrinsic value parameters")

    def speculativePremium(self):
        # Find the speculative value of a call or put
        specPremium = self.blackScholes()-self.intrinsicValue()
        return specPremium

    def binomialModel(self):
        # Find the theoretical price of a call or put option using the binomial model
        deltaT = self._T / self._N                         # delta _T
        u = np.exp(self._sigma * np.sqrt(deltaT))       # up factor
        d = 1/u                                        # down factor
        p = (1 + self._r - d) / (u - d)                              # risk-neutral up probability
        q = 1-p                                        # risk-neutral down probability

        # Initialize the price vector
        binomialStock = np.zeros([self._N + 1, self._N + 1])
        for i in range(self._N + 1):
            for y in range(i+1):
                binomialStock[y, i] = self._s * (u ** (i - y)) * (d ** y)

        # Initialize the price vector & generate the option prices recursively
        binomialOption = np.zeros([self._N + 1, self._N + 1])
        binomialOption[:, self._N] = np.maximum(np.zeros(self._N + 1), (binomialStock[:, self._N] - self._x))
        for i in range(self._N - 1, -1, -1):
            for y in range(0, i+1):
                binomialOption[y, i] = (1 / (1 + self._r) * (p * binomialOption[y, i + 1] + q * binomialOption[y + 1, i + 1]))
        return binomialOption

    def monteCarloSimulation(self):
        # Find the theoretical price of a call or put option using a monte carlo simulation
        # 2 columns: (zeros & payoffs) for a call max(0,_s-_x)
        optionData = np.zeros([self._iterations, 2])

        # 1-dimensional array with items = number of _iterations
        # mean 0 and variance 1
        rand = np.random.normal(0, 1, [1, self._iterations])

        # Formula for the stock price
        stockPrice = self._s * np.exp(self._T * (self._r - 0.5 * self._sigma ** 2) + self._sigma * np.sqrt(self._T) * rand)

        try:
            if self._optionType == "Call":
                # Compute the payoff function
                optionData[:, 1] = stockPrice - self._x

            elif self._optionType == "Put":
                # Different payoff function for a put
                optionData[:, 1] = self._x - stockPrice

            # The average for the monte carlo method
            avg = np.sum(np.amax(optionData, axis=1))/float(self._iterations)

            # Using the exponential (continuously compounded) discount rate exp(-rT)
            # For the present value of the future cash flow
            simulation = np.exp(-1.0 * self._r * self._T) * avg
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
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        try:
            if self._optionType == "Call":
                # The delta of a call
                _delta = norm.cdf(d1, 0, 1)
            elif self._optionType == "Put":
                # The delta of a put
                _delta = norm.cdf(d1, 0, 1) - 1.0
            return _delta
        except:
            print("Review incorrect Delta parameters")

    def gamma(self):
        # Gamma is the rate of change for an options delta based on a single point move in the deltas price (highest when ATM)
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        _gamma = (norm.pdf(d1)) / (self._s * self._sigma * np.sqrt(self._T))
        return _gamma

    def charm(self):
        # Charm is the 'delta decay' the rate at which the delta of an option changes with respect to the passage of time
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        d2 = d1 - self._sigma * np.sqrt(self._T)
        _charm = -norm.pdf(d1, 0, 1) * (2 * self._r * self._T - d2 * self._sigma * np.sqrt(self._T)) / (2 * self._T * self._sigma * np.sqrt(self._T))
        return _charm

    def vega(self):
        # Vega is the sensitivity of the options price to the change in the underlying assets return _volatility
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        _vega = (self._s * norm.pdf(d1) * np.sqrt(self._T)) / 100.0
        return _vega

    def theta(self):
        # Theta is the change in the options price with respect to the passage of time as maturity becomes shorter
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        d2 = d1 - (self._sigma * np.sqrt(self._T))
        try:
            if self._optionType == "Call":
                # The theta of a call
                _theta = (-((self._s * norm.pdf(d1) * self._sigma) / (2.0 * np.sqrt(self._T))) - (self._r * self._x * np.exp(-self._r * self._T) * norm.cdf(d2, 0, 1))) / 365.0
            elif self._optionType == "Put":
                # The theta of a put
                _theta = (-((self._s * norm.pdf(d1) * self._sigma) / (2.0 * np.sqrt(self._T))) + (self._r * self._x * np.exp(-self._r * self._T) * norm.cdf(-d2, 0, 1))) / 365.0
            return _theta
        except:
            print("Review incorrect Theta parameters")

    def rho(self):
        # Rho is the options sensitivity to the change in the risk-free rate (_r)
        d1 = (1.0 / (self._sigma * np.sqrt(self._T))) * (np.log(self._s / self._x) + (self._r + 0.5 * self._sigma ** 2.0) * self._T)
        d2 = d1 - (self._sigma * np.sqrt(self._T))
        try:
            if self._optionType == "Call":
                # The rho of a call
                _rho = (self._x * self._T * np.exp(-self._r * self._T) * norm.cdf(d2, 0, 1)) / 100.0
            elif self._optionType == "Put":
                # The rho of a put
                _rho = (-self._x * self._T * np.exp(-self._r * self._T) * norm.cdf(-d2, 0, 1)) / 100.0
            return _rho
        except:
            print("Review incorrect Rho parameters")

    def impliedVolatility(self):
        maxIter = 1          # computationally expensive keep maxIter low
        precise = 1.0e-5
        for m in range(0, maxIter):
            # Root objective function
            difference = self._x - self.blackScholes()
            if abs(difference) < precise:
                return self._sigma
            _sigma = self._sigma + difference / self.vega
        return _sigma



