# Task 1: Print All Elements
#
# Description:
# numbers = [1, 2, 3, 4, 5]
#
# Print all elements of the list using a for loop.

print('-' * 10, 'Task 1:', sep='\n')

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print('Result: done')

# Task 2: Sum of List
#
# Description:
# numbers = [2, 4, 6, 8]
#
# Find the sum of all elements (without using sum()).

print('-' * 10, 'Task 2:', sep='\n')

numbers = [2, 4, 6, 8]
total = 0

for number in numbers:
    total += number

print('Sum of all elements:', total)

# Task 3: Find Maximum
#
# Description:
# numbers = [10, 3, 7, 25, 1]
#
# Find the largest number (without using max()).

print('-' * 10, 'Task 3:', sep='\n')

numbers = [10, 3, 7, 25, 1]
largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print('The largest of the number:', largest_number)

# Task 4: Filter Even Numbers
#
# Description:
# numbers = [1, 2, 3, 4, 5, 6]
#
# Create a new list with only even numbers.

print('-' * 10, 'Task 4:', sep='\n')

numbers = [1, 2, 3, 4, 5, 6]
numbers_even = []

for number in numbers:
    if number % 2 == 0:
        numbers_even.append(number)

print('Even numbers of the list:', numbers_even)

# Task 5: Count Occurrences
#
# Description:
# numbers = [1, 2, 2, 3, 2, 4]
#
# Count how many times the number 2 appears.

print('-' * 10, 'Task 5:', sep='\n')

numbers = [1, 2, 2, 3, 2, 4]
number2 = 0

for number in numbers:
    if number == 2:
        number2 += 1

print('Number 2 appears of the list:', number2)

# Task 6: Reverse List
#
# Description:
# numbers = [1, 2, 3, 4, 5]
#
# Create a new list in reverse order without using reverse() and without slicing [::-1].

print('-' * 10, 'Task 6:', sep='\n')

numbers = [1, 2, 3, 4, 5]
reversed_list = []

for number in range (4, -1, -1):
    reversed_list.append(numbers[number])

print('Reversed list:', reversed_list)

# Task 7: Remove Duplicates (keep order)
#
# Description:
# [1, 2, 2, 3, 1, 4]
#
# Remove duplicates, but keep the original order.
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

# Task 8: Second Largest
#
# Description:
# Find the second largest number in list.
#
# hint:
# use sort
# or max + remove

print('-' * 10, 'Task 8:', sep='\n')

numbers = [1, 2, 2, 3, 1, 4]

unique_list = list(set(numbers))
unique_list.sort()

second_largest = unique_list[-2]

print('Second largest number:', second_largest)

# Task 9: Reverse List (Slicing)
#
# Description:
# [1, 2, 3, 4, 5]
#
# Reverse the list using slicing.
#
# Result:
# [5, 4, 3, 2, 1]

print('-' * 10, 'Task 9:', sep='\n')

numbers = [1, 2, 3, 4, 5]
reverse_numbers = numbers[::-1]

print('Reversed numbers:', reverse_numbers)

# Task 10: Extract Middle Part
#
# Description:
# [10, 20, 30, 40, 50, 60]
#
# Get elements from index 1 to index 4 (inclusive of start, exclusive of end).
#
# Result:
# [20, 30, 40, 50]

print('-' * 10, 'Task 10:', sep='\n')

numbers_1 = [10, 20, 30, 40, 50, 60]
numbers_2 = numbers_1[1:5]

print('Result:', numbers_2)

# Task 11: There is a price list.
#
# Description:
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

# Task 12: List of prices
#
# Description:
# There is a list of prices collected from the site.
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

# Task 13: New subscribers
#
# Description:
# There is a list showing the number of new subscribers by day over the course of a week
# (for 6 days excluding Sunday), and the days of the week themselves are in a tuple.
#
# Need to output a chart (roughly) like this to the terminal, with progress bars
# (the ‘#’ symbols act as a scale in percentages of the maximum value – this is the progress bar):
#
# Mon: ##################### (30)
# Tue: ###########__________ (15)
# Wed: #____________________ ( 1)
# Thu: #################____ (25)
# Fri: ####_________________ ( 5)
# Sat: ###################__ (28)

