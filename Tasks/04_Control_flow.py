# Task 1: Stop at Number
#
# Description:
# Print numbers from 1 to 10
# using a loop.
#
# Stop the loop when the number becomes 5
# using break.
#
# The number 5 must not be printed.

print('-' * 10, 'Task 1:', sep='\n')

for i in range(1, 11):
    if i == 5:
        break

    print(i)

print('Result: done')

# Task 2: Skip Number
#
# Description:
# Print numbers from 1 to 10
# using a loop.
#
# Skip the number 5
# using continue.
#
# All other numbers must be printed.

print('-' * 10, 'Task 2:', sep='\n')

for i in range(1, 11):
    if i == 5:
        continue

    print(i)

print('Result: done')

# Task 3: First Negative Number
#
# Description:
# Given:
# numbers = [3, 7, 2, -5, 10, -1]
#
# Go through the list using a loop.
#
# When you find the first negative number:
# - print it;
# - stop the loop using break.
#
# Only the first negative number must be printed.

print('-' * 10, 'Task 3:', sep='\n')

numbers = [3, 7, 2, -5, 10, -1]

for number in numbers:
    if number < 0:
        print(number)
        break

print('Result: done')

# Task 4: Skip Negative Numbers
#
# Description:
# Given:
# numbers = [3, -2, 5, -1, 7]
#
# Go through the list using a loop.
#
# Skip all negative numbers
# using continue.
#
# Print only positive numbers.

print('-' * 10, 'Task 4:', sep='\n')

numbers = [3, -2, 5, -1, 7]

for number in numbers:
    if number < 0:
        continue

    print(number)

print('Result: done')

# Task 5: Password with Limit
#
# Description:
# Given:
# password = '1234'
#
# The user has 3 attempts to enter the correct password.
#
# For each attempt:
# - ask the user to enter a password;
# - if the password is correct, print 'Access granted'
#   and stop the loop using break;
# - otherwise, print 'Wrong password'.
#
# If all 3 attempts are used without success,
# print 'Access denied'.

print('-' * 10, 'Task 5:', sep='\n')

attempts = 0
password = '1234'

while attempts < 3:
    passw = input('Enter your password: ')

    if passw == password:
        print ('Access granted')
        break
    else:
        print('Wrong password')
    attempts += 1

if attempts == 3:
    print('Access denied')

# Task 6: Guess with Exit
#
# Description:
# Set a secret number in a variable.
#
# Ask the user to guess the number.
#
# Repeat until the user either guesses correctly
# or enters 'exit'.
#
# For each guess:
# - if the user enters 'exit', stop the loop using break;
# - if the guess is too high, print 'Too high';
# - if the guess is too low, print 'Too low';
# - if the guess is correct, print 'You win!'
#   and stop the loop.

print('-' * 10, 'Task 6:', sep='\n')

secret = '7'

while True:
    number = input('Enter a number or exit: ')

    if number == 'exit':
        break
    elif number == secret:
        print('You win!')
        break
    elif int(number) > int(secret):
        print('Too high')
    elif int(number) < int(secret):
        print('Too low')
