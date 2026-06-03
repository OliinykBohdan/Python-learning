# Task 1: Numbers from 1 to 10 (for)
#
# Print numbers from 1 to 10 using a for loop.

print('-' * 10, 'Task 1:', sep='\n')

for i in range(1, 11):
    print(i)

print('Result: done')

# Task 2: Even Numbers (for)
#
# Print all even numbers from 1 to 20.

print('-' * 10, 'Task 2:', sep='\n')

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print('Result: done')
# Task 3: Sum of Even Numbers (for)
#
# The user enters a number n.
# You need to calculate the sum of only even numbers from 1 to n.

print('-' * 10, 'Task 3:', sep='\n')

n = int(input('Enter a number: '))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print(total)
print('Result: done')

# Task 4: Numbers from 10 to 1 (while)
#
# Print numbers from 10 to 1 in reverse order using a while loop.

print('-' * 10, 'Task 4:', sep='\n')

number = 10

while number > 0:
    print(number)
    number -= 1

print('Result: done')

# Task 5: Password Check (while)
#
# Set a password (for example '1234').
# The program should:
#
# ask the user to enter a password
# keep asking while the password is incorrect
# print 'Access granted' when the password is correct

print('-' * 10, 'Task 5:', sep='\n')

passw = '1234'
password = input('Enter your password: ')

while password != passw:
    password = input('Password is incorrect, try again: ')

print('Access granted')

# Task 6: The user enters numbers.
# The program should calculate the sum of the entered numbers until the user enters 0.

print('-' * 10, 'Task 6:', sep='\n')

total = 0
num = int(input('Enter a number: '))

while num != 0:
    total += num
    num = int(input('Enter a number: '))

print('Sum of the entered numbers:', total)
