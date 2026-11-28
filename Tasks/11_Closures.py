# Task 1: Personal Message
#
# Description:
# Write a function:
# make_message(text)
#
# The function receives a string
# and must return an inner function.
#
# The inner function must:
# - remember the original text using a closure;
# - print the text each time it is called.
#
# Example:
# hello = make_message('Hello world')
#
# hello()
# hello()
#
# Expected output:
# Hello world
# Hello world

print('-' * 10, 'Task 1:', sep='\n')


def make_message(text):
    def say_hello ():
        print (text)
    return say_hello


hello = make_message('Hello world')

print('Result:')
hello()
hello()

# Task 2: Add Number
#
# Description:
# Write a function:
# add_n(n)
#
# The function receives a number n
# and must return an inner function.
#
# The inner function must:
# - remember the value of n using a closure;
# - accept another number;
# - return the sum of that number and n.
#
# Example:
# add5 = add_n(5)
#
# add5(10) -> 15
# add5(3)  -> 8

print('-' * 10, 'Task 2:', sep='\n')


def add_n(n):
    def adding (x):
        return x + n
    return adding


add5 = add_n(5)

print('Result:')
print(add5(10))
print(add5(3))

# Task 3: Step Counter
#
# Description:
# Write a function:
# make_counter(step)
#
# The function receives a step value
# and must return an inner function.
#
# The counter starts at 0.
#
# The inner function must:
# - remember the counter value using a closure;
# - increase the counter by step on each call;
# - return the updated counter value.
#
# Use nonlocal to modify the counter.
#
# Example:
# c = make_counter(2)
#
# c() -> 2
# c() -> 4
# c() -> 6

print('-' * 10, 'Task 3:', sep='\n')


def make_counter(step):
    count = 0
    def counter ():
        nonlocal count
        count += step
        return count
    return counter


c = make_counter(2)

print('Result:')
print(c())
print(c())
print(c())

# Task 4: Bank Account
#
# Description:
# Write a function:
# bank_account(start_money)
#
# The function receives an initial balance
# and must return an inner function.
#
# The inner function must:
# - remember the current balance using a closure;
# - accept an amount;
# - increase the balance if the amount is positive;
# - decrease the balance if the amount is negative;
# - return the updated balance.
#
# Use nonlocal to modify the balance.
#
# Example:
# account = bank_account(100)
#
# account(50)  -> 150
# account(-30) -> 120

print('-' * 10, 'Task 4:', sep='\n')


def bank_account(start_money):
    balance = start_money
    def account1 (money):
        nonlocal balance
        balance += money
        return balance
    return account1


account = bank_account(100)

print('Result:')
print(account(50))
print(account(-30))

# Task 5: Counter
#
# Description:
# Write a function:
# create_counter()
#
# The function must initialize a variable count = 0
# and return an inner function.
#
# The inner function must:
# - remember the current count using a closure;
# - increase count by 1 on each call;
# - return the updated count.
#
# Use nonlocal to modify the count variable.
#
# Example:
# counter = create_counter()
#
# counter() -> 1
# counter() -> 2
# counter() -> 3

print('-' * 10, 'Task 5:', sep='\n')


def create_counter():
    count = 0
    def counter ():
        nonlocal count
        count += 1
        return count
    return counter


count_1 = create_counter()

print('Result:')
print(count_1())
print(count_1())
print(count_1())

# Task 6: Custom Multiplier
#
# Description:
# Write a function:
# make_multiplier(n)
#
# The function receives a multiplier n
# and must return an inner function.
#
# The inner function must:
# - remember the value of n using a closure;
# - accept a number x;
# - multiply x by n;
# - return the result.
#
# Example:
# multiply_by_3 = make_multiplier(3)
#
# multiply_by_3(5)  -> 15
# multiply_by_3(10) -> 30

print('-' * 10, 'Task 6:', sep='\n')


def make_multiplier(n):
    def multiplier (x):
        return x * n
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print('Result:')
print(double(5))
print(triple(5))

# Task 7: Unique File Names
#
# Description:
# Given a set of existing files:
# existing_files = {'report.txt', 'report_1.txt', 'photo.jpg'}
#
# Write a function:
# create_filename_generator(existing_files)
#
# The function must return an inner function
# that accepts a new file name.
#
# Rules:
# - if the name is available, return it unchanged;
# - if it is taken, add _1, _2, _3, etc.
#   before the file extension;
# - use the smallest available number;
# - each returned name becomes reserved.
#
# Use a closure to remember reserved file names.
# Do not modify the original existing_files set.
#
# Example of consecutive calls:
# generate = create_filename_generator(existing_files)
#
# generate('report.txt') -> 'report_2.txt'
# generate('report.txt') -> 'report_3.txt'
# generate('photo.jpg')  -> 'photo_1.jpg'
# generate('notes.txt')  -> 'notes.txt'
# generate('notes.txt')  -> 'notes_1.txt'
#
# Condition: each file name contains exactly one dot.

print('-' * 10, 'Task 7:', sep='\n')

existing_files = {'report.txt', 'report_1.txt', 'photo.jpg'}


def create_filename_generator(existing_files):
    reserved_files = existing_files.copy()

    def generate(filename):
        if filename not in reserved_files:
            reserved_files.add(filename)
            return filename

        unique_name = filename
        name, extension = filename.split('.')
        counter = 1

        while unique_name in reserved_files:
            unique_name = name + '_' + str(counter) + '.' + extension
            counter += 1

        reserved_files.add(unique_name)

        return unique_name

    return generate


generate = create_filename_generator(existing_files)

print('Result:')
print(generate('report.txt'))
print(generate('report.txt'))
