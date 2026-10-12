# Task 1: Import Module
#
# Description:
# Import the built-in module math
#
# Task:
# print:
# square root of 16
# value of π

print ('-' * 10, 'Task 1:', sep = '\n')

import math

print('Square root:', math.sqrt(16))
print('Value of π:', math.pi)

# Task 2: Import with Alias
#
# Description:
# Import module random as rnd
#
# Task:
# generate:
# random number from 1 to 10

print ('-' * 10, 'Task 2:', sep = '\n')

import random as rnd

print('Random number:', rnd.randint(1, 10))

# Task 3: Import Specific Function
#
# Description:
# Import only randint from random
#
# Task:
# generate 5 random numbers (1–100)

print ('-' * 10, 'Task 3:', sep = '\n')

from random import randint

count = 0

while count < 5:
    print(randint(1, 100))
    count += 1

print('Result: done')

# Task 4: Custom Module (Basic)
#
# Description:
# Create file my_math.py
#
# Add functions:
# add(a, b)
# sub(a, b)
#
# Task:
# - import this module;
# - use both functions.

print('-' * 10, 'Task 4:', sep = '\n')

import my_math_module

print('Addition:', my_math_module.add(7, 5))
print('Substraction:', my_math_module.sub(7, 5))

# Task 5: Custom Module with Variables
#
# Description:
# In my_math.py add:
# PI = 3.14
#
# Task:
# - import module;
# - print PI.

print('-' * 10, 'Task 5:', sep = '\n')

print('PI:', my_math_module.PI)

# Task 6: name Check
#
# Description:
# In my_math.py add:
# if name == 'main':
# print('Running directly')
#
# Task:
# - run file directly;
# - then import it in another file;
# - see difference.

print('-' * 10, 'Task 6:', sep = '\n')

# When running directly it prints - Running directly but when importing it doesn't