print('-' * 10, 'Task 13:', sep='\n')

subs = [30, 15, 1, 25, 5, 28]
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

max_day = max(subs)

index = 0

while index < len(days):
    percent = subs[index] * 100 / max_day
    scale = round(20 * percent / 100) * '#' + round(20 * (100 - percent) / 100) * '_'

    print(f'{days[index]}: {scale} ({subs[index]})')

    index += 1

# Task 14: Sorting codes
#
# Description:
# There are two lists containing country codes and product codes.
# Product codes must be sorted by country code.
#
# Expected output:
# 754: 7547682958186 7543817559796 7544194259711
# 690: 6900626469201 6900590565047 6901237511586 6901237511587
# 450: 4506436054267 4502714135954 4500295752923

print('-' * 10, 'Task 14:', sep='\n')

country_codes = ['754', '690', '450']

products = ['4506436054267', '7547682958186', '6900626469201',
            '7543817559796', '7544194259711', '6900590565047',
            '6901237511586', '4502714135954', '4500295752923',
            '6901237511587']

for country_code in country_codes:
    print(f'{country_code}: ', end = '')

    for code in products:
        if country_code in code:
            print(code, end=' ')

    print()

print('Result: done')

# Task 15: Sorting codes
#
# Description:
# The same two lists are given as in the previous task.
# A new categories list needs to be created, containing sub-lists,
# each of which will contain barcodes specific to a particular country.
#
# Expected output:
# [['7547682958186', '7543817559796', '7544194259711'], ['6900626469201', '6900590565047',
# '6901237511586', '6901237511587'], ['4506436054267', '4502714135954', '4500295752923']]

print('-' * 10, 'Task 15:', sep='\n')

country_codes = ['754', '690', '450']

products = ['4506436054267', '7547682958186', '6900626469201',
            '7543817559796', '7544194259711', '6900590565047',
            '6901237511586', '4502714135954', '4500295752923',
            '6901237511587']

categories = []

for country_code in country_codes:
    category = []

    for code in products:
        if country_code in code:
            category.append(code)

    categories.append(category)

print(categories, '\nResult: done')

# Task 16: List of countries
#
# Description:
# These names must be added to the 'normalized_names' list in accordance with the naming conventions,
# for example: Peru, Canada, New Zealand, USA
# 'abbr_list' is a reference list containing examples of abbreviations.

print('-' * 10, 'Task 16:', sep='\n')

raw_names = ['peru', 'cANADA', 'australia', 'austria',
             'slovenia', 'slovakia', 'sweden', 'switzerland',
             'new zealand', 'uae', 'usa']

normalized_names = []
abbr_list = ['USA', 'UAE', 'GBR']

for name in raw_names:
    if name.upper() in abbr_list:
        normalized_names.append(name.upper())
    else:
        normalized_names.append(name.title())

print(normalized_names, '\nResult: done')

# Task 17: IP
#
# Description:
# The 'raw_data' list contains a collection of IP addresses and ports.
# The IP addresses and ports are fictitious and have been chosen at random
# (it is not recommended to check them in a browser).
# Only plain IP strings, without ports, should be added to the 'ips_list'. The list must be one-dimensional,
# with no nested lists, but simply consist of individual strings of values.

print('-' * 10, 'Task 17:', sep='\n')

raw_data = [
    [' 192.168.0.1:8080', ' 10.0.0.5 :22', '172.16.0.3 : 443  '],
    ['  8.8.8.8:53', ' 1.1.1.1 :  80', '  192.168.1.10:  3306'],
    [' 127.0.0.1 :5000', '  10.10.10.10:  8081 ', ' 0.0.0.0:   1234 ']
]

ips_list = []

for ip_list in raw_data:
    for ip in ip_list:
        ips_list.append(ip.split(':')[0].strip())

print(ips_list, '\nResult: done')

# Task 18: Longest Word
#
# Description:
# text = 'Python is a powerful programming language'
#
# Find the longest word in the sentence.
#
# Print:
# Longest word: programming
# Length: 11
#
# If there are several words with the same maximum length, print the first one.
#
# Restrictions:
# - Do not use max();
# - do not sort the list;
# - do not use lambda.
#
# Bonus:
# Ignore punctuation marks:
# . , ! ? : ;
#
# Example:
# 'Python is awesome!!!'
# should treat 'awesome!!!' as 'awesome'.

