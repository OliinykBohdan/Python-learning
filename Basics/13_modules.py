# Task 1

import sys
import os
import platform
from math import ceil, sqrt as s
import time
import datetime as dt
import own_module

print('Sys:', sys.path)
print('Os:', os.name)
print('Platform:', platform.system())
print('Math:', ceil(s(121)))

time.sleep(1)

print('Datetime:', dt.datetime.now())

# Task 2

print(own_module.name)

own_module.say_hi()

res = own_module.add_3_numbers(1, 1, 1)

print(res)
