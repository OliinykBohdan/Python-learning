# Task 1: Access Values
#
# Description:
# user = {
#     'name': 'Alex',
#     'age': 25,
#     'city': 'Kyiv'
# }
#
# Print:
# name
# city

print('-' * 10, 'Task 1:', sep='\n')

user = {
    'name': 'Alex',
    'age': 25,
    'city': 'Kyiv',
}

print('name:', user['name'] )
print('city:', user['city'])

# Task 2: Add New Key
#
# Description:
# user = {
#     'name': 'Alex',
#     'age': 25
# }
#
# Add a key:
# 'city': 'Kyiv'
# Print the dictionary

print('-' * 10, 'Task 2:', sep='\n')

user = {
    'name': 'Alex',
    'age': 25,
}

user['city'] = 'Kyiv'

print(user)

# Task 3: Update Value
#
# Description:
# user = {
#     'name': 'Alex',
#     'age': 25
# }
#
# Change the age to 26

print('-' * 10, 'Task 3:', sep='\n')

user = {
    'name': 'Alex',
    'age': 25,
}

user['age'] = 26

print(user)

# Task 4: Loop Through Dict
#
# Description:
#
# user = {
#     'name': 'Alex',
#     'age': 25,
#     'city': 'Kyiv'
# }
#
# Print all keys and values in the format:
# name: Alex
# age: 25
# city: Kyiv

print('-' * 10, 'Task 4:', sep='\n')

user = {
    'name': 'Alex',
    'age': 25,
    'city': 'Kyiv',
}

for key, value in user.items():
    print(f'{key}: {value}')

# Task 5: Check Key
#
# Description:
# user = {
#     'name': 'Alex',
#     'age': 25
# }
#
# Check:
# if 'city' exists → print the value
# if not → 'Key not found'

print('-' * 10, 'Task 5:', sep='\n')

user = {
    'name': 'Alex',
    'age': 25,
}

city = user.get('city', 'Key not found')

print(city)

# Task 6: Count Characters
#
# Description:
# text = 'hello'
#
# Count how many times each character appears
# Use a dict
#
# Expected result:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print('-' * 10, 'Task 6:', sep='\n')

text = 'hello'
text_dict = {}

for char in text:
    if char in text_dict:
        text_dict[char] += 1
    else:
        text_dict[char] = 1

print(text_dict)

# Task 7 (challenge): Find Max Value
#
# Description:
# scores = {
#     'Alex': 50,
#     'John': 75,
#     'Mike': 60
# }
#
# Find:
# who has the highest score
#
# Print:
# John: 75
# without using max()

print('-' * 10, 'Task 7:', sep='\n')

scores = {
    'Alex': 50,
    'John': 75,
    'Mike': 60
}

max_name = None
max_score = None

for key, value in scores.items():
    if max_score is None or value > max_score:
        max_name = key
        max_score = value

print(f'{max_name}: {max_score}')

# Task 8: Add with Accumulation
#
# Description:
# cart = {}
#
# The user enters:
# a product
# a quantity
#
# The program should:
# if the product is new → add it
# if the product already exists → add the quantity to the existing one

print('-' * 10, 'Task 8:', sep='\n')

cart = {}
while True:
    product = input('Enter product name or exit: ')
    if product == 'exit':
        break

    try:
        quantity = int(input('Enter quantity: '))

    except ValueError:
        print('Please enter a numeric value.')
        continue

    cart[product] = cart.get(product, 0) + quantity
    print(cart)

# Task 9: Remove Partially
#
# Description:
# cart = {
#     'apple': 5,
#     'banana': 3
# }
#
# The user enters:
# a product
# a quantity to remove

print('-' * 10, 'Task 9:', sep='\n')

cart = {
    'apple': 5,
    'banana': 3
}

while True:
    product = input('Enter product name or exit: ')
    if product == 'exit':
        break
    elif product not in cart:
        print('Product not found')
        continue

    try:
        quantity = int(input('Enter removal quantity: '))

    except ValueError:
        print('Please enter a numeric value.')
        continue

    if quantity <= 0:
        print('Please enter a positive number.')
        continue
    elif quantity >= cart[product]:
            del cart[product]
    elif quantity < cart[product]:
            cart[product] -= quantity

    print(cart)

