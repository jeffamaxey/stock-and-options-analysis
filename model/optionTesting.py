from model.Option import Option


def main():
    # Adjustments so print shows all columns and more rows of the dataframe
    #desired_width=400
    #pd.set_option('display.width', desired_width)
    #np.set_printoptions(linewidth=desired_width)
    #pd.set_option('display.max_columns', 12)

    # to display more than 10 rows when the dataframe is truncated set min_rows greater than 10
    # with more than 200 rows if max_rows is 200 and min_rows is 20, 10 from the head and 10 from the tail are displayed
    # with more than 200 rows of data if max_rows is 200 and min_rows is none 100 from the head and 100 from the tail will be displayed
    #pd.set_option("display.max_rows", 200)
    #pd.set_option("display.min_rows", None)

    tickerSymbol = "TSLA"
    # Print the sorted options chain
    # Print calls in ascending order of strike price
    # Print puts in ascending order of strike price
    print(Option.get_entire_sorted_options_chain(tickerSymbol))
    print("Price of the Underlying Asset: ", Option.get_currentPriceOfTheUnderlyingAsset(tickerSymbol))
    print("Expirations: \n", Option.get_expirations(tickerSymbol))
    print("Risk-Free Rate: ", Option.get_riskFreeRate(tickerSymbol))

    # Printing Call Getters
    print("\n** Call Getters **: \n")
    print("ITM_Minus_Call_Strike: ", Option.get_itm_call_minus_strike(tickerSymbol))
    print("ITM_Minus_Call_T:      ", Option.get_itm_call_minus_T(tickerSymbol))
    print("ITM_Minus_Call_Sigma:  ", Option.get_itm_call_minus_sigma(tickerSymbol))

    print("\nITM_Call_Strike: ", Option.get_itm_call_strike(tickerSymbol))
    print("ITM_Call_T:      ", Option.get_itm_call_T(tickerSymbol))
    print("ITM_Call_Sigma:  ", Option.get_itm_call_sigma(tickerSymbol))

    print("\nATM_Call_Strike: ", Option.get_atm_call_strike(tickerSymbol))
    print("ATM_Call_T:      ", Option.get_atm_call_T(tickerSymbol))
    print("ATM_Call_Sigma:  ", Option.get_atm_call_sigma(tickerSymbol))

    print("\nOTM_Call_Strike: ", Option.get_otm_call_strike(tickerSymbol))
    print("OTM_Call_T:      ", Option.get_otm_call_T(tickerSymbol))
    print("OTM_Call_Sigma:  ", Option.get_otm_call_sigma(tickerSymbol))

    print("\nITM_Plus_Call_Strike: ", Option.get_otm_call_plus_strike(tickerSymbol))
    print("ITM_Plus_Call_T:      ", Option.get_otm_call_plus_T(tickerSymbol))
    print("ITM_Plus_Call_Sigma:  ", Option.get_otm_call_plus_sigma(tickerSymbol))

    # Printing Put Getters
    print("\n** Put Getters **: \n")
    print("OTM_Plus_Put_Strike: ", Option.get_otm_put_plus_strike(tickerSymbol))
    print("OTM_Plus_Put_T:      ", Option.get_otm_put_plus_T(tickerSymbol))
    print("OTM_Plus_Put_Sigma:  ", Option.get_otm_put_plus_sigma(tickerSymbol))

    print("\nOTM_Put_Strike: ", Option.get_otm_put_strike(tickerSymbol))
    print("OTM_Put_T:      ", Option.get_otm_put_T(tickerSymbol))
    print("OTM_Put_Sigma:  ", Option.get_otm_put_sigma(tickerSymbol))

    print("\nATM_Put_Strike: ", Option.get_atm_put_strike(tickerSymbol))
    print("ATM_Put_T:      ", Option.get_atm_put_T(tickerSymbol))
    print("ATM_Put_Sigma:  ", Option.get_atm_put_sigma(tickerSymbol))

    print("\nITM_Put_Strike: ", Option.get_itm_put_strike(tickerSymbol))
    print("ITM_Put_T:      ", Option.get_itm_put_T(tickerSymbol))
    print("ITM_Put_Sigma:  ", Option.get_itm_put_sigma(tickerSymbol))

    print("\nITM_Minus_Put_Strike: ", Option.get_itm_put_minus_strike(tickerSymbol))
    print("ITM_Minus_Put_T:      ", Option.get_itm_put_minus_T(tickerSymbol))
    print("ITM_Minus_Put_Sigma:  ", Option.get_itm_put_minus_sigma(tickerSymbol))


# run test
if __name__ == "__main__":
    main()
