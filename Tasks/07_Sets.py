# Task 1: Create Unique List
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Get only unique values using set
# Convert it back to a list
# Print the result

print('-' * 10, 'Task 1:', sep='\n')

numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers)
numbers = list(numbers_set)

print('Result:', numbers)

# or
# unique_numbers = list(set(numbers))
#
# print(unique_numbers)

# Task 2: Add Elements
#
# You have a set:
#
# nums = {1, 2, 3}
#
# Add numbers 4 and 5
# Print the result

print('-' * 10, 'Task 2:', sep='\n')

nums = {1, 2, 3}

nums.add(4)
nums.add(5)

print('Result:', nums)

# Task 3: Remove Elements
#
# You have a set:
#
# nums = {1, 2, 3, 4, 5}
#
# Remove number 3
# Print the result

print('-' * 10, 'Task 3:', sep='\n')

nums = {1, 2, 3, 4, 5}
nums.remove(3)

print('Result:', nums)

# Task 4: Common Elements (Intersection)
# Task 4: Common Elements (Intersection)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find the common elements
#
# Find the common elements

print('-' * 10, 'Task 4:', sep='\n')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.intersection(set2)

print('Result:', set3)

# Task 5: Difference
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find elements that are in set1 but not in set2

print('-' * 10, 'Task 5:', sep='\n')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.difference(set2)

print('Result:', set3)

# Task 6: Loop Through Set
#
# You have a set:
#
# nums = {10, 20, 30}
#
# Print all elements using a for loop

print('-' * 10, 'Task 6:', sep='\n')

nums = {10, 20, 30}

for num in nums:
    print(num)

print('Result: done')

# Task 7: Remove Duplicates WITHOUT set()
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Create a new list without duplicates
# do NOT use set()

print('-' * 10, 'Task 7:', sep='\n')

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print('Result:', unique_numbers)

# Task 8: Common Elements
# Given two lists:
# [1, 2, 3, 4]
# [3, 4, 5, 6]
#
# Task:
# find common elements

print('-' * 10, 'Task 8:', sep='\n')

numbers_1 = [1, 2, 3, 4]
numbers_2 = [3, 4, 5, 6]

common_elements = set(numbers_1) & set(numbers_2)
# or
# common_elements = set(numbers_1).intersection(set(numbers_2))

print('Result:', common_elements)

# Task 9: Unique Values
# Given a list:
# [1, 2, 2, 3, 3, 3, 4]
#
# Task:
# get only unique values

print('-' * 10, 'Task 9:', sep='\n')

numbers = [1, 2, 2, 3, 3, 3, 4]

unique_values = set(numbers)
# or
# unique_values = []
# for num in numbers:
#     if num not in unique_values:
#         unique_values.append(num)

print('Result:', unique_values)

# Task 10: Product Barcodes by Country
#
# Description:
# Create a dictionary where the keys are country codes extracted from product barcodes,
# and the values are sets containing the product barcodes manufactured in those countries.
# Only countries that have at least one product should be included in the resulting dictionary.
# The function should process the product list and return the completed dictionary.

print('-' * 10, 'Task 10:', sep='\n')

country_codes = ['754', '690','450', '479']

products = ['4506436054267', '7547682958186', '6900626469201',
            '7543817559796', '7544194259711', '6900590565047',
            '6901237511586', '4502714135954', '4500295752923',
            ]


def dict_frame(codes_country, product):
    result = {}

    for code in codes_country:
        for prod in product:
            if prod[:3] == code:
                result[code] = set()

    return result


def run(products_code):
    result = dict_frame(country_codes, products_code)

    for code in products_code:
        result[code[:3]].add(code)

    return result


print('Result:', run(products), sep='\n')

# Task 11: Movies
#
# Description:
# List the movies that all users have watched.
# List the movies that no one has watched from the given list of all movies.
# For a specific user (Ann), recommend movies that other users have watched but she hasn't.

print('-' * 10, 'Task 11:', sep='\n')

all_movies = ['Inception', 'The Matrix', 'Interstellar', 'Tenet', 'Avatar', 'Titanic', 'Gravity']

watched_movies = {
    'Ann': {'Inception', 'Interstellar', 'Tenet'},
    'Bob': {'Inception', 'Avatar', 'Titanic'},
    'Kate': {'Interstellar', 'Gravity', 'Avatar', 'Inception'}
}


def recommendation(watched: dict[str, set[str]], movies: list[str],
                   user: str) -> dict[str, set[str]]:
    data = {'all_watched': set(), 'no_one_watched': set(), 'for_user': set()}

    movie_everyone_watched = watched[user].copy()
    all_watched_movies = set()
    watched_movies_without_user = set()

    for person, watch_movie in watched.items():
        movie_everyone_watched = movie_everyone_watched.intersection(watch_movie)
        all_watched_movies = all_watched_movies.union(watch_movie)

        if person == user:
            continue

        watched_movies_without_user = watched_movies_without_user.union(watch_movie)

    data['all_watched'] = movie_everyone_watched
    data['no_one_watched'] = set(movies).difference(all_watched_movies)
    data['for_user'] = watched_movies_without_user.difference(watched[user])

    return data


result = recommendation(watched_movies, all_movies, 'Ann')
print('Result:', result, sep='\n')
