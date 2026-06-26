# Task 1: Personal Message
#
# Create a function:
#
# make_message(text)
#
# It should return a function that prints the text.
#
# Example:
#
# hello = make_message('Hello world')
#
# hello()
# hello()

print('-' * 10, 'Task 1:', sep='\n')


def make_message(text):
    def say_hello ():
        print (text)
    return say_hello


hello = make_message('Hello world')

hello()
hello()

# Task 2: Add Number
#
# Create a function:
#
# add_n(n)
#
# Example:
#
# add5 = add_n(5)
#
# add5(10)  # 15
# add5(3)   # 8

print('-' * 10, 'Task 2:', sep='\n')


def add_n(n):
    def adding (x):
        return x + n
    return adding


add5 = add_n(5)

print(add5(10))
print(add5(3))

# Task 3: Step Counter
#
# Create a function:
#
# make_counter(step)
#
# Example:
#
# c = make_counter(2)
#
# c()
# c()
# c()

print('-' * 10, 'Task 3:', sep='\n')


def make_counter(step):
    count = 0
    def counter ():
        nonlocal count
        count += step
        return count
    return counter


c = make_counter(2)

print(c())
print(c())
print(c())

# Task 4: Bank Account
#
# Create a function:
#
# bank_account(start_money)
#
# Example:
#
# account = bank_account(100)
#
# account(50)
# account(-30)

print('-' * 10, 'Task 4:', sep='\n')


def bank_account(start_money):
    balance = start_money
    def account1 (money):
        nonlocal balance
        balance += money
        return balance
    return account1


account = bank_account(100)

print(account(50))
print(account(-30))

# Task 5: Counter (Closure + nonlocal)
# Description:
#
# Create a function:
#
# def create_counter():
#
# This function should:
#
# create a variable count = 0
# define an inner function
# each time the inner function is called:
# increase count by 1
# return current value

print('-' * 10, 'Task 5:', sep='\n')


def create_counter():
    count = 0
    def counter ():
        nonlocal count
        count += 1
        return count
    return counter


count_1 = create_counter()

print(count_1())
print(count_1())
print(count_1())

# Task 6: Custom Multiplier (Closure Factory)
# Description:
#
# Create a function:
#
# def make_multiplier(n):
#
# This function should:
#
# return another function
# the inner function takes one argument x
# returns x * n

print('-' * 10, 'Task 6:', sep='\n')


def make_multiplier(n):
    def multiplier (x):
        return x * n
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))