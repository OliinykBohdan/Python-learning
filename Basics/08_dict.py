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

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

temps_celsius = [
    ['06:00', -1.5],
    ['07:00', 0.2],
    ['08:00', 2.8],
    ['09:00', 5.6],
    ['10:00', 8.4],
    ['11:00', 11.2],
    ['12:00', 14.7],
    ['13:00', 17.0],
    ['14:00', 18.3],
    ['15:00', 19.1],
    ['16:00', 19.4],
    ['17:00', 18.8],
    ['18:00', 17.0],
    ['19:00', 14.5],
    ['20:00', 11.2],
    ['21:00', 7.8],
    ['22:00', 4.0]
]

temps_d = dict(temps_celsius)

temps_d['14:00'] = 14.7
temps_d['23:00'] = 2.7
del temps_d['10:00']

print(temps_d)
