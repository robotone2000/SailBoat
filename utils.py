

def placeRound(measure, nDigits = 2):
    rounded = round(measure * pow(10, nDigits)) / pow(10, nDigits)
    return rounded

def angleMod(someAngle, makePos=1):

    someAngle %= (TWO_PI)

    if (makePos==1):
        while (someAngle < 0):
            someAngle += TWO_PI

    return someAngle
