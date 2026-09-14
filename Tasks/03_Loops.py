# Task 1: Numbers from 1 to 10 (for)
#
# Description:
# Print numbers from 1 to 10 using a for loop.

print('-' * 10, 'Task 1:', sep='\n')

for i in range(1, 11):
    print(i)

print('Result: done')

# Task 2: Even Numbers (for)
#
# Description:
# Print all even numbers from 1 to 20.

print('-' * 10, 'Task 2:', sep='\n')

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print('Result: done')

# Task 3: Sum of Even Numbers (for)
#
# Description:
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
# Description:
# Print numbers from 10 to 1 in reverse order using a while loop.

print('-' * 10, 'Task 4:', sep='\n')

number = 10

while number > 0:
    print(number)
    number -= 1

print('Result: done')

# Task 5: Password Check (while)
#
# Description:
# Set a password (for example '1234').
#
# The program should:
# - ask the user to enter a password;
# - keep asking while the password is incorrect;
# - print 'Access granted' when the password is correct.

print('-' * 10, 'Task 5:', sep='\n')

passw = '1234'
password = input('Enter your password: ')

while password != passw:
    password = input('Password is incorrect, try again: ')

print('Access granted')

# Task 6: The user enters numbers.
#
# Description:
# The program should calculate the sum of the entered numbers until the user enters 0.

print('-' * 10, 'Task 6:', sep='\n')

total = 0
num = int(input('Enter a number: '))

while num != 0:
    total += num
    num = int(input('Enter a number: '))

print('Sum of the entered numbers:', total)

# Task 7: Count Vowels
#
# Description:
# Ask the user to enter a word and count how many vowels it contains.
#
# Requirements:
# - use a while loop;
# - check each character one by one;
# - consider a, e, i, o, and u as vowels;
# - increase the counter whenever a vowel is found;
# - print the total number of vowels.
#
# Example:
# word = 'education'
#
# Result:
# Number of vowels: 5

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

# Task 8: Remove Numbers
#
# Description:
# Given a string containing letters, spaces, and digits,
# create a new string with all numbers removed.
#
# Requirements:
# - use a while loop;
# - check each character one by one;
# - remove digits from 0 to 9;
# - keep all other characters unchanged;
# - preserve the original order of the remaining characters;
# - do not use .replace() or .isdigit().
#
# Example:
# line = '1Hello 5 Hi775 415'
#
# Result:
# Hello World

print('-' * 10, 'Task 8:', sep='\n')

line = '1Hello 5 Hi775 415'
clear_line = ''

numbers = '0123456789'
index = 0

while index < len(line):
    if line[index].lower() not in numbers:
        clear_line += line[index]

    index += 1

print('Line:', line, '\nClear line:', clear_line)

# Task 9: Replace Spaces
#
# Description:
# Given a string:
# line = 'Replace all spaces with _.'
#
# Create a new string where every space ' ' is replaced with an underscore '_'.
#
# Requirements:
# - use a while loop;
# - do not use .replace();
# - build the new string character by character;
# - keep all non-space characters unchanged.
#
# Example result:
# 'Replace_all_spaces_with_.'

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

# Task 10: Extract Numbers
#
# Description:
# Given a string containing letters, symbols, and digits, create a new string
# that contains only the numbers from the original string.
#
# Requirements:
# - use a while loop;
# - check each character one by one;
# - keep only digits from 0 to 9;
# - preserve the original order of the digits;
# - do not use .isdigit().
#
# Example:
# line = 'ss31317923wrwiiu$62162%#&4242d97ddd32323ffddffh%%*@ds33'
#
# Result:
# '31317923621624242973232333'

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

# Task 11: Calendar.
#
# Description:
# Given three inputs;
# - month - a tuple listing the dates of a SPECIFIC month (let's say December);
# - week_days - an auxiliary tuple listing the days of the week that exist;
# - first - the day of the week on which the first date of a SPECIFIC month falls.
#
# Need to print the calendar for this month in the terminal:
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

