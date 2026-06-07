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

# Task 7: Count the number of vowels.

print('-' * 10, 'Task 7:', sep='\n')

word = input('Enter a word: ')
vowels = 'aeiou'

number_vowels = 0
index = 0

while index < len(word):
    if word[index] in vowels:
        number_vowels += 1

    index += 1

print('Number of vowels:', number_vowels)

# Task 8: Remove all numbers from a string.

print('-' * 10, 'Task 8:', sep='\n')

line = '1Hello? 5 Hi77!5 415'
clear_line = ''

numbers = '0123456789'
index = 0

while index < len(line):
    if line[index].lower() not in numbers:
        clear_line += line[index]

    index += 1

print('Line:', line, '\nClear line:', clear_line)

# Task 9: Replace all spaces with _..

print('-' * 10, 'Task 9:', sep='\n')

line = 'Replace all spaces with _.'
new_line = ''

index = 0

while index < len(line):
    if line[index] == ' ':
        new_line += '_'
    else:
        new_line += line[index]

    index += 1

print(new_line, '\nResult: done')

# Task 10: Leave only the numbers.

print('-' * 10, 'Task 10:', sep='\n')

line = 'ss31317923wrwiiu$62162%#&4242d97ddd32323ffddffh%%*@ds33'
new_line = ''

numbers = '1234567890'
index = 0

while index < len(line):
    if line[index] in numbers:
        new_line += line[index]

    index += 1

print('Numbers in line:', new_line)

# Task 11: Calendar. You have three inputs:
#
# - month - a tuple listing the dates of a SPECIFIC month (let's say December).
# - week_days - an auxiliary tuple listing the days of the week that exist.
# - first - the day of the week on which the first date of a SPECIFIC month falls.
#
# You need to print the calendar for this month in the terminal:
#
# M T W T F S S
#     1 2 3 4 5
# 6 7 8 9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31

print('-' * 10, 'Task 11:', sep='\n')

month = (1, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 11, 12, 13, 14,
         15, 16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27, 28,
         29, 30, 31)

week_days = ('Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday')
first = 'Wednesday'

day_in_week = 0

while day_in_week < len(week_days):
    print(week_days[day_in_week][0], end='  ')
    day_in_week += 1

print(end='\n')

start_position = week_days.index(first)

print('   ' * start_position, end='')

day_in_month = 0
month_start_day = start_position

while day_in_month < len(month):
    if day_in_month > 8:
        print(month[day_in_month], end=' ')
    else:
        print(month[day_in_month], end='  ')

    if week_days[month_start_day] == 'Sunday':
        print(end='\n')
        month_start_day = -1

    day_in_month += 1
    month_start_day += 1
