# Task 1: Simple Function
#
# Description:
# Create a function that:
# takes a name as a parameter
#
# Print:
# 'Hello, <name>!'

print('-' * 10, 'Task 1:', sep='\n')


def name(x):
    print(f'Hello, {x}!')


name('Bohdan')

# Task 2: Return Sum
#
# Description:
# Create a function that:
# - takes two numbers;
# - returns their sum.
#
# Print the result outside the function.

print('-' * 10, 'Task 2:', sep='\n')


def sum_numbers(x, y):
    return x + y


print('Sum_numbers:', sum_numbers(7, 9))
print('Sum_numbers:', sum_numbers(10, 2))

# Task 3: Even or Odd (Function)
#
# Description:
# Create a function that:
# - takes a number;
# - returns 'even' or 'odd'.
#
# Use return, not print.

print('-' * 10, 'Task 3:', sep='\n')


def number(x):
    if x % 2 == 1:
        return 'odd'
    else:
        return 'even'


print(number(12))
print(number(11))

# Task 4: Max of Three
#
# Description:
# Create a function that:
# - takes three numbers;
# - returns the largest number.
#
# Do NOT use max().

print('-' * 10, 'Task 4:', sep='\n')


def largest_number (x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z


print('Largest number:', largest_number(50, 60, 100))
print('Largest number:', largest_number(10, 1700, 220))


# Task 5: Shopping Cart Total (Function)
#
# Description:
# You have:
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
# - takes cart and price;
# - returns total price.
#
# Call the function and print result.

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


print('Total price:', total_price(cart, price))

# Task 6: Password Check (Function + Loop)
#
# Description:
# Create a function that:
# - asks the user for a password;
# - has 3 attempts.
#
# Rules:
# - correct → return 'Access granted';
# - wrong → ask again;
# - after 3 attempts → return 'Access denied'.

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
#
# Description:
# Create a function that:
# - takes a list;
# - returns a dictionary where:;
# - key → element;
# - value → how many times it appears.

print('-' * 10, 'Task 7:', sep='\n')

numbers = [1, 2, 2, 3, 1]


def count_elements(number):
    result = {}
    for x in number:
        result[x] = result.get(x, 0) + 1
    return result


print('Result:', count_elements(numbers))

# Task 8: Filter Greater Than (Function + List)
#
# Description:
# Create a function that:
# - takes a list and a number n;
# - returns a new list with elements greater than n.

print('-' * 10, 'Task 8:', sep='\n')

numbers = [1, 5, 8, 2, 10]
n = 5


def greater_than_n (x, y):
    numbers_greater = []
    for i in x:
        if i > y:
            numbers_greater.append(i)
    return numbers_greater


print('Result:', greater_than_n (numbers, n))

# Task 9: Mini Calculator (Function + Logic)
#
# Description:
# Create a function that takes:
# - two numbers;
# - an operator ('+', '-', '*', '/');
# - returns the result.

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
print('Result: done')

# Task 10: Convert temperature
#
# Description:
# There is a list of values in degrees Celsius:
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

# Task 11: Filter Numbers
#
# Description:
# Write a function:
# filter_numbers(numbers, min_value=0, max_value=100,
#                descending=False, even_only=False)
#
# numbers is a list or tuple of numbers.
#
# The function must:
# - keep only numbers from min_value to max_value inclusive;
# - if even_only=True, keep only even numbers;
# - sort the result;
# - if descending=True, sort in descending order.
#
# The function must return a new list
# without modifying the original sequence.
#
# Example:
# numbers = (1, 4, 12, 98, 102, -5, 0, 77, 88)
#
# filter_numbers(numbers)
# -> [0, 1, 4, 12, 77, 88, 98]
#
# filter_numbers(numbers, even_only=True)
# -> [0, 4, 12, 88, 98]

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

# Task 12: List Transformation
#
# Description:
# Write a function:
# transform_list(numbers, group_size=3)
#
# The function receives a one-dimensional list.
#
# It must modify the original list in place
# by grouping its elements into nested lists.
#
# Each nested list must contain group_size elements.
#
# If there are not enough elements for the final group,
# add the remaining elements as a shorter nested list.
#
# The default group_size is 3.
#
# The function must not create and return
# a separate transformed list.
#
# Return True if the transformation was successful.
# If the input list is empty, return False.

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
# Description:
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
# Description:
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


print('Result:', get_stats((10, 20, 30)))

# Task 15: Average of Arguments 1
#
# Description:
# Write a function:
# average_value(*args, rounding=2)
#
# The function must:
# - accept any number of positional arguments;
# - calculate the arithmetic mean of all arguments;
# - round the result using the rounding parameter;
# - use 2 decimal places by default;
# - return the calculated result.
#
# If the function is called without positional arguments,
# return None.

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

# Task 16: Average of Arguments 2
#
# Description:
# Write a function that calculates the overall
# arithmetic mean of all temperature values.
#
# The temperature values are not stored
# in a single one-dimensional list.
#
# They are grouped in a nested data structure,
# so the function must process all contained values
# and calculate one overall average.

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
# Description:
# The function must return a new list containing the quantities of banknotes required
# to dispense the requested amount to the customer.
#
# Conditions:
# - the quantities of banknotes of a specific denomination must appear in the
# same order in the new list as in the banknotes_in_atm list;
# - if there are 0 banknotes of a particular denomination, it should still be added to the list;
# - the quantities of banknotes for each denomination are calculated according
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


print('Result:', get_banknote_counts(cash, banknotes_in_atm))

# Task 18: Analyze text
#
# Description:
# Write a function that takes a string and a mode: count or length.
# If the mode is count - return the number of letters a,
# if it is length - return the length of the string.

print('-' * 10, 'Task 18:', sep='\n')


def analyze_text(text, mode):
    if mode == 'count':
        counter = 0
        for char in text.lower():
            if char == 'a':
                counter += 1

        return counter

    elif mode == 'length':
        counter = 0
        for _ in text:
            counter += 1

        return counter


print('String length:', analyze_text('Alakazam', 'length'))
print('Number of letters a:', analyze_text('Alakazam', 'count'))

# Task 19: Number Range
#
# Description:
# Write a function is_in_range(number, min_value, max_value)
#
# The function should:
# - return True if the number is within the range (inclusive);
# - otherwise return False.
#
# Example:
# is_in_range(10, 1, 20) -> True
# is_in_range(25, 1, 20) -> False
#
# Bonus:
# Add an optional argument inclusive=True.
# If inclusive=False, the range should exclude the borders.

print('-' * 10, 'Task 19:', sep='\n')


def is_in_range(numb, min_value, max_value, inclusive=True):
    if inclusive:
        if min_value <= numb <= max_value:
            return True
        return False

    if min_value < numb < max_value:
        return True
    return False


number_in_range = is_in_range(30, 1, 30, inclusive=False)

print('Result:', number_in_range)

# Task 20: Word Counter
#
# Description:
# Write a function count_words(text)
# The function should return the number of words in a string.
#
# Requirements:
# - words are separated by spaces;
# - ignore leading and trailing spaces;
# - if the string is empty or contains only spaces, return 0.
#
# Example:
# count_words('Python is awesome') -> 3
# count_words('   Hello world   ') -> 2
# count_words('') -> 0

print('-' * 10, 'Task 20:', sep='\n')


def count_words_manual(text):
    count = 0
    text = ' '.join(text.split())

    if not text:
        return count

    for char in text:
        if char == ' ':
            count += 1

    return count + 1


# Alternative solution
def count_words_split(text):
    return len(text.split())


print('Number of words:', count_words_manual('Python is awesome'))
print('Number of words:', count_words_split('   Hello world   '))

# Task 21: Capitalize Sentence
#
# Description:
# Write a function capitalize_sentence(text)
#
# The function should:
# - capitalize the first letter of every word;
# - keep the remaining letters lowercase;
# - ignore extra spaces between words.
#
# Example:
# capitalize_sentence('pYtHon    IS   AwEsOmE')
#
# Result:
# 'Python Is Awesome'
#
# Do not use str.title().

print('-' * 10, 'Task 21:', sep='\n')


def capitalize_sentence(text):
    words = text.split()
    new_text = []

    for word in words:
        new_text.append(word.capitalize())

    return ' '.join(new_text)


print('Result:', capitalize_sentence('pYtHon    IS   AwEsOmE'))

# Task 22: Rotate List
#
# Description:
# Write a function rotate_right(numbers).
#
# The function should return a new list where
# all elements are shifted one position to the right.
# The last element becomes the first.
#
# Example:
# [1, 2, 3, 4, 5]
#
# Result:
# [5, 1, 2, 3, 4]
#
# If the list is empty, return an empty list.
# Do not use collections.deque or ready-made rotation methods.

print('-' * 10, 'Task 22:', sep='\n')


def rotate_right(numbers):
    if not numbers:
        return []

    rotate_list = []
    rotate_list.append(numbers[-1])

    index = 0

    while index < len(numbers) - 1:
        rotate_list.append(numbers[index])

        index += 1

    return rotate_list


print('Result:', rotate_right([1, 2, 3, 4, 5]))

# Task 23: Functions
#
# Description:
# Write a function repeat_text(text, count)
# The function should return the text repeated
# the specified number of times.
#
# If count is less than or equal to 0,
# return an empty string.
#
# Examples:
# repeat_text('Hi', 3)
# Result:
# 'HiHiHi'
#
# repeat_text('Python', 1)
# Result:
# 'Python'
#
# repeat_text('Test', 0)
# Result:
# ''
#
# Do not use string multiplication (*).

print('-' * 10, 'Task 23:', sep='\n')


def repeat_text(text, count):
    if count <= 0:
        return ''

    new_text = ''
    current = 0

    while current < count:
        new_text += text
        current += 1

    return new_text


print('Result:', repeat_text('Hi', 3))
print('Result:', repeat_text('Hi', 0))

# Task 24: Balance Changes
#
# Description:
# Given a starting balance and a list of balance changes, write a function
# balance_history(start_balance, changes) that stores the balance after every successful operation.
#
# Requirements:
# - positive numbers add money and negative numbers subtract money;
# - do not include the starting balance in the result;
# - if an operation would make the balance negative, skip it;
# - skipped operations should not add anything to the result;
# - do not modify the original changes list.
#
# Bonus: also return the number of skipped operations.

print('-' * 10, 'Task 24:', sep='\n')

changes = [100, -30, -20, 50, -150, 70, -10]


def balance_history(start_balance, changes):
    result = []
    skipped_count = 0

    for change in changes:
        if start_balance + change >= 0:
            start_balance += change
            result.append(start_balance)
        else:
            skipped_count += 1

    return result, skipped_count


print('Result:', balance_history(200, changes), sep='\n')

# Task 25: Price Changes
#
# Description:
# Given product names and their old and new prices:
# products = ['Steel', 'Nickel', 'Titanium', 'Copper']
# old_prices = [10, 25, 40, 15]
# new_prices = [12, 20, 40, 18]
#
# Write a function:
# compare_prices(products, old_prices, new_prices)
#
# Return a dictionary containing only products whose price changed.
# Each value must be: new_price - old_price.
#
# Expected result:
# {'Steel': 2, 'Nickel': -5, 'Copper': 3}
#
# Do not add products whose price stayed unchanged.
#
# Conditions:
# - all three lists have the same length;
# - prices are numbers;
# - do not modify the original lists;
# - use zip() to iterate through the lists together.
#
# Bonus:
# also return the number of price increases
# and the number of price decreases.
#
# Example:
# ({'Steel': 2, 'Nickel': -5, 'Copper': 3}, 2, 1)

print('-' * 10, 'Task 25:', sep='\n')

products = ['Steel', 'Nickel', 'Titanium', 'Copper']
old_prices = [10, 25, 40, 15]
new_prices = [12, 20, 40, 18]


def compare_prices(products, old_prices, new_prices):
    result = {}
    increased = 0
    decreased = 0

    for product, old_price, new_price in zip(products, old_prices, new_prices):
        if new_price != old_price:
            difference = new_price - old_price
            result[product] = difference

            if difference > 0:
                increased += 1
            else:
                decreased += 1

    return result, increased, decreased


print('Result:', compare_prices(products, old_prices, new_prices), sep='\n')

# Task 26: Command Navigator
#
# Description:
# Given a list of commands:
# commands = [
#     'UP 3',
#     'RIGHT 5',
#     'DOWN 2',
#     'LEFT 1',
#     'UP x',
#     'JUMP 4'
# ]
#
# Write a function:
# navigate(commands)
#
# The starting position is:
# x = 0, y = 0
#
# Valid commands:
# UP n, DOWN n, LEFT n, RIGHT n
#
# n must be a positive integer.
# Skip invalid commands and count them.
#
# Directions:
# UP -> increase y
# DOWN -> decrease y
# RIGHT -> increase x
# LEFT -> decrease x
#
# Return:
# ((x, y), invalid_commands)
#
# Bonus:
# return the greatest distance from (0, 0)
# reached after any valid command as the third value.
# Calculate distance as abs(x) + abs(y).

print('-' * 10, 'Task 26:', sep='\n')

commands = [
    'UP 3',
    'RIGHT 5',
    'DOWN 2',
    'LEFT 1',
    'UP x',
    'JUMP 4'
]


def navigate(commands):
    valid_commands = ('UP', 'DOWN', 'RIGHT', 'LEFT')
    invalid_commands_count = 0
    greatest_distance = 0
    x = 0
    y = 0

    for command in commands:
        parts = command.split()
        if len(parts) != 2:
            invalid_commands_count += 1
            continue

        try:
            current_command = parts[0]
            value = int(parts[1])

        except ValueError:
            invalid_commands_count += 1
            continue

        if current_command in valid_commands and value > 0:
            if current_command == 'UP':
                y += value
            elif current_command == 'DOWN':
                y -= value
            elif current_command == 'RIGHT':
                x += value
            elif current_command == 'LEFT':
                x -= value

            current_distance = abs(x) + abs(y)

            if current_distance > greatest_distance:
                greatest_distance = current_distance

        else:
            invalid_commands_count += 1

    return (x, y), invalid_commands_count, greatest_distance


print('Result:', navigate(commands))