# Task 10: Invert Dictionary
#
# Description:
# {'a': 1, 'b': 2, 'c': 3}
#
# Task:
# swap keys and values
#
# Result:
# {1: 'a', 2: 'b', 3: 'c'}

print('-' * 10, 'Task 10:', sep='\n')

dictionaries_1 = {'a': 1, 'b': 2, 'c': 3}

dictionaries_2 = {
value: key
    for key, value in dictionaries_1.items()
}

print(dictionaries_2)

# Task 11: Count Frequency
#
# Description:
# Given a list:
# ['apple', 'banana', 'apple', 'orange', 'banana']
#
# Task:
# count how many times each element appears
#
# Result:
# {'apple': 2, 'banana': 2, 'orange': 1}

print('-' * 10, 'Task 11:', sep='\n')

fruits = ['apple', 'banana', 'apple', 'orange', 'banana']
fruit_count = {}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

print(fruit_count)

# Task 12: Student Scores
# 
# Description:
# Create a dictionary where:
# - the key is the student's name;
# - the value is the student's score.
#
# Then:
# - print all students and their scores;
# - find and print the student with the highest score.
#
# Example:
# {
#     'John': 85,
#     'Emma': 92,
#     'Mike': 78,
#     'Anna': 95
# }
#
# Expected output:
# John: 85
# Emma: 92
# Mike: 78
# Anna: 95
#
# Best student: Anna (95)

print('-' * 10, 'Task 12:', sep='\n')

students_results = {
                    'John': 85,
                    'Emma': 92,
                    'Mike': 78,
                    'Anna': 95
}

for student, score in students_results.items():
    print(f'{student}: {score}')

best_student = max(students_results, key=students_results.get)

print(f'\nBest student: {best_student} ({students_results[best_student]})')

# Task 13: Inventory
#
# Description:
# inventory = {
#     'Sword': 1,
#     'Potion': 5,
#     'Shield': 1,
#     'Arrow': 20
# }
#
# Print every item in the following format:
# Sword: 1
# Potion: 5
# Shield: 1
# Arrow: 20
#
# Then calculate and print the total number of items.
#
# Result:
# Total items: 27

print('-' * 10, 'Task 13:', sep='\n')

inventory = {
    'Sword': 1,
    'Potion': 5,
    'Shield': 1,
    'Arrow': 20
}

total_items = 0

for item, value in inventory.items():
    print(f'{item}: {value}')
    total_items += value

print(f'\nTotal items: {total_items}')

# Task 14: Delivery countries
# 
# Description:
# There is a dictionary containing the countries available for delivery and the approximate delivery time,
# in days, to the relevant country.
#
# Task:
# The view_delivery function must return a string to be displayed somewhere in the interface,
# listing all these countries separated by \n.
#
# An example of the string, when viewed using repr:
# 'Argentina\nBrazil\nCanada\nMexico\nUSA'

print('-' * 10, 'Task 14:', sep='\n')

delivery_countries = {'Argentina': 4, 'Brazil': 3,
                      'Canada': 2, 'Mexico': 2, 'USA': 1}

def view_delivery():
    text = ''

    for country in delivery_countries:
        text += f'{country}\n'

    return text[:-1]

print('Result:', repr(view_delivery()))

# Task 15: Delivery countries 2
#
# Description:
# Continuation of Task 14. Countries are now stored not in alphabetical order,
# but in the order in which they were added. There is one country to which delivery
# has not yet been implemented, but is planned (Peru).
#
# Task:
# The view_delivery function must return a string to be displayed somewhere in the interface,
# listing all the countries to which delivery is available, separated by \n.
#
# - The countries must be listed in the string in ALPHABETICAL order.
# - Countries to which delivery is not yet available must not be included in the list.
#
# An example of a string, as seen when printed using repr:
# 'Argentina\nBrazil\nCanada\nMexico\nUSA'

print('-' * 10, 'Task 15:', sep='\n')

