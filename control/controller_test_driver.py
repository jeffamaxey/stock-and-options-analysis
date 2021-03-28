"""
Author: Sahngwoo Kim, Adam Bouthillette

Description:
Run the main() function for testing.
"""


def main():
    """
    A test driver for the controller
    """
    from control import controller as c
    numError = 0

    # ------------------ test fundamental analysis with valid ticker ----------------------------------------
    result = None
    try:
        result = c.get_fundamental_analysis("AAPL", "Yahoo")
    except Exception:
        print("Test case 1 failed: get_fundamental_analysis() threw an unexpected exception with valid ticker.")
        numError += 1

    if result is None:
        print("Test case 2 failed: get_fundamental_analysis() returned None with valid ticker.")
        numError += 1

    general_keys = result.keys()
    if "stock_details" not in general_keys:
        print("Test case 3 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'stock_details'.")
        numError += 1

    if "metrics" not in general_keys:
        print("Test case 4 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'metrics'.")
        numError += 1

    if "dividends" not in general_keys:
        print("Test case 5 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'dividends'.")
        numError += 1

    if "income_statements" not in general_keys:
        print("Test case 6 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'income_statements'.")
        numError += 1

    # check if every key in the general keys contains values
    stock_details = result["stock_details"]
    metrics = result["metrics"]
    dividends = result["dividends"]
    income_statements = result["income_statements"]
    news = result["news"]

    for key in stock_details.keys():
        if stock_details[key] is None:
            print("Test case 7 failed. key '" + key + "' in stock_detail doesn't contain a value.")
            numError += 1

    for key in metrics.keys():
        if metrics[key] is None:
            print("Test case 8 failed. key '" + key + "' in metrics doesn't contain a value.")
            numError += 1

    for key in dividends.keys():
        if dividends[key] is None:
            print("Test case 9 failed. key '" + key + "' in dividends doesn't contain a value.")
            numError += 1

    for key in income_statements.keys():
        if income_statements[key] is None:
            print("Test case 10 failed. key '" + key + "' in income_statements doesn't contain a value.")
            numError += 1

    if news is None:
        print("Test case 11 failed. key 'news' doesn't contain a value.")
        numError += 1

    # ------------------ test fundamental analysis with invalid ticker ----------------------------------------
    try:
        result = c.get_fundamental_analysis("This is an invalid ticker", "Yahoo")
    except Exception:
        print("Test case 12 failed: get_fundamental_analysis() threw an unexpected exception with invalid ticker.")
        numError += 1

    if result is not None:
        print("Test case 13 failed: get_fundamental_analysis() didn't return None with invalid ticker.")
        numError += 1

    # ------------------ test technical analysis with valid ticker ----------------------------------------
    result = None
    try:
        result = c.get_technical_analysis("AAPL", "Yahoo")
    except Exception:
        print("Test case 14 failed: get_technical_analysis() threw an unexpected exception with valid ticker.")
        numError += 1

    if result is None:
        print("Test case 15 failed: get_technical_analysis() returned None with valid ticker.")
        numError += 1

    if "tech_details" not in general_keys:
        print(
            "Test case 16 failed: The analysis returned by get_technical_analysis() doesn't contain the key "
            "'tech_details'.")
        numError += 1

    # check if every key in the general keys contains values
    tech_details = result["tech_details"]
    summary = result["summary"]

    for key in tech_details.keys():
        if tech_details[key] is None:
            print("Test case 17 failed. key '" + key + "' in tech_detail doesn't contain a value.")
            numError += 1

    if summary is None:
        print("Test case 18 failed. key 'summary' doesn't contain a value.")
        numError += 1

    # print the final message
    if numError == 0:
        print("controller_test_driver: test successful!")
    else:
        print("controller_test_driver: number of test failed: " + str(numError))


if __name__ == "__main__":
    main()
