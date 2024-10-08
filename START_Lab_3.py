
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    if number <= cutoff:
        return True
    else:
        return False
    pass

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    if decimal_number > 0:
        return "positive"
    elif decimal_number < 0:
        return "negative"
    elif decimal_number == 0:
        return "zero"
    else:
        return "invalid"
    pass

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    if 2001 <= year <= 2100:
        return "21st century"
    elif 1901 <= year <= 2000:
        return "20th century"
    elif 1801 <= year <= 1900:
        return "19th century"
    elif year <= 1800:
        return "ancient"
    else:
        return "invalid"
    pass

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    num = [number_1, number_2, number_3]
    try:
        for x in num: int(x)
    except ValueError:
        return None
    else:
        return max(num)
    pass

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid

    if scale_used == "C":
        if 0 <= temperature <= 100:
            return "Liquid"
        elif temperature <= 0:
            return "Solid"
        elif temperature >= 100:
            return "Gas"
        else:
            return "Invalid"
    elif scale_used == "F":
        if 32 <= temperature <= 212:
            return "Liquid"
        elif temperature <= 32:
            return "Solid"
        elif temperature >= 212:
            return "Gas"
        else:
            return "Invalid"
    else:
        return "Invalid"
    pass
    