# Task 12: Strings
#
# Description:
# Ask the user to enter a text.
# Count how many vowels it contains.
#
# Vowels:
# a, e, i, o, u
#
# Ignore letter case.
#
# Example:
# Input:
# Hello World
#
# Result:
# Vowels: 3

print('-' * 10, 'Task 12:', sep='\n')

VOWELS = ('a', 'e', 'i', 'o', 'u')
text = input('Please enter a text: ')

vowels_count = 0

for char in text:
    if char.lower() in VOWELS:
        vowels_count += 1

print(f'There are {vowels_count} vowels in \'{text}\'.')

# Task 13: Number Streak
#
# Description:
# Given a list of numbers:
# some_numbers = [4, 4, 4, 2, 2, 7, 7, 7, 7, 3, 3, 5]
#
# Write a function longest_streak(numbers) that finds the
# longest sequence of identical consecutive numbers.
#
# Return:
# (number, count)
#
# Requirements:
# - do not use max() or count();
# - if several streaks have the same maximum length, return the first one;
# - the list contains at least one number.
#
# Bonus: also return the starting index of the longest streak:
# (7, 4, 5)

print('-' * 10, 'Task 13:', sep='\n')

some_numbers = [4, 4, 4, 2, 2, 7, 7, 7, 7, 3, 3, 5]


def longest_streak(numbers):
    current_number = numbers[0]
    streaks = []
    count = 0
    start_index = 0
    index = 0

    for number in numbers:
        if number == current_number:
            count += 1
        else:
            streaks.append((current_number, count, start_index))
            start_index = index
            current_number = number
            count = 1

        index += 1

    streaks.append((current_number, count, start_index))

    result = streaks[0]

    for number in streaks:
        if number[1] > result[1]:
            result = number

    return result


print('Result:', longest_streak(some_numbers))

# Task 14: Compress Sequence
#
# Description:
# Given a list of numbers:
# numbers = [1, 1, 1, 3, 3, 5, 2, 2, 2, 2, 7]
#
# Write a function compress_sequence(numbers) that compresses consecutive identical numbers.
#
# Return a list of tuples:
# [(1, 3), (3, 2), (5, 1), (2, 4), (7, 1)]
#
# Each tuple should contain the number and the number of its consecutive occurrences.
#
# Requirements:
# - do not use .count();
# - identical numbers belong to the same group only when they are consecutive;
# - do not modify the original list;
# - the list contains at least one number.

print('-' * 10, 'Task 14:', sep='\n')

numbers = [1, 1, 1, 3, 3, 5, 2, 2, 2, 2, 7]


def compress_sequence(numbers):
    result = []
    count = None
    previous_number = None

    for number in numbers:
        if previous_number is None:
            previous_number = number
            count = 1
            continue

        if number == previous_number:
            count += 1
        else:
            result.append((previous_number, count))
            previous_number = number
            count = 1

    result.append((previous_number, count))

    return result


print('Result:', compress_sequence(numbers), sep='\n')

# Task 15: Longest Word Streak
#
# Description:
# Given a string of words, write a function longest_word_streak(text)
# that finds the longest consecutive sequence where each next word is
# strictly longer than the previous one.
#
# Requirements:
# - words are separated by spaces;
# - compare words using their lengths;
# - each next word must be strictly longer;
# - if several sequences have the same maximum length, return the first one;
# - do not use max().
#
# Bonus: also return the number of words in the longest sequence.

print('-' * 10, 'Task 15:', sep='\n')

text = 'Python code is very easy to read and really fun to write'


def longest_word_streak(text):
    all_sequences = []
    increasing_sequence = []
    previous_word_length = None
    result = None

    for word in text.split():
        if previous_word_length is None:
            increasing_sequence.append(word)
            previous_word_length = len(word)
            continue

        if len(word) > previous_word_length:
            increasing_sequence.append(word)
            previous_word_length = len(word)
        else:
            all_sequences.append(increasing_sequence)
            increasing_sequence = [word]
            previous_word_length = len(word)

    all_sequences.append(increasing_sequence)

    for sequence in all_sequences:
        if result is None:
            result = sequence
            continue

        if len(result) < len(sequence):
            result = sequence

    return result, len(result)


print('Result:', longest_word_streak(text))
