from pprint import pprint

import requests

BASE = 'https://apilearn.tukas.dev/api/'

response = requests.get(BASE + 'categories/')

print(response.status_code)
pprint(response.json())
