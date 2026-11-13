# Task 1: Variables
#
# Description:
# Given the following variables:
# a = 2
# b = 5.3
# c = '5'
#
# Print the type of each variable using type().
#
# Then perform and print these operations:
# - a + b
# - a - b
# - a * b
# - a / b
#
# Do not change the original values of the variables.

print('-' * 10, 'Task 1:', sep='\n')

a = 2
b = 5.3
c = '5'

print('Integer: ', type(a), 'Float: ', type(b), 'String: ', type(c), sep='\n')
print('Addition: ', a+b, 'Subtraction: ', a-b, 'Multiplication: ', a*b, 'Division: ', a/b, sep='\n')

# Task 2: Convert Values
#
# Description:
# Given:
# c = '5'
# a = 2
#
# Convert:
# - c from str to int;
# - a from int to float.
#
# Store the converted values in new variables.
#
# Then calculate:
# result = converted_a + converted_c
#
# Print:
# - both converted values;
# - their types;
# - the final result.
#
# Do not change the original values of a and c.

print('-' * 10, 'Task 2:', sep='\n')

Add = float(a) + int(c)

print(Add)

# Task 3: Operators
#
# Description:
# Given:
# x = 10
# y = 3
#
# Calculate and print:
# - regular division using /;
# - floor division using //;
# - remainder using %;
# - power using **.
#
# Then explain the difference between:
# - / and //;
# - % and //.
#
# Do not change the original values of x and y.

print('-' * 10, 'Task 3:', sep='\n')

x = 10
y = 3

print('Division: ', x / y, 'Division to an integer: ', x // y,
      'Remainder from division: ', x % y, '', 'Power: ', x ** y, sep='\n')

# Task 4: Bus Station
#
# Description:
# Given:
# - num_tickets — the number of tickets sold;
# - bus_capacity — the number of passengers one bus can carry.
#
# Determine:
# - how many buses can be completely filled;
# - how many passengers remain after filling those buses.
#
# Store both results in new variables.
#
# Conditions:
# - num_tickets and bus_capacity are positive integers;
# - do not modify the original values
#   of num_tickets and bus_capacity;
# - use print() to display the results.
#
# Output:
# - first value — number of fully occupied buses;
# - second value — number of remaining passengers.

print('-' * 10, 'Task 4:', sep='\n')

num_tickets = 237
bus_capacity = 48

num_bus = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print('Number of full buses:', num_bus, '\nRemaining passengers:', num_left_passengers)

# Task 5: Strings
#
# Description:
# Given a string:
# text = 'abcde12345xyz6789'
#
# Find the longest consecutive sequence of digits and return it as a string.
#
# For the given example, the result should be:
# 12345
#
# For example:
# text = '12abc123xyz45'
#
# The result should be:
# 123
#
# Conditions:
# - use a loop;
# - do not use regular expressions;
# - do not use max();
# - if the string contains no digits, return an empty string ''.
#
# Bonus: if there are several consecutive digit sequences with the same maximum length, return the first one.

print('-' * 10, 'Task 5:', sep='\n')

text = 'abcde12345xyz6789'

numbers = '1234567890'
digit_sequences = ''

for char in text:
    if char in numbers:
        digit_sequences += char
    else:
        digit_sequences += ' '

numbers_from_next = digit_sequences.split()
long_sequ_numbers = ''

for number in numbers_from_next:
    if len(number) > len(long_sequ_numbers):
        long_sequ_numbers = number

print('The longest sequence of numbers in the text:', long_sequ_numbers, sep='\n')

# Task 6: Strings
#
# Description:
# Given a string:
# text = 'aaabbccccddeee'
#
# Write a function compress_text() that compresses the string by writing the number of
# consecutive identical characters followed by the character.
#
# For example:
# aaabbccccddeee
#
# Should become:
# 3a2b4c2d3e
#
# Conditions:
# - do not use Counter;
# - do not use itertools.groupby;
# - preserve the order of characters;
# - if a character appears only once consecutively, still write 1, for example ab → 1a1b;
# - the function should work with any non-empty string.
#
# Bonus: make the function handle an empty string correctly.

print('-' * 10, 'Task 6:', sep='\n')

some_text = 'aaabbccccddeee'


def compress_text(text):
    if not text:
        return ''

    repeat_char = text[0]
    char_count = []
    count = 0

    for char in text:
        if char == repeat_char:
            count += 1

        if char != repeat_char:
            char_count.append(str(count) + repeat_char)
            repeat_char = char
            count = 1

    char_count.append(str(count) + repeat_char)

    return ''.join(char_count)


print('Result:', compress_text(some_text))

# Task 7: Longest Word
#
# Description:
# Given a string:
# text = 'Python is a powerful programming language for developers'
#
# Write a function longest_word(text) that finds and returns the longest word.
#
# Requirements:
# - do not use max();
# - if several words have the same maximum length, return the first one;
# - do not change the letter case;
# - assume that words are separated by spaces.
#
# Bonus: return all words with the maximum length as a list.

print('-' * 10, 'Task 7:', sep='\n')

some_text = 'Python is a powerful programming language for developers'


def longest_word(text):
    words = text.split()
    longest = words[0]
    longest_words = []

    for word in words:
        if len(word) > len(longest):
            longest = word

    for word in words:
        if len(word) == len(longest):
            longest_words.append(word)

    return longest_words


print('Result:', longest_word(some_text))

# Task 8: Character Groups
#
# Description:
# Given a string:
# text = 'aaabbccccdaa'
#
# Write a function group_characters(text) that groups identical
# consecutive characters and returns them as a list of strings.
#
# Expected result:
# ['aaa', 'bb', 'cccc', 'd', 'aa']
#
# Requirements:
# - do not use .count();
# - characters belong to the same group only when they are consecutive;
# - preserve the original order;
# - the string contains at least one character.
#
# Bonus: return only groups containing two or more characters.

print('-' * 10, 'Task 8:', sep='\n')

text = 'aaabbccccdaa'


def group_characters(text):
    result = []
    previous_char = text[0]
    count = 0

    for char in text:
        if char == previous_char:
            count += 1

        else:
            if count > 1:
                result.append(count * previous_char)

            previous_char = char
            count = 1

    if count > 1:
        result.append(count * previous_char)

    return result


print('Result:', group_characters(text), sep='\n')

# Task 9: Word Chain
#
# Description:
# Given a list of words:
# words = ['apple', 'ear', 'rat', 'tree', 'egg']
#
# Write a function:
# validate_word_chain(words)
#
# Each next word must start with the last letter
# of the previous word.
#
# For the example above:
# apple -> ear -> rat -> tree -> egg
# so the function returns True.
#
# Conditions:
# - the list contains at least one word;
# - ignore letter case;
# - the same word cannot be used twice;
# - return False when the chain is broken;
# - do not modify the original list.
#
# Bonus:
# instead of False, return the index of the first word
# that breaks the chain. Return True if the chain is valid.

print('-' * 10, 'Task 9:', sep='\n')

words = ['apple', 'ear', 'rat', 'tree', 'egg']


def validate_word_chain(words):
    if not words:
        return

    previous_word = None
    used_words = set()

    for index, word in enumerate(words):
        word = word.lower()

        if previous_word is None:
            previous_word = word
            used_words.add(word)
            continue

        if word not in used_words and word[0] == previous_word[-1]:
            previous_word = word
            used_words.add(word)
        else:
            return index

    return True


print('Result:', validate_word_chain(words))
