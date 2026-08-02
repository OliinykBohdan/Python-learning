# Task 1

print('-' * 10, 'Task 1:', sep='\n')

# Methods covered: update(), get()

user = {'name': 'Alex', 'age': 27, 'country': 'USA'}

print(user)

# Add a new key-value pair
user['city'] = 'New York'

print('After adding city:', user)

# Remove a key from the dictionary
del user['age']

print('After removing age:', user)

user_info = {'hobby': 'programming', 'gender': 'male'}

# Merge another dictionary into user
user.update(user_info)
print('After merging dictionaries:', user)

# Safely access a non-existent key with default value
hobby = user.get('hobby1', 0)
print('Hobby value:', hobby)