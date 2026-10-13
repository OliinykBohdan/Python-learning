from pprint import pprint

import requests
import json

# Task 1: Requests basics

print('-' * 10, 'Task 1:', sep='\n')

BASE = 'https://apilearn.tukas.dev/api/'

response = requests.get(BASE + 'categories/')

print(response.status_code)
pprint(response.json())

# Task 2: JSON

print('-' * 10, 'Task 2:', sep='\n')

data = {
    'name': 'Alex',
    'age': 33,
    'animal': True,
    'favorite_nums': {1, 2, 3},
    'dimension': (180.5, 103),
    'kids': None,
    'favorite_movies': {'fantasy': '5th element',
                        'drama': 'Game of Thrones'}
}


def to_list(obj):
    if isinstance(obj, set):
        return list(obj)


js = json.dumps(data, default=to_list)

print(js)
print(json.loads(js))
