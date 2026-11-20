# Task 1: Access Elements
#
# Description:
# Given:
# data = (10, 20, 30, 40)
#
# Print:
# - the first element of the tuple;
# - the last element of the tuple.
#
# Use tuple indexing.

print('-' * 10, 'Task 1:', sep='\n')

data = (10, 20, 30, 40)

print('The first/last elements:', data[0], data[3])

# Task 2: Tuple Length
#
# Description:
# Given:
# data = (5, 15, 25, 35, 45)
#
# Find and print the number
# of elements in the tuple.
#
# Use len().

print('-' * 10, 'Task 2:', sep='\n')

data = (5, 15, 25, 35, 45)

print('Length:', len(data))

# Task 3: Loop Through Tuple
#
# Description:
# Given:
# data = ('a', 'b', 'c')
#
# Go through the tuple
# using a for loop.
#
# Print each element
# on a separate line.

print('-' * 10, 'Task 3:', sep='\n')

data = ('a', 'b', 'c')

for i in data:
    print(i)

print('Result: done')

# Task 4: Count Element
#
# Description:
# Given:
# data = (1, 2, 2, 3, 2, 4)
#
# Count how many times
# the number 2 appears in the tuple.
#
# Do not use .count().
#
# Store the result in a variable
# and print it.

print('-' * 10, 'Task 4:', sep='\n')

data = (1, 2, 2, 3, 2, 4)

number_2 = 0

for number in data:
    if number == 2:
        number_2 += 1

print('Number 2 appears:', number_2)

# Task 5: Find Maximum
#
# Description:
# Given:
# data = (10, 5, 20, 3)
#
# Find the largest number
# in the tuple.
#
# Do not use max().
#
# Store the result in a variable
# and print it.

print('-' * 10, 'Task 5:', sep='\n')

data = (10, 5, 20, 3)

largest_number = data[0]

for number in data:
    if number > largest_number:
        largest_number = number

print('Largest number:', largest_number)

# Task 6: Tuple to List
#
# Description:
# Given:
# data = (1, 2, 3, 4)
#
# Convert the tuple to a list.
#
# Add the number 5
# to the end of the list.
#
# Print the final list.

print('-' * 10, 'Task 6:', sep='\n')

data = (1, 2, 3, 4)

list1 = []

for number in data:
    list1.append(number)

list1.append(5)

print('Converted list:', list1)

# or
#
# list1 = list(data)
#
# list1.append(5)
#
# print('Converted list:', list1)

# Task 7: Unpack Tuple
#
# Description:
# Given:
# numbers = (10, 20, 30)
#
# Unpack the tuple into
# three separate variables:
# a, b, c.
#
# Print the value
# of each variable.

print('-' * 10, 'Task 7:', sep='\n')

numbers = (10, 20, 30)
a, b, c = numbers

print('a:', a,'b:',  b, 'c:', c)

# Task 8: Swap Values
#
# Description:
# Given:
# a = 5
# b = 10
#
# Swap the values of a and b
# without using a temporary variable.
#
# Use tuple unpacking.
#
# Print the values
# after the swap.

print('-' * 10, 'Task 8:', sep='\n')

a = 5
b = 10

a, b = b, a

print('a:', a, 'b:', b)

# Task 9: Slice Tuple
#
# Description:
# Given:
# numbers = (1, 2, 3, 4, 5, 6)
#
# Create a new tuple containing
# only the elements at even indexes:
# 0, 2, 4, ...
#
# Use tuple slicing.
#
# Print the resulting tuple.

print('-' * 10, 'Task 9:', sep='\n')

numbers_1 = (1, 2, 3, 4, 5, 6)
number_2 = numbers_1[::2]

print('Result:', number_2)

# Task 10: Average Daily Temperatures
#
# Description:
# Given:
# - a tuple of weekdays;
# - a tuple of average daily temperatures.
#
# Both tuples have the same length.
# Each temperature corresponds to the weekday
# at the same position.
#
# Print each weekday together
# with its corresponding temperature.
#
# Use zip() to combine the tuples.
#
# Output format:
# Mon: 12 °C
# Tue: 15 °C
# ...

print('-' * 10, 'Task 10:', sep='\n')

temps = (12, 15, 14, 10, 9, 11, 13)
week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

index = 0

while index < len(temps):
    print(f'{week[index]}: {temps[index]} °C')
    index += 1

# Task 11: Exchange Rate
#
# Description:
# Given:
# - a tuple of currency codes;
# - a tuple of corresponding exchange rates.
#
# Both tuples have the same length.
# Each rate corresponds to the currency
# at the same position.
#
# Print each currency together
# with its corresponding exchange rate.
#
# Output format:
# USD | 193.00
# EUR | 220.00
# ...

print('-' * 10, 'Task 11:', sep='\n')

currencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')
rates = (193, 220, 215, 1.63, 15.8)

index = 0

while index < len(currencies):
    print(f'{currencies[index]} | {rates[index]}')
    index += 1