delivery_countries_2 = {'USA': 1, 'Canada': 2, 'Mexico': 2,
                      'Brazil': 3, 'Argentina': 4, 'Peru': None}


def view_delivery():
    text = ''

    for country in sorted(delivery_countries_2):
        if delivery_countries_2[country]:
            text += f'{country}\n'

    return text[:-1]


print('Result:', repr(view_delivery()))

# Task 16: Dictionaries
#
# Description:
# purchases = [
#     'apple',
#     'banana',
#     'apple',
#     'orange',
#     'banana',
#     'apple',
#     'kiwi'
# ]
#
# Create a dictionary where:
# - the key is the product name;
# - the value is how many times the product appears.
#
# Result:
# {
#     'apple': 3,
#     'banana': 2,
#     'orange': 1,
#     'kiwi': 1
# }
#
# Print the dictionary.
#
# Bonus:
# Find and print the product that was purchased the most times.
#
# Restrictions:
# - Do not use collections.Counter.
# - Do not use dict.setdefault().

print('-' * 10, 'Task 16:', sep='\n')

purchases = [
    'apple',
    'banana',
    'apple',
    'orange',
    'banana',
    'apple',
    'kiwi'
]

purchases_dict = {}

for product in purchases:
    if product in purchases_dict:
        purchases_dict[product] += 1
    else:
        purchases_dict[product] = 1

common_product = max(purchases_dict, key=purchases_dict.get)

print(f'Result: {purchases_dict}\n'
      f'Most purchased product \'{common_product}\' (quantity {purchases_dict[common_product]})')

# Task 17: Dictionaries + Strings
#
# Description:
# text = 'Python python Java PYTHON java C++ python'
# Count how many times each word appears.
#
# Requirements:
# - Ignore letter case.
# - Store the result in a dictionary.
#
# Result:
# {
#     'python': 4,
#     'java': 2,
#     'c++': 1
# }
#
# Bonus:
# Print the most frequent word and its count.
#
# Restrictions:
# - Do not use Counter.
# - Do not use count().
# - Do not sort the dictionary.

print('-' * 10, 'Task 17:', sep='\n')

text = 'Python python Java PYTHON java C++ python'
text_list = text.split()
text_dict = {}

for word in text_list:
    word = word.lower()

    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1

frequent_word = max(text_dict, key=text_dict.get)

print(f'Result:, {text_dict}\n'
      f'Most frequent word: {frequent_word} ({text_dict[frequent_word]})')

# Task 18: Dictionaries
#
# Description:
# inventory = {
#     'Sword': 1,
#     'Potion': 5,
#     'Shield': 1,
#     'Arrow': 20,
#     'Apple': 7,
#     'Helmet': 2
# }
#
# Create TWO new dictionaries:
# low_stock  - items with quantity less than 5
# high_stock - items with quantity greater than or equal to 5
#
# Result:
# low_stock:
# {
#     'Sword': 1,
#     'Shield': 1,
#     'Helmet': 2
# }
#
# high_stock:
# {
#     'Potion': 5,
#     'Arrow': 20,
#     'Apple': 7
# }
#
# Restrictions:
# - Do not modify the original dictionary.
# - Do not use dictionary comprehensions.
#
# Bonus:
# Print the total quantity of items in each new dictionary.

print('-' * 10, 'Task 18:', sep='\n')

inventory = {
    'Sword': 1,
    'Potion': 5,
    'Shield': 1,
    'Arrow': 20,
    'Apple': 7,
    'Helmet': 2
}

low_stock = {}
high_stock = {}

total_quantity_low = 0
total_quantity_high = 0

for key, value in inventory.items():
    if value < 5:
        low_stock[key] = value
        total_quantity_low += value
    else:
        high_stock[key] = value
        total_quantity_high += value

print(f'Low stock: {low_stock} | Total quantity: {total_quantity_low}\n'
      f'High stock: {high_stock} | Total quantity: {total_quantity_high}')

