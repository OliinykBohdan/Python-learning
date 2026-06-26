# Task 1: Simple Decorator
# Description:
#
# Create a decorator:
#
# def my_decorator(func):
#
# It should:
#
# print 'Start' before function call
# call the function
# print "End" after

print('-' * 10, 'Task 1:', sep='\n')


def my_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


@my_decorator
def my_function():
    print('Hello')

my_function()

# Task 2: Decorator with Arguments
# Description:
#
# Modify the decorator so it works with any function:
#
# use *args, **kwargs

print('-' * 10, 'Task 2:', sep='\n')


def sum_numbers(func):
    def wrapper (*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return wrapper


@sum_numbers
def numbers(a, b):
    print(a + b)

numbers(2, 3)

# Task 3: Return Value
#  Description:
#
# Create a decorator that:
#
# calls a function
# returns its result
# prints 'Result is: <result>'

print('-' * 10, 'Task 3:', sep='\n')


def decorator_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Result is: {result}')
        return result
    return wrapper


@decorator_result
def numbers(a, b):
     return a * b

numbers(2, 5)

# Task 4: Access Control
# Description:
#
# Create a decorator:
#
# def check_password(func):
#
# It should:
#
# ask user for password
# if correct → call function
# if wrong → print "Access denied"

print('-' * 10, 'Task 4:', sep='\n')


def check_password(func):
    def wrapper():
        password = input('Enter password: ')
        if password == '1111':
            return func ()
        else:
            print('Access denied')
    return wrapper


@check_password
def login():
    print('Secret data')

login()

# Task 5: Call Counter
# Description:
#
# Create a decorator that:
#
# counts how many times a function was called
# prints:
# Called 1 times
# Called 2 times

print('-' * 10, 'Task 5:', sep='\n')


def how_many(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        func ()
        print(f'Called {count} times')
    return wrapper


@how_many
def hello():
    print('Hi')

hello()
hello()

# Task 6: Repeat Function
# Description:
#
# Create a decorator:
#
# def repeat(n):
#
# It should:
#
# call function n times

print('-' * 10, 'Task 6:', sep='\n')


def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator


@repeat(3)
def function_n_times():
    print('Hi')

function_n_times()

# Task 7: Logger (mini real-life)
# Description:
#
# Create a decorator that:
#
# prints function name
# prints arguments

print('-' * 10, 'Task 7:', sep='\n')


def function_name(func):
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__}')
        print(f'Args: {args}')
        return func(*args, **kwargs)
    return wrapper


@function_name
def function_n_times(a, b):
    return a, b


function_n_times(2, 3)

# Task 8: Timer
# Description:
#
# Create a decorator that:
#
# measures execution time
# prints it

print('-' * 10, 'Task 8:', sep='\n')

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start}')
        return result
    return wrapper


@timer
def slow():
    for i in range(1000000):
        pass


slow()
