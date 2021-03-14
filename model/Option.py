from yfinance


class Option:
    # Initializer or Constructor method to run every time the Option class is called
    def __init__(self, ticker, dataSource, expiration, currentDate, optionStyle, optionType, ITMATMOTM):
        """
        The Option class represents the analysis input the user must submit for the valuation page & some of the backend math
        Attributes:
            :param ticker is the ticker symbol of the Underlying Asset
            :param dataSource is the chosen data source
            :param expiration is the chosen expiration date of the option
            :param currentDate is the current day
            :param optionStyle is either American or European
            :param optionType is either a Call or Put
            :param ITMATMOTM is in-the-money, at-the-money, out-the-money
        :thrown RuntimeError if ticker is invalid
        """
        # if the ticker is not valid an exception is thrown
        if not ValidTicker.valid_ticker(ticker):
            raise RuntimeError

        self.ticker = ticker
        self.dataSource = dataSource
        self.expiration = expiration
        self.currentDate = currentDate
        self.optionStyle = optionStyle
        self.optionType = optionType
        self.ITMATMOTM = ITMATMOTM

    # Getter
    # Making the attributes, properties
    @property
    def ticker(self):
        return self.ticker

    # Setter
    # Can access these by just .ticker dont need to use get_attribute or call function name or anything
    # print(Option[0].ticker)
    @ticker.setter
    def ticker(self, assignedData):
        self.ticker = assignedData

    # the following deletes the input
    # del Option[0].ticker
    @ticker.deleter
    def ticker(self):
        del self.ticker

    # Getter for data source
    @property
    def dataSource(self):
        return self.dataSource

    # Setter for data source
    @dataSource.setter
    def dataSource(self, assignedData):
        self.dataSource = assignedData

    # Getter for expiration
    @property
    def expiration(self):
        return self.expiration

    # Setter for expiration
    @expiration.setter
    def expiration(self, assignedData):
        self.expiration = assignedData

    # Getter for current date
    @property
    def currentDate(self):
        return self.currentDate

    # Setter for current date
    @currentDate.setter
    def currentDate(self, assignedData):
        self.currentDate = assignedData

    # Getter for option style
    @property
    def optionStyle(self):
        return self.optionStyle

    # Setter for option style
    @optionStyle.setter
    def optionStyle(self, assignedData):
        self.optionStyle = assignedData

    # Getter for option type
    @property
    def optionType(self):
        return self.optionType

    # Setter for option type
    @optionType.setter
    def optionType(self, assignedData):
        self.optionType = assignedData

    # Getter for in-the-money, at-the-money, out-the-money
    @property
    def ITMATMOTM(self):
        return self.ITMATMOTM

    # Setter for in-the-money, at-the-money, out-the-money
    @ITMATMOTM.setter
    def ITMATMOTM(self, assignedData):
        self.ITMATMOTM = assignedData

    # Getter for risk-free-rate (r)
    @property
    def riskFreeRate(self):
        return self.riskFreeRate

    # Setter for risk-free-rate (r)
    @riskFreeRate.setter
    def riskFreeRate(self, assignedData):
        self.riskFreeRate = assignedData

    # Getter for strike price (x)
    @property
    def strikePrice(self):
        return self.strikePrice

    # Setter for strike price (x)
    @strikePrice.setter
    def strikePrice(self, assignedData):
        self.strikePrice = assignedData

    # Getter for underlyingAsset (s)
    @property
    def underlyingAsset(self):
        return self.underlyingAsset

    # Setter for underlyingAsset (s)
    @underlyingAsset.setter
    def underlyingAsset(self, assignedData):
        self.underlyingAsset = assignedData

    # Getter for volatility (sigma)
    @property
    def volatility(self):
        return self.volatility

    # Setter for volatility (sigma)
    @volatility.setter
    def volatility(self, assignedData):
        self.volatility = assignedData





    # Determine days left by using the current date and expiration date
    # T = days left / 365
    # look up how to calculate time to maturity, maybe option chain will just have it
    def timeToMaturity(self):
        return





















    # Override the String Method
    def __str__(self):
        return self.ticker +" "+ self.dataSource +" "+ self.expiration +" "+ self.optionStyle +" "+ self.optionType +" "+ self.ITMATMOTM +" "+ self.longShort

    # Sees if two valuation classes are equal (can compare any attributes)
    # If you dont override it compares memory location
    def __eq__(self, other):
        if self.ticker == other.ticker and self.dataSource == other.dataSource and self.optionType == other.optionType:
            return True
        return False

# Call the option class & Print
tester = Option("AAPL", "Yahoo", "May 9, 2021", "American", "Call", "OTM")
print(tester.ticker, tester.dataSource, tester.expiration, tester.optionStyle, tester.optionType, tester.ITMATMOTM)
# Alternatively save the options in a list & print AAPL
options = [Option("AAPL", "Yahoo", "May 9, 2021", "American", "Call", "OTM"),
           Option("GME", "Yahoo", "May 21, 2021", "American", "Put", "ATM")]
print(options[0].ticker)

# Tests comparison __eq__ prints T or F
print(Option[0]==Option[1])

# __repr__ = __str__
# The above override allows you to print an entire
# Data structures contents with just
#print(options)
# Removes the need for the following:
def print_all_options(options):
    for x in options:
        print(x)






if __name__ == "__main__":
    ticker = ValidTicker
    dataSource = ["Yahoo", "Bloomberg", "Questtrade", "RobinHood"]
    optionStyle = ["American", "European"]
    optionType = ["Call", "Put"]
    ITMATMOTM = ["ITM", "ATM", "OTM", "ITM+", "OTM+"]
    expiration =
    currentDate =
    T = 40.0/365.0
    s = 30.0
    x = 40.0
    r = 0.01
    sigma = 0.30


    financialModel = Option(ticker, dataSource, expiration, currentDate, optionStyle, optionType, ITMATMOTM)

    # Round to 2 decimal places and print
    black_scholes_price = (round(financialModel.blackScholes()), 2)
    print("Black Scholes Price: ", black_scholes_price)

