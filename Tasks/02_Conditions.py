# Task 1: Even or Odd Number
#
# Write a program that:
#
# Asks the user for a number.
# Prints 'The number is even' if the number is divisible by 2.
# Prints 'The number is odd' if it is not divisible by 2.

print('-' * 10, 'Task 1:', sep='\n')

number = int(input('Enter a number: '))

if number % 2 == 0:
    print('The number is even')
else:
    print('An odd number')

# Task 2: Grade Based on Score
#
# The user enters a number from 0 to 100 — their test score.
# The program should print a grade:
#
# 90–100 → 'Excellent'
# 75–89 → 'Good'
# 60–74 → 'Satisfactory'
# Less than 60 → 'Needs Improvement'
# If the number is not in 0–100 → 'Invalid score'

print('-' * 10, 'Task 2:', sep='\n')

number = int(input('Enter a number: '))

if number < 0 or number > 100:
    print('Invalid score')
elif number >= 90:
    print('Excellent')
elif number >= 75:
    print('Good')
elif number >= 60:
    print('Satisfactory')
else:
    print('Needs Improvement')

# Task 3: Determine the Season
#
# The user enters the month number (1–12).
# The program should print the season:
#
# 12, 1, 2 → 'Winter'
# 3, 4, 5 → 'Spring'
# 6, 7, 8 → 'Summer'
# 9, 10, 11 → 'Autumn'
# Any other number → 'Invalid month number'

print('-' * 10, 'Task 3:', sep='\n')

month = int(input('Enter a number month: '))

if month == 12 or month == 1 or month == 2:
    print('Winter')
elif month == 3 or month == 4 or month == 5:
    print('Spring')
elif month == 6 or month == 7 or month == 8:
    print('Summer')
elif month == 9 or month == 10 or month == 11:
    print('Autumn')
else:
    print('Invalid month number')

# Task 4: Login Check
#
# The user enters a login name.
#
# If the login is 'admin' → 'Welcome, administrator!'
# If the login is 'guest' → 'Welcome, guest!'
# Any other login → 'Unknown user'

print('-' * 10, 'Task 4:', sep='\n')

login_name = input('Please enter your login name: ')

if login_name == 'admin':
    print('Welcome, administrator!')
elif login_name == 'guest':
    print('Welcome, guest!')
else:
    print('Unknown user')

# Task 5: Maximum of Three Numbers
#
# The user enters three numbers.
# The program should print the largest number among them. Use if, elif, else (do not use the max function).

print('-' * 10, 'Task 5:', sep='\n')

number1 = int(input('Enter a number 1: '))
number2 = int(input('Enter a number 2: '))
number3 = int(input('Enter a number 3: '))

if number1 == number2 and number1 == number3 and number2 == number3:
    print('Numbers are equal')
elif number1 > number2 and number1 > number3:
    print('Number is the largest:', number1)
elif number2 > number3:
    print('Number is the largest:', number2)
else:
    print('Number is the largest:', number3)

# Task 6: Need to determine their age group:
# - 0–12 years inclusive – child;
# - 13–17 years inclusive – teenager;
# - 18–149 years inclusive – adult;
# - all others – age not specified.
#
# What constitutes a valid result: the terminal must display the corresponding message:
# child or teenager or adult or no such age exists AND SPECIFY THIS NUMBER.

print('-' * 10, 'Task 6:', sep='\n')

age = int(input('Enter age: '))

if 0 <= age <= 12:
    print(age, 'is a child')
elif 13 <= age <= 17:
    print(age, 'is a teenager')
elif 18 <= age <= 149:
    print(age, 'is a adult')
else:
    print('No such age exists')

# Task 7: Bus station.

print('-' * 10, 'Task 7:', sep='\n')

num_tickets = 444
bus_capacity = 30

num_bus = round(num_tickets / bus_capacity)
num_left_passengers = num_tickets % bus_capacity

if num_left_passengers == 0:
    empty_seats = 0
else:
    empty_seats = bus_capacity - num_left_passengers

print('Number of buses:', num_bus, '\nRemaining passengers:', num_left_passengers, '\nEmpty seats:', empty_seats)

# Task 8: The user enters their first name and then their surname separately.
# The program must be designed so that, if they enter everything correctly,
# their first name and surname are combined into a single line (as a single new string) and displayed in the terminal.
# However, if they make a mistake and enter both their first name and surname into the 'first name'
# field of the form at the same time, the following message will be displayed:
# 'Please fill in the form carefully!' and the program will terminate.

print('-' * 10, 'Task 8:', sep='\n')

name = input('Enter your name: ')
surname  = input('Enter your surname: ')

if ' ' in name or ' ' in surname:
    print('Please fill in the form carefully!')
else:
    full_name = name + ' ' + surname
    print('Full name:', full_name)

# Task 9: 'URL Normalisation'
# You need to normalise a URL to its full format, including the https:// protocol and the www subdomain. Example:
# youtube.com
# became https://www.youtube.com
#
# Task clarification:
# These are strings (str).
#
# The input (in this case, the variable url) may contain ONLY three possible cases (the domain is irrelevant):
# 1) A fully normalised URL:
# 'https://www.example.com'
#
# 2) Without specifying a transfer/encryption protocol:
# 'www.example.com'
#
# 3) Just the domain without a protocol or the www subdomain:
# 'example.com'
#
# 4) Do not attempt to account for the existence of the http protocol (without the “s”).
#
# Technical points:
# 1) As the input function cannot be used here, use the url variable as the source of input data. (Store strings containing addresses in it to test the code).
# 2) After the code has been executed, the url variable should contain a string with a valid URL address.

# There are three possible input options:
# 'https://www.example.com'
# 'www.example.com'
# 'example.com'

# The url variable (cannot be renamed).
# To test different cases, change the values in the variable.

print('-' * 10, 'Task 9:', sep='\n')

url = 'example.com'

if 'www.' not in url:
    url = 'https://www.' + url
elif 'https://' not in url:
    url = 'https://' + url

print('Correct URL:', url)
