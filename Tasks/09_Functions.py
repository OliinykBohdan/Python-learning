# Task 1: Simple Function
# Description:
#
# Create a function that:
#
# takes a name as a parameter
# prints: 'Hello, <name>!'

print('-' * 10, 'Task 1:', sep='\n')

def name(x):
    print(f'Hello, {x}!')

name('Bohdan')

# Task 2: Return Sum
#  Description:
#
# Create a function that:
#
# takes two numbers
# returns their sum
#
# Print the result outside the function

print('-' * 10, 'Task 2:', sep='\n')

def sum_numbers(x, y):
    return x + y

print(sum_numbers(7, 9))
print(sum_numbers(10, 2))

# Task 3: Even or Odd (Function)
# Description:
#
# Create a function that:
#
# takes a number
# returns 'even' or 'odd'
#
# Use return, not print

print('-' * 10, 'Task 3:', sep='\n')

def number(x):
    if x % 2 == 1:
        return 'odd'
    else:
        return 'even'

print(number(12))
print(number(11))

# Task 4: Max of Three
# Description:
#
# Create a function that:
#
# takes three numbers
# returns the largest number
#
# Do NOT use max()

print('-' * 10, 'Task 4:', sep='\n')

def largest_number (x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

print(largest_number(50, 60, 100))
print(largest_number(10, 1700, 220))

# Task 5: Shopping Cart Total (Function)
# Description:
#
# You have:
#
# cart = {
#     'apple': 2,
#     'banana': 3
# }
#
# price = {
#     'apple': 3,
#     'banana': 2
# }
#
# Create a function that:
#
# takes cart and price
# returns total price
#
# Call the function and print result

print('-' * 10, 'Task 5:', sep='\n')

cart = {
    'apple': 2,
    'banana': 3
}
price = {
    'apple': 3,
    'banana': 2
}

def total_price(x, y):
    total = 0
    for key, value in x.items():
        total += value * y[key]
    return total

print (total_price(cart, price))

# Task 6: Password Check (Function + Loop)
# Description:
#
# Create a function that:
#
# asks the user for a password
# has 3 attempts
#
# Rules:
#
# correct → return 'Access granted'
# wrong → ask again
# after 3 attempts → return 'Access denied'

print('-' * 10, 'Task 6:', sep='\n')

def passwords ():
    attempts = 0
    while True:
        x = input('Enter password: ')

        if x == '1111':
            return 'Access granted'
        else:
            attempts += 1
            print('Incorrect password')

        if attempts == 3:
            return 'Access denied'

print(passwords())

# Task 7: Count Elements (Function + Dict)
# Description:
#
# Create a function that:
#
# takes a list
# returns a dictionary where:
# key → element
# value → how many times it appears

print('-' * 10, 'Task 7:', sep='\n')

numbers = [1, 2, 2, 3, 1]

def count_elements(number):
    result = {}
    for x in number:
        result[x] = result.get(x, 0) + 1
    return result

print(count_elements (numbers))

# Task 8: Filter Greater Than (Function + List)
# Description:
#
# Create a function that:
#
# takes a list and a number n
# returns a new list with elements greater than n

print('-' * 10, 'Task 8:', sep='\n')

numbers = [1, 5, 8, 2, 10]
n = 5

def greater_than_n (x, y):
    numbers_greater = []
    for i in x:
        if i > y:
            numbers_greater.append(i)
    return numbers_greater

print(greater_than_n (numbers, n))

# Task 9: Mini Calculator (Function + Logic)
# Description:
#
# Create a function that:
#
# takes:
# two numbers
# an operator ('+', '-', '*', '/')
# returns the result

print('-' * 10, 'Task 9:', sep='\n')

def calculator(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return 'Error'
        return x / y
    else:
        return 'Error'

print(calculator (5, 4, '+'))
print(calculator (5, 4, '-'))
print(calculator (5, 4, '*'))
print(calculator (5, 0, '/'))

# Task 10: There is a list of values in degrees Celsius:
# temps_celsius = [-1.5, 0.2, 2.8, 5.6, 8.4, 11.2,
#                 14.7, 17.0, 18.3, 19.1, 19.4, 18.8,
#                 17.0, 14.5, 11.2, 7.8, 4.0, -300]
#
# Need to populate the new list with values in Fahrenheit:
# temps_fahrenheit = []

print('-' * 10, 'Task 10:', sep='\n')


def convert_temperature(temps_cel):
    temps_fahrenheit = []

    for temp in temps_cel:
        if temp < -273.15:
            new_temp = False
            temps_fahrenheit.append(new_temp)
        else:
            new_temp = temp * 9 / 5 + 32
            temps_fahrenheit.append(round(new_temp, 1))

    return temps_fahrenheit


temps_celsius = [-1.5, 0.2, 2.8, 5.6, 8.4, 11.2,
                14.7, 17.0, 18.3, 19.1, 19.4, 18.8,
                17.0, 14.5, 11.2, 7.8, 4.0, -300]

print(f'Celsius: {temps_celsius}',
      f'Fahrenheit: {convert_temperature(temps_celsius)}', sep='\n')
