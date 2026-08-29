# Task 1: Variables
#
# Description:
# a = 2 (int)
# b = 5.3 (float)
# c = '5' (str)
#
# Print the type of each variable using type()
#
# Perform operations:
# a + b
# a - b
# a * b
# a / b

print('-' * 10, 'Task 1:', sep='\n')

a = 2
b = 5.3
c = '5'

print('Integer: ', type(a), 'Float: ', type(b), 'String: ', type(c), sep='\n')
print('Addition: ', a+b, 'Subtraction: ', a-b, 'Multiplication: ', a*b, 'Division: ', a/b, sep='\n')

# Task 2: Convert
#
# Description:
# c (string '5') to a number
# a to float
#
# Perform calculation:
# result = a + int(c)

print('-' * 10, 'Task 2:', sep='\n')

Add = float(a) + int(c)

print(Add)

# Task 3: Operators
#
# Description:
# x = 10
# y = 3
#
# Find:
# regular division /
# floor division //
# remainder %
# power
#
# Explain the difference between:
# / and //
# % and //

print('-' * 10, 'Task 3:', sep='\n')

x = 10
y = 3

print('Division: ', x / y, 'Division to an integer: ', x // y, 'Remainder from division: ', x % y, '', 'Power: ', x ** y, sep='\n')

# Task 4: Bus station
#
# Description:
# You need to determine how many buses to dispatch, depending on the number of tickets sold, as well as
# the number of passengers who could not be accommodated on a fully occupied bus.
#
# Clarification of the task:
# - you need to determine the number of fully occupied buses;
# - you need to determine the number of remaining passengers (tickets purchased) who could
# not be accommodated on a full bus.
#
# Technical aspects of the task:
# - The number of tickets purchased and the capacity of the buses are known;
# - do not change the names of the initial variables num_tickets and bus_capacity;
# - do not assign new values resulting from calculations to the variables num_tickets and
# bus_capacity within the program; create new variables for the results;
# - however, you may change the initial values of these variables. The values must be positive integers of type int;
# - you may use as many variables as you need to solve the problem;
# - output the result using the print function. The first argument is the number of buses;
# the second, separated by a comma, is the number of remaining passengers.

print('-' * 10, 'Task 4:', sep='\n')

num_tickets = 237
bus_capacity = 48

num_bus = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print('Number of full buses:', num_bus, '\nRemaining passengers:', num_left_passengers)

# Task 5: Strings
#
# Description:
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
