# Task 1: Access Elements
#
# You have a tuple:
#
# data = (10, 20, 30, 40)
#
# Print:
#
# the first element
# the last element

print('-' * 10, 'Task 1:', sep='\n')

data = (10, 20, 30, 40)

print('The first/last elements:', data[0], data[3])

# Task 2: Length
#
# You have a tuple:
#
# data = (5, 15, 25, 35, 45)
#
# Print the length of the tuple

print('-' * 10, 'Task 2:', sep='\n')

data = (5, 15, 25, 35, 45)

print('Length:', len(data))

# Task 3: Loop Through Tuple
#
# You have a tuple:
#
# data = ('a', 'b', 'c')
#
# Print all elements using a for loop

print('-' * 10, 'Task 3:', sep='\n')

data = ('a', 'b', 'c')

for i in data:
    print(i)

print('Result: done')

# Task 4: Count Element
#
# You have a tuple:
#
# data = (1, 2, 2, 3, 2, 4)
#
# Count how many times the number 2 appears
# without using .count()

print('-' * 10, 'Task 4:', sep='\n')

data = (1, 2, 2, 3, 2, 4)

number_2 = 0

for number in data:
    if number == 2:
        number_2 += 1

print('Number 2 appears:', number_2)

# Task 5: Find Maximum
#
# You have a tuple:
#
# data = (10, 5, 20, 3)
#
# Find the largest number
# without using max()

print('-' * 10, 'Task 5:', sep='\n')

data = (10, 5, 20, 3)

largest_number = data[0]

for number in data:
    if number > largest_number:
        largest_number = number

print('Largest number:', largest_number)

# Task 6: Tuple → List
#
# You have a tuple:
#
# data = (1, 2, 3, 4)
#
# Convert it to a list
# Add number 5
# Print the result

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
# Given a tuple:
# (10, 20, 30)
#
# Task:
# unpack into variables:
# a, b, c

print('-' * 10, 'Task 7:', sep='\n')

numbers = (10, 20, 30)
a, b, c = numbers

print('a:', a,'b:',  b, 'c:', c)

# Task 8: Swap Values
# Given:
# a = 5
# b = 10
#
# Task:
# swap values
# without using a temporary variable

print('-' * 10, 'Task 8:', sep='\n')

a = 5
b = 10

a, b = b, a

print('a:', a, 'b:', b)

# Task 9: Slice Tuple
# Given a tuple:
# (1, 2, 3, 4, 5, 6)
#
# Task:
# get only even-index elements (0, 2, 4...)
#
# Result:
# (1, 3, 5)

print('-' * 10, 'Task 9:', sep='\n')

numbers_1 = (1, 2, 3, 4, 5, 6)
number_2 = numbers_1[::2]

print('Result:', number_2)

# Task 10: There are two tuples with average daily temperatures and a tuple of days of the week.
# They are the same length, essentially just a temperature-day-of-week correspondence.
# They need to be output to the terminal like this:
# Mon: 12 °C

print('-' * 10, 'Task 10:', sep='\n')

temps = (12, 15, 14, 10, 9, 11, 13)
week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

index = 0

while index < len(temps):
    print(f'{week[index]}: {temps[index]} °C')
    index += 1

# Task 11: This task is essentially the same as the previous one. Just for reinforcement.
# There are two tuples: a currency and today's (fictitious) exchange rate.
# You need to produce an output in the following format:
# USD | 193.00

print('-' * 10, 'Task 11:', sep='\n')

currencies = ('USD', 'EUR', 'GBP', 'JPY', 'CNY')
rates = (193, 220, 215, 1.63, 15.8)

index = 0

while index < len(currencies):
    print(f'{currencies[index]} | {rates[index]}')
    index += 1