# Task 19: Celsius - Fahrenheit
#
# Write a function called convert_temp_data that returns a new dictionary.
#
# Description:
# - The convert_temp_data function takes a dictionary or an iterable [(key, value), ...)
# object as an argument. An example of such an argument is provided in the example.py file
# (you do not need to modify it; simply use it as an argument).
# - The convert_temp_data function must return a new dictionary in which all temperature
# values in degrees Celsius have been converted to Fahrenheit. Do not modify the
# convert_temperature function; simply use it.
# - In the new dictionary, any invalid temperature values must be None only.
# The idea is that the key with the measurement time should remain, but with a value of None.
# - Round correctly converted values to 2 decimal places.

print('-' * 10, 'Task 19:', sep='\n')

temps_celsius = {
    '06:00': -1.5,
    '07:00': -1000000.0,  # Incorrect data.
    '08:00': 2.8,
    '09:00': 5.6,
    '10:00': 8.4,
    '11:00': 11.2,
    '12:00': 14.7,
    '13:00': 17.0,
    '14:00': 18.3,
    '15:00': 19.1,
    '16:00': 19.4,
    '17:00': 18.8,
    '18:00': 17.0,
    '19:00': 14.5,
    '20:00': 11.2,
    '21:00': None,  # No measurement was taken.
    '22:00': 4.0
}


def convert_temperature(temp_celsius: float | int, /) -> float | None:
    if temp_celsius < -273.15:
        return False
    return temp_celsius * 9 / 5 + 32


def convert_temp_data(data) -> dict[str, float | None]:
    temps_fahrenheit = {}

    if isinstance(data, dict):
        data = data.items()

    for time, temp in data:
        if temp == None or temp < -273.15 or temp > 1.4 * 10**32:
            temps_fahrenheit[time] = None
        else:
            temp_fahrenheit = round(convert_temperature(temp), 2)
            temps_fahrenheit[time] = temp_fahrenheit

    return temps_fahrenheit


print('Temperature readings in degrees Fahrenheit:', convert_temp_data(temps_celsius), sep='\n')

# Task 20: Number of words
# 
# Description:
# Create a class called WordCounter that takes a string of text.
# Add a method called count that returns a dictionary where:
# - the key is a word
# - the value is the number of times it appears in the text

print('-' * 10, 'Task 20:', sep='\n')


class WordCounter:
    def __init__(self, words):
        self.words = words

    def count(self):
        words_dict = {}
        words_list = self.words.lower().split()

        for word in words_list:
            word = word.strip('! ? , . : ;')

            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1

        return words_dict


counter = WordCounter('?Hello!!! HI! hello!! HELlo., hi')

print('Result:', counter.count())

# Task 21: Dictionary of vowels and consonants
#
# Description:
# Write a function that takes a string and returns a dictionary containing
# the counts of vowels and consonants.

print('-' * 10, 'Task 21:', sep='\n')


def vowels_and_consonants(text):
    vowels_chars = 'aeiouy'
    consonants_chars = 'bcdfghjklmnpqrstvwxz'
    dict_chars = {}

    for char in text:
        char = char.lower()

        if char in vowels_chars:
            dict_chars['vowels'] = dict_chars.get('vowels', 0) + 1
        elif char in consonants_chars:
            dict_chars['consonants'] = dict_chars.get('consonants', 0) + 1

    return dict_chars


print('Result:', vowels_and_consonants('Text'))

# Task 22: ShoppingCart.
#
# Description:
# Create a ShoppingCart class. The add(product, price) method adds an item.
# The total() method returns the sum of all prices.

print('-' * 10, 'Task 22:', sep='\n')


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add(self, product, price):
        self.cart[product] = self.cart.get(product, 0) + price

    def total(self):
        total_price = 0

        for price in self.cart.values():
            total_price += price

        return total_price


user = ShoppingCart()

user.add('apple', 100)
user.add('apple', 100)
user.add('apple', 100)
user.add('orange', 200)
user.add('orange', 200)

print('Cart:', user.cart, sep='\n')
print('\nTotal price:', user.total())

# Task 23: Top player
#
# Description:
# Create a ScoreTable class. The add(name, points) method adds points to a player.
# The top_player() method returns the name of the player with the highest score.

print('-' * 10, 'Task 23:', sep='\n')


