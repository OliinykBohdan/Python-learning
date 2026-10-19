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

# Task 3: Command Calculator
#
# Description:
# Given a starting value and a list of commands:
# value = 10
# commands = ['ADD 5', 'MUL 2', 'SUB 4', 'DIV 2']
#
# Write a function:
# execute_commands(value, commands)
#
# Execute commands from left to right.
# Supported operations:
# ADD x — add x;
# SUB x — subtract x;
# MUL x — multiply by x;
# DIV x — divide by x.
#
# Example:
# 10 -> 15 -> 30 -> 26 -> 13
# Result: 13
#
# Conditions:
# - x may be an int or float written as text;
# - skip unknown commands and count them as errors;
# - skip commands with an invalid number;
# - skip DIV 0;
# - do not modify the original commands list.
#
# Bonus:
# return (result, error_count), where error_count is
# the number of skipped invalid commands.

print('-' * 10, 'Task 3:', sep='\n')

value = 10
commands = ['ADD 5', 'MUL 2', 'SUB 4', 'DIV 2']


def execute_commands(value, commands):
    error_count = 0
    result = value

    for command in commands:
        try:
            if command[:3] == 'ADD':
                result += float(command[4:])
            elif command[:3] == 'MUL':
                result = result * float(command[4:])
            elif command[:3] == 'SUB':
                result -= float(command[4:])
            elif command[:3] == 'DIV':
                result = result / float(command[4:])
            else:
                error_count += 1

        except ValueError, ZeroDivisionError:
            error_count += 1

    return result, error_count


print('Result:', execute_commands(value, commands))