print('-' * 10, 'Task 18:', sep='\n')

text = 'Python is a powerful programming language'
text_list = text.split()

longest_word = text_list[0]

for word in text_list:
    word = word.strip('. , ! ? : ;')

    if len(word) > len(longest_word):
        longest_word = word

print(f'Longest word: {longest_word}\n'
      f'Length: {len(longest_word)}')

# Task 19: Lists
#
# Description:
# numbers = [4, 7, 2, 9, 1, 6, 8]
#
# Create a new list where every number is replaced with:
# 'even'  - if the number is even
# 'odd'   - if the number is odd
#
# Result:
# ['even', 'odd', 'even', 'odd', 'odd', 'even', 'even']
#
# Restrictions:
# - Do not modify the original list;
# - do not use list comprehensions.
#
# Bonus:
# Instead of strings, replace numbers with True (even)
# and False (odd).

print('-' * 10, 'Task 19:', sep='\n')

numbers = [4, 7, 2, 9, 1, 6, 8]
numbers_text = []
numbers_bool = []

for number in numbers:
    if number % 2 == 0:
        numbers_text.append('even')
        numbers_bool.append(True)
    else:
        numbers_text.append('odd')
        numbers_bool.append(False)

print('Result:', numbers_text, numbers_bool, sep='\n')

# Task 20: Lists
#
# Description:
# numbers = [4, 7, 2, 9, 4, 7, 1, 9, 8, 2, 5]
#
# Write a function find_duplicates() that returns a set of numbers that appear more than once in the list.
#
# Conditions:
# - do not use set(numbers) to find duplicates;
# - the result must be a set;
# - if there are no duplicates, return an empty set.
#
# For the given list, the result should be:
# {2, 4, 7, 9}

print('-' * 10, 'Task 20:', sep='\n')

numbers = [4, 7, 2, 9, 4, 7, 1, 9, 8, 2, 5]


def find_duplicates(nums):
    result = set()
    all_numbers = []

    for num in nums:
        if num in all_numbers:
            result.add(num)

        all_numbers.append(num)

    return result


print('Result:', find_duplicates(numbers))

# Task 21: First duplicate
#
# Description:
# numbers = [4, 7, 2, 4, 9, 7, 2, 8, 4, 9, 1]
#
# Write a function find_first_duplicate() that returns the first number
# that appears for the second time in the list.
#
# For the given list, the result should be:
# 4
#
# Conditions:
# - do not use count();
# - do not use set() to find duplicates;
# - if there are no duplicates, return None.

print('-' * 10, 'Task 21:', sep='\n')

list_numbers = [4, 7, 2, 4, 9, 7, 2, 8, 4, 9, 1]


def find_first_duplicate(numbers):
    find_duplicate = []

    for number in numbers:
        if number in find_duplicate:
            return number

        find_duplicate.append(number)

    return None


print('First duplicate:', find_first_duplicate(list_numbers))

# Task 22: Balanced Numbers
#
# Description:
# Given a list of numbers:
# numbers = [4, 7, 2, 9, 4, 7, 2, 9, 5, 4]
#
# Write a function find_balanced_numbers() that returns a set of numbers
# that appear an even number of times in the list.
#
# For the given list:
# - 4 appears 3 times → does not qualify;
# - 7 appears 2 times → qualifies;
# - 2 appears 2 times → qualifies;
# - 9 appears 2 times → qualifies;
# - 5 appears once → does not qualify.
#
# Result:
# {2, 7, 9}
#
# Conditions:
# - do not use Counter;
# - do not use count();
# - the result must be a set.
#
# Bonus: make the function work with any list of numbers.

print('-' * 10, 'Task 22:', sep='\n')

some_numbers = [4, 7, 2, 9, 4, 7, 2, 9, 5, 4]


def find_balanced_numbers(numbers):
    count_numbers = {}
    result = set()

    for number in numbers:
        count_numbers[number] = count_numbers.get(number, 0) + 1

    for number, count in count_numbers.items():
        if count % 2 == 0:
            result.add(number)

    return result


print('Result:', find_balanced_numbers(some_numbers))
