"""
Author: Sahngwoo Kim

Description:
Run the main() function for testing.
If the test is successful, no message will be printed to the console.
"""


def main():
    """
    A test driver for the controller
    """
    import controller as c

    # ------------------ test fundamental analysis with valid ticker ----------------------------------------
    result = None
    try:
        result = c.get_fundamental_analysis("AAPL", "Yahoo")
    except Exception:
        print("Test case 1 failed: get_fundamental_analysis() threw an unexpected exception with valid ticker.")

    if result is None:
        print("Test case 2 failed: get_fundamental_analysis() returned None with valid ticker.")

    general_keys = result.keys()
    if "stock_details" not in general_keys:
        print("Test case 3 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'stock_details'.")

    if "metrics" not in general_keys:
        print("Test case 4 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'metrics'.")

    if "dividends" not in general_keys:
        print("Test case 5 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'dividends'.")

    if "income_statements" not in general_keys:
        print("Test case 6 failed: The analysis returned by get_fundamental_analysis() doesn't contain the key 'income_statements'.")

    # check if every key in the general keys contains values
    stock_details = result["stock_details"]
    metrics = result["metrics"]
    dividends = result["dividends"]
    income_statements = result["income_statements"]
    news = result["news"]

    for key in stock_details.keys():
        if stock_details[key] is None:
            print("Test case 7 failed. key '" + key + "' in stock_detain doesn't contain a value.")

    for key in metrics.keys():
        if metrics[key] is None:
            print("Test case 8 failed. key '" + key + "' in metrics doesn't contain a value.")

    for key in dividends.keys():
        if dividends[key] is None:
            print("Test case 9 failed. key '" + key + "' in dividends doesn't contain a value.")

    for key in income_statements.keys():
        if income_statements[key] is None:
            print("Test case 10 failed. key '" + key + "' in income_statements doesn't contain a value.")

    if news is None:
        print("Test case 11 failed. key 'news' doesn't contain a value.")

    # ------------------ test fundamental analysis with invalid ticker ----------------------------------------
    try:
        result = c.get_fundamental_analysis("This is an invalid ticker", "Yahoo")
    except Exception:
        print("Test case 12 failed: get_fundamental_analysis() threw an unexpected exception with invalid ticker.")

    if result is not None:
        print("Test case 13 failed: get_fundamental_analysis() didn't return None with invalid ticker.")


if __name__ == "__main__":
    main()