class ScoreTable:
    def __init__(self):
        self.scores = {}

    def add(self, name, points):
        self.scores[name] = self.scores.get(name, 0) + points

    def top_player(self):
        if not self.scores:
            return None

        top_player = max(self.scores, key=self.scores.get)

        return top_player


game = ScoreTable()

game.add('Alex', 9)
game.add('John', 7)

print('Top player:', game.top_player())

# Task 24: List + logic
#
# Description:
# Given a list of numbers:
# numbers = [10, 3, 5, 10, 8, 3, 7, 5, 12, 8, 3]
#
# Find the first number that appears exactly once in the list.
#
# For the given list, the result should be:
# 7
#
# Restrictions:
# - do not use set();
# - do not use collections.Counter;
# - do not use list.count();
# - do not modify the original list.
#
# Bonus: make the algorithm return None if there is no number that appears exactly once.

print('-' * 10, 'Task 24:', sep='\n')

numbers = [10, 3, 5, 10, 8, 3, 7, 5, 12, 8, 3]
counts = {}
found = False

for number in numbers:
    counts[number] = counts.get(number, 0) + 1

for number in numbers:
    if counts[number] == 1:
        print('First unique number in list:', number)
        found = True
        break

if not found:
    print('Result:', None)

# Task 25: Student grades
#
# Description:
# There are two dictionaries containing data on students and their grades for two semesters.
#
# 1) Find students who appear in both semesters.
# 2) Find students who appear only in the second semester.
# 3) Find students whose grades are the same across both semesters.

print('-' * 10, 'Task 25:', sep='\n')

sem1 = {'Ann': 85, 'Bob': 90, 'Kate': 75}
sem2 = {'Bob': 88, 'Kate': 75, 'Mike': 92}

key_sem1 = sem1.keys()
key_sem2 = sem2.keys()

stud_both_sem = key_sem1 & key_sem2
stud_app_in_second_sem = key_sem2 - key_sem1

items_sem1 = sem1.items()
items_sem2 = sem2.items()

stud_grade_across_sem = items_sem1 & items_sem2

print('Students in both semesters:', stud_both_sem,
      'Students appeared in the second semester:', stud_app_in_second_sem,
      'The grade is the same across semesters:', stud_grade_across_sem, sep='\n')

# Task 26: Average price
#
# Description:
# Write a function that takes a dictionary of product prices and returns the average price.
# If the dictionary is empty, return 0.

print('-' * 10, 'Task 26:', sep='\n')


def average_price(prices):
    if not prices:
        return 0

    total = 0

    for price in prices.values():
        total += price

    return total / len(prices)


print('Average price:', average_price({}))

# Task 27: First letter stats
#
# Description:
# Write a function that takes a list of words and returns a dictionary where:
# - the key is the first letter of the word;
# - the value is the number of words starting with that letter.

print('-' * 10, 'Task 27:', sep='\n')


def first_letter_stats(words):
    words_dict = {}

    for word in words:
        word = word.lower()

        words_dict[word[0]] = words_dict.get(word[0], 0) + 1

    return words_dict


print('First letter stats:', first_letter_stats(['Hello', 'Python']), sep='\n')

# Task 28: Number of characters
#
# Description:
# Write a function that takes a string and returns a dictionary:
# - 'digits' — the number of digits;
# - 'letters' — the number of letters;
# - 'others' — the number of other characters.

print('-' * 10, 'Task 28:', sep='\n')


def char_stats(text):
    result = {'digits': 0, 'letters': 0, 'others': 0}

    for char in text:
        if char.isdigit():
            result['digits'] += 1
        elif char.isalpha():
            result['letters'] += 1
        else:
            result['others'] += 1

    return result


print('Result:', char_stats('123 sd.'))

# Task 29: Word length
#
# Description:
# Write a function that takes a list of words and returns a dictionary where:
# - the key is the word length;
# - the value is a set of words of that length.

print('-' * 10, 'Task 29:', sep='\n')


def group_by_length(words):
    result = {}

    for word in words:
        word_length = len(word)

        if word_length not in result:
            result[word_length] = set()

        result[word_length].add(word)

    return result


