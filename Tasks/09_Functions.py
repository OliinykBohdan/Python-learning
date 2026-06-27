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

# Task 11: Write a function called filter_numbers that takes a tuple (or list)
# of numbers and returns a filtered list according to the following rules:
#
# - A tuple of numbers is passed to the function.
# - The new list, which is defined within the function, must contain only values from a specified range,
# which can also be passed as arguments to the function
# (for example, the new list must contain only numbers from 1 to 100). By default, the range is set to 0 to 100.
# - The function returns this new list as its result.
# - Before returning the new list, it must be sorted.
# - The function must also have two additional optional arguments:
# sort in descending order and include only even numbers.
# List:
# numbers = (1, 4, 12, 98, 102, -5, 0, 77, 88)
# An example of the desired behaviour:
# [0, 1, 4, 12, 77, 88, 98]

print('-' * 10, 'Task 11:', sep='\n')


def filter_numbers(nums, min_value=0, max_value=100, reverse=False, even_only=False):
    filter_nums = []

    for num in nums:
        if num in range(min_value, max_value):
            if even_only:
                if num % 2 == 0:
                    filter_nums.append(num)
            else:
                filter_nums.append(num)

    if reverse:
        filter_nums.sort()
        filter_nums.reverse()
    else:
        filter_nums.sort()

    return filter_nums


numbers = (1, 4, 12, 98, 102, -5, 0, 77, 88)

new_numbers = filter_numbers(numbers)

print('Filtered list:', new_numbers)

# Task 12: List transformation
#
# Description:
# 
# - A one-dimensional list is provided as input.
# - The output must be the same list object, but modified.
# - Nested lists must contain three elements each.
# - If there are not enough elements to complete the last nested list, add the remaining elements.
# - The number of elements in the nested lists must be passed as a parameter; the default is 3.
# - The function need not return a value (as the list itself is being modified). It would be good to return 'True' on success and 'False' if the list passed in was empty.

print('-' * 10, 'Task 12:', sep='\n')

data = [33, 34, 32, 24, 22, 25, 26, 26, 27, 51, 53]


def to_matrix(arr, columns=3):
    if len(arr) == 0:
        return False

    temp_data = []
    start = 0
    stop = columns

    while start < len(arr):
        part = arr[start:stop]

        if part:
            temp_data.append(part)

        if len(part) < columns:
            break

        start = stop
        stop += columns

    arr.clear()
    return arr.extend(temp_data)


to_matrix(data)
print('Result:', data)

# Task 13: Transaction History
#
# Create a function:
# show_history(history)
#
# Example input:
# history = [
#     'Deposit: 100',
#     'Withdraw: 50',
#     'Deposit: 200'
# ]
#
# The function should print all transactions.
#
# If the history is empty:
# No transactions found.

print('-' * 10, 'Task 13:', sep='\n')


def show_history(history):
    if not history:
        print('No transactions found.')
        return

    count = 1
    print('===== TRANSACTION HISTORY =====')
    for transaction in history:
        print(f'{count}. {transaction}')
        count += 1


show_history([
    'Deposit: 100',
    'Withdraw: 50',
    'Deposit: 200'
])

# Task 14: Statistics
#
# Create a function:
# get_stats(numbers)
#
# Return:
# (min_number, max_number, average)
#
# Example:
# get_stats((10, 20, 30))
#
# Expected result:
# (10, 30, 20)
#
# Do not use:
# min()
# max()
# sum()

print('-' * 10, 'Task 14:', sep='\n')


def get_stats(list_numbers):
    min_number = numbers[0]
    max_number = numbers[0]
    total = 0

    for num in list_numbers:
        if num < min_number:
            min_number = num

        if num > max_number:
            max_number = num

        total += num

    average = round(total / len(list_numbers), 2)
    return min_number, max_number, average


print(get_stats((10, 20, 30)))

# Task 15: Average of arguments 1
# Implement a generic function average_value that calculates the arithmetic mean of all the arguments passed to it. The function must accept:
# - an arbitrary number of positional arguments (*args);
# - an optional named argument rounding (with a default value of 2), which controls the rounding of the result;
# - return the result;
# - if the function is called without any arguments, return None.

print('-' * 10, 'Task 15:', sep='\n')

temps_celsius = [-1.5, 0.2, 2.8, 5.6, 8.4, 11.2, 14.7, 17.0, 18.3, 19.1, 19.4, 18.8, 17.0, 14.5, 11.2, 7.8, 4.0]


def average_value(*args, rounding=2):
    if not args:
        return None

    total = 0

    for arg in args:
        total += arg

    average = total / len(args)
    return round(average, rounding)


print('Average temperature value:', average_value(*temps_celsius))

# Task 16: Average of arguments 2
# Calculate the overall arithmetic mean of these temperature values, but they are not stored in a single
# one-dimensional list, instead, they are in the following format:

print('-' * 10, 'Task 16:', sep='\n')

temp_groups = [
    [12.4, 13.6, 15.1],
    [8.3, 9.1],
    [20.0],
    [],
    [0, -2, 4, 5]
]


def average_value(*args, rounding=2):
    if not args:
        return None

    total = 0
    total_value = 0

    for arg in args:
        total_value += len(arg)

        for value in arg:
            total += value

    if total_value == 0:
        return None

    average = total / total_value
    return round(average, rounding)


print('Average temperature value:', average_value(*temp_groups))

# Task 17: New ATM
#
# The function must return a new list containing the quantities of banknotes required
# to dispense the requested amount to the customer.
#
# Conditions:
# 1) The quantities of banknotes of a specific denomination must appear in the
# same order in the new list as in the banknotes_in_atm list.
# 2) If there are 0 banknotes of a particular denomination, it should still be added to the list.
# 3) The quantities of banknotes for each denomination are calculated according
# to the principle of dispensing the largest possible denominations.

print('-' * 10, 'Task 17:', sep='\n')

cash = 350
banknotes_in_atm = [100, 50, 20, 5, 1]


def get_banknote_counts(values, banknotes_list):
    banknotes_counts = []

    for banknote in banknotes_list:
        counter = 0

        while values >= banknote:
            counter += 1
            values -= banknote

        banknotes_counts.append(counter)

    return banknotes_counts


print(get_banknote_counts(cash, banknotes_in_atm))
