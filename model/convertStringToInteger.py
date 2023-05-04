from numpy import double


def convertStringToInteger(stringVal):
    """
        A simple script used to convert a string integer ending in (K,M,B,T) to an integer value
        For example a string value 1.1M represents 1.1 million and will be converted to 1100000
        :return the integer representation of a string number
        :throws runtime error if the parameter stringVal is not a string
        """
    if type(stringVal) != str:
        raise RuntimeError

    if stringVal.endswith('K') or stringVal.endswith('M') or stringVal.endswith('B') or stringVal.endswith('T'):
        # determine multiplier
        multiplier = 0
        if stringVal.endswith('K'):
            multiplier = 10 ** 3
            stringVal = stringVal[:-1]
        elif stringVal.endswith('M'):
            multiplier = 10 ** 6
            stringVal = stringVal[:-1]
        elif stringVal.endswith('B'):
            multiplier = 10 ** 9
            stringVal = stringVal[:-1]
        elif stringVal.endswith('T'):
            multiplier = 10 ** 12
            stringVal = stringVal[:-1]

        # convert value to float, multiply, then convert the result to int
        return int(double(stringVal) * multiplier)

    else:
        return

# x= "11M"
# x = convertStringToInteger(x)
# print(x)