print('Result:', group_by_length(['1', '2', '33']))

# Task 30: Dictionaries
#
# Description:
# Given a dictionary containing products and their prices:
# products = {
#     'apple': 25,
#     'banana': 18,
#     'orange': 30,
#     'kiwi': 45,
#     'mango': 60
# }
#
# Create a function price_groups() that returns a dictionary with three groups:
# 'cheap' — products cheaper than 30;
# 'medium' — products from 30 to 50 inclusive;
# 'expensive' — products more expensive than 50.
#
# The values for these keys should be sets containing product names.
#
# Expected result:
# {
#     'cheap': {'apple', 'banana'},
#     'medium': {'orange', 'kiwi'},
#     'expensive': {'mango'}
# }

print('-' * 10, 'Task 30:', sep='\n')

products_dict = {
    'apple': 25,
    'banana': 18,
    'orange': 30,
    'kiwi': 45,
    'mango': 60
}


def price_groups(products):
    result = {'cheap': set(), 'medium': set(), 'expensive': set()}

    for product, price in products.items():
        if price < 30:
            result['cheap'].add(product)
        elif 30 <= price <= 50:
            result['medium'].add(product)
        else:
            result['expensive'].add(product)

    return result


print('Result:', price_groups(products_dict), sep='\n')

# Task 31: Dictionaries
#
# Description:
# Given a dictionary containing students and their grades:
# students = {
#     'Ann': [85, 90, 78],
#     'Bob': [92, 88, 95],
#     'Kate': [70, 75, 68],
#     'Mike': [90, 84, 87]
# }
#
# Write a function student_averages() that returns a new dictionary where:
# - the key is the student's name;
# - the value is their average grade.
#
# Additional condition: round the average grade to 2 decimal places.
#
# Bonus: include only students whose average grade is at least 80.
#
# Expected result:
# {
#     'Ann': 84.33,
#     'Bob': 91.67,
#     'Mike': 87.0
# }

print('-' * 10, 'Task 31:', sep='\n')

students_dict = {
    'Ann': [85, 90, 78],
    'Bob': [92, 88, 95],
    'Kate': [70, 75, 68],
    'Mike': [90, 84, 87]
}


def student_averages(students):
    stud_average_grade = {}

    for name, grades in students.items():
        average_grade = round(sum(grades) / len(grades), 2)

        if average_grade >= 80:
            stud_average_grade[name] = average_grade

    return stud_average_grade


print('Result:', student_averages(students_dict))

# Task 32: Transaction Summary
#
# Description:
# Given a list of transactions:
# transactions = [
#     ('deposit', 500),
#     ('withdraw', 120),
#     ('deposit', 300),
#     ('withdraw', 50),
#     ('deposit', 200),
#     ('withdraw', 100)
# ]
#
# Write a function transaction_summary() that returns a dictionary with three keys:
# - 'total_deposits' — the total amount of all deposits;
# - 'total_withdrawals' — the total amount of all withdrawals;
# - 'balance_change' — the final change in balance: deposits minus withdrawals.
#
# For the given data, the result should be:
# {
#     'total_deposits': 1000,
#     'total_withdrawals': 270,
#     'balance_change': 730
# }
#
# Bonus: add a 'transactions_count' key containing the total number of transactions.

print('-' * 10, 'Task 32:', sep='\n')

transactions = [
    ('deposit', 500),
    ('withdraw', 120),
    ('deposit', 300),
    ('withdraw', 50),
    ('deposit', 200),
    ('withdraw', 100)
]


def transaction_summary(operations):
    total_deposits = 0
    total_withdrawals = 0
    transactions_count = 0

    for transaction in operations:
        if transaction[0] == 'deposit':
            total_deposits += transaction[1]
        elif transaction[0] == 'withdraw':
            total_withdrawals += transaction[1]

        transactions_count += 1

    balance_change = total_deposits - total_withdrawals

    return {
        'total_deposits': total_deposits,
        'total_withdrawals': total_withdrawals,
        'balance_change': balance_change,
        'transactions_count': transactions_count
    }


print('Result:', transaction_summary(transactions), sep='\n')
