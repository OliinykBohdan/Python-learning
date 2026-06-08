# Task 1: Print All Elements
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Print all elements of the list using a for loop

print('-' * 10, 'Task 1:', sep='\n')

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print('Result: done')

# Task 2: Sum of List
#
# You have a list:
#
# numbers = [2, 4, 6, 8]
#
# Find the sum of all elements (without using sum())

print('-' * 10, 'Task 2:', sep='\n')

numbers = [2, 4, 6, 8]
total = 0

for number in numbers:
    total += number

print('Sum of all elements:', total)

# Task 3: Find Maximum
#
# You have a list:
#
# numbers = [10, 3, 7, 25, 1]
#
# Find the largest number (without using max())

print('-' * 10, 'Task 3:', sep='\n')

numbers = [10, 3, 7, 25, 1]
largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print('The largest of the number:', largest_number)

# Task 4: Filter Even Numbers
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# Create a new list with only even numbers

print('-' * 10, 'Task 4:', sep='\n')

numbers = [1, 2, 3, 4, 5, 6]
numbers_even = []

for number in numbers:
    if number % 2 == 0:
        numbers_even.append(number)

print('Even numbers of the list:', numbers_even)

# Task 5: Count Occurrences
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 2, 4]
#
# Count how many times the number 2 appears

print('-' * 10, 'Task 5:', sep='\n')

numbers = [1, 2, 2, 3, 2, 4]
number2 = 0

for number in numbers:
    if number == 2:
        number2 += 1

print('Number 2 appears of the list:', number2)

# Task 6: Reverse List
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Create a new list in reverse order
# without using reverse() and without slicing [::-1]

print('-' * 10, 'Task 6:', sep='\n')

numbers = [1, 2, 3, 4, 5]
reversed_list = []

for number in range (4, -1, -1):
    reversed_list.append(numbers[number])

print('Reversed list:', reversed_list)

# Task 7: Remove Duplicates (keep order)
# Given a list:
# [1, 2, 2, 3, 1, 4]
#
# Task:
# remove duplicates
# but keep the original order
#
# Result:
# [1, 2, 3, 4]
#
# hint: do NOT use set() directly

print('-' * 10, 'Task 7:', sep='\n')

numbers = [1, 2, 2, 3, 1, 4]
numbers_1 = []

for number in numbers:
    if number not in numbers_1:
        numbers_1.append(number)

print('Numbers without duplicates:', numbers_1)

# Task 8: Find Second Largest
# Given a list of numbers
#
# Task:
# find the second largest number
#
# hint:
#
# use sort
# or max + remove

print('-' * 10, 'Task 8:', sep='\n')

numbers = [1, 2, 2, 3, 1, 4]

unique_list = list(set(numbers))
unique_list.sort()

second_largest = unique_list[-2]

print('Second largest number:', second_largest)

# Task 9: Reverse List (Slicing)
# Given a list:
# [1, 2, 3, 4, 5]
#
# Task:
# reverse the list using slicing
#
# Result:
# [5, 4, 3, 2, 1]

print('-' * 10, 'Task 9:', sep='\n')

numbers = [1, 2, 3, 4, 5]
reverse_numbers = numbers[::-1]

print('Reversed numbers:', reverse_numbers)

# Task 10: Extract Middle Part
# Given a list:
# [10, 20, 30, 40, 50, 60]
#
# Task:
# get elements from index 1 to index 4 (inclusive of start, exclusive of end)
#
# Result:
# [20, 30, 40, 50]

print('-' * 10, 'Task 10:', sep='\n')

numbers_1 = [10, 20, 30, 40, 50, 60]
numbers_2 = numbers_1[1:5]

print('Result:', numbers_2)

# Task 11: There is a price list.
# Need to apply a 10% discount to each price and create a new list with the resulting amounts.

print('-' * 10, 'Task 11:', sep='\n')

prices = [2332.25, 24.55, 96.94, 652.54]
discount_prices = []

discount = 10
index = 0

while index < len(prices):
    discount_prices.append(prices[index] - prices[index] * discount / 100)

    index += 1

print('Prices:', prices, '\nDiscount prices:', discount_prices)

# Task 12: There is a list of prices collected from the site.
# This list should contain prices converted to float type.
# Do not add empty lines.

print('-' * 10, 'Task 12:', sep='\n')

scraped_prices = ['100,50', '5,80', '', '', '25,99', '', '17,50', '0,95', '99,00']
normalized_price_list = []

index = 0

while index < len(scraped_prices):
    if scraped_prices[index]:
        normalized_price_list.append(float(scraped_prices[index].replace(',', '.')))

    index += 1

print('Normalized price list:', normalized_price_list)
