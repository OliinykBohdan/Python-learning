# Task 1: Access Values
#
# Here is a dictionary:
#
# user = {
#     'name': 'Alex',
#     'age': 25,
#     'city': 'Kyiv'
# }
#
# Print:
#
# name
# city
from operator import add

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
# Here is a dictionary:
#
# user = {
#     'name': 'Alex',
#     'age': 25
# }
#
# Add a key:
#
# 'city': 'Kyiv'
#
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
# Here is a dictionary:
#
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
# Here is a dictionary:
#
# user = {
#     'name': 'Alex',
#     'age': 25,
#     'city': 'Kyiv'
# }
#
# Print all keys and values in the format:
#
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
# Here is a dictionary:
#
# user = {
#     'name': 'Alex',
#     'age': 25
# }
#
# Check:
#
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
# Here is a string:
#
# text = 'hello'
#
# Count how many times each character appears
# Use a dict
#
# Expected result:
#
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
# Here is a dictionary:
#
# scores = {
#     'Alex': 50,
#     'John': 75,
#     'Mike': 60
# }
#
# Find:
#
# who has the highest score
#
# Print:
#
# John: 75
#
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
# Description:
#
# You have a cart:
#
# cart = {}
#
# The user enters:
#
# a product
# a quantity
#
# The program should:
#
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
# Description:
#
# You have:
#
# cart = {
#     'apple': 5,
#     'banana': 3
# }
#
# The user enters:
#
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
# Given:
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
# Given:
#
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

# Continuation of Task 14. Countries are now stored not in alphabetical order, but in the order in which they were added.
#
# - There is one country to which delivery has not yet been implemented, but is planned (Peru).
#
# Task:
# The view_delivery function must return a string to be displayed somewhere in the interface, listing all the countries to which delivery is available, separated by \n.
#
# # - The countries must be listed in the string in ALPHABETICAL order.
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
# Given:
#
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
# Given:
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
# Given:
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
