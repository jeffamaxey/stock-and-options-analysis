from control import controller
from model import OptionData
from model.Option import Option


def main(self=None):
    tickerSymbol = "TSLA"
    print("Expirations: ", Option.get_expirations(tickerSymbol))
    #print("Price of the Underlying Asset: ", Option.get_currentPriceOfTheUnderlyingAsset(tickerSymbol))
    print("Risk-Free Rate: ", Option.get_riskFreeRate(tickerSymbol))
    print(OptionData.get_finalDict('TSLA', 'Call', 'atm', '2021-07-16'))
    print(controller.get_quantitative_analysis('TSLA', '2021-07-16', 'American', 'Call', 'Yahoo', 'atm'))


# run test
if __name__ == "__main__":
    main()
