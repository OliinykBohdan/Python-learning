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
