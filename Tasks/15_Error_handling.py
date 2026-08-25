# Task 1: Temperature Conversion
#
# Description:
# Create a function that converts a temperature from Celsius to Fahrenheit.
# Raise a TypeError if the provided value is not a number.
# Raise a ValueError if the temperature is lower than absolute zero (-273.15°C).
# The function should also reject boolean values.

print('-' * 10, 'Task 1:', sep='\n')


def convert_temperature(temp_celsius: int |float, /):
    if not isinstance(temp_celsius, int |float) or type(temp_celsius) is bool:
        raise TypeError('temperature must be a number')

    if temp_celsius < -273.15:
        raise ValueError('temperature cannot be lower than absolute zero')

    return temp_celsius * 9 / 5 + 32


print('Temperature in degrees Fahrenheit:', convert_temperature(1))

# Task 2: Functions + error handling
#
# Description:
# Create a function divide_numbers(a, b) that returns the result of dividing a by b.
#
# The function should:
# - accept only int or float values;
# - reject boolean values;
# - raise TypeError if one of the arguments is not a number;
# - raise ZeroDivisionError if b == 0;
# - return the division result if all conditions are valid.

print('-' * 10, 'Task 2:', sep='\n')


def divide_numbers(a, b):
    if not isinstance(a, int |float) or not isinstance(b, int |float)\
            or isinstance(a, bool) or isinstance(b, bool):
        raise TypeError('not a number entered')

    if b == 0:
        raise ZeroDivisionError('division by zero')

    return round(a / b, 2)


print('Result:', divide_numbers(121, 3))
