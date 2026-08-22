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