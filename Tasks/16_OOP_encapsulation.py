# Task 1: Private Attribute
#
# Description:
#
# Create a class User
#
# Task:
#
# add attribute __password (private)
# try to print it outside class → there must be an error

print('-' * 10, 'Task 1:', sep = '\n')


class User:

    def __init__(self):
        self.__password = '1111'


user1 = User()

try:
    print(user1.password)

except AttributeError:
    print('AttributeError')

# Task 2: Getter Method
#
# Description:
#
# Access private data safely
#
# Task:
#
# add method get_password()
# return password
# print this using the method

print('-' * 10, 'Task 2:', sep = '\n')


class User:
    __password = '111111'

    def get_password(self):
        return self.__password


user2 = User()

print('You password:', user2.get_password())

# Task 3: Setter Method (Validation)
#
# Description:
#
# Control data before setting
#
# Task:
#
# add method set_password(new_password)
# if length < 6 → print error
# else → update password

print('-' * 10, 'Task 3:', sep = '\n')


class User:

    def __init__(self, password='111111'):
        self.__password = password

    def set_password(self, new_password):
        if len(new_password) < 6:
            print('Password must be at least 6 characters')
        else:
            self.__password = new_password
            print('Password updated')

    def get_password(self):
        return self.__password


user2 = User()

print('You password:', user2.get_password())
user2.set_password('1112888')
print('You password:', user2.get_password())

# Task 4: Protected Attribute
#
# Description:
#
# Create attribute with _
#
# Task:
#
# create class Person
# add _age
# print it outside class, understand difference _ vs __

print('-' * 10, 'Task 4:', sep = '\n')


class Person:
    _age = 20


p = Person()

print('Age:', p._age)
print('''
# _ you can apply outside class, but it is not advisable
# __ cannot be applied outside class
'''
)

# Task 5: Hide Balance (Bank Account)
#
# Description:
#
# Protect important data
#
# Task:
#
# Create class BankAccount
#
# private __balance
# method deposit(amount)
# method withdraw(amount)
# method get_balance()
#
# Rules:
# cannot change the balance directly
# cannot withdraw more than there is

print('-' * 10, 'Task 5:', sep = '\n')


class BankAccount:

    def __init__(self, balance=1000):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('Enter positive amount')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Enter positive amount')
        elif amount > self.__balance:
            print('You cannot withdraw more than you have')
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


User2 = BankAccount()

print('You balance:', User2.get_balance())
User2.deposit(300)
User2.withdraw(100)
print('You balance:', User2.get_balance())

# Task 6: Read-Only Property
#
# Description:
#
# Value that cannot be changed
#
# Task:
#
# create class Car
# private __brand
# only getter (without setter)

print('-' * 10, 'Task 6:', sep = '\n')


class Car:
    def __init__(self, brand='Ford'):
        self.__brand = brand

    def get_brand(self):
        return self.__brand


c = Car()

print('Brand:', c.get_brand())

# Task 7: Simple Encapsulation Practice
#
# Description:
#
# Combine everything
#
# Task:
#
# Create class Student
#
# private __grade
# setter:
# only 0–100
# getter:
# return grade

print('-' * 10, 'Task 7:', sep = '\n')


class Student:

    def __init__(self, grade):
        self.__grade = grade

    def set_grade(self, grade):
        if grade < 0 or grade > 100:
            print('Grade must be between 0 and 100')
        else:
            self.__grade = grade

    def get_grade(self):
        return self.__grade


st = Student('')

st.set_grade(10)
print('Grade:', st.get_grade())

# Task 8: Simple @property
#
# Description:
#
# Create a class User
#
# Requirements:
#
# private attribute _name
# getter using @property
# setter using @name.setter
#
# Rules:
#
# name must not be empty
# if empty → print error
# else → update value
#
# Test:
#
# create object
# set name
# print name

print('-' * 10, 'Task 8:', sep = '\n')


class User:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == '':
            print('Name cannot be empty')
            self._name = None
        else:
            self._name = name


n = User('')

# Task 9: Temperature
#
# Description:
#
# Create a Temperature class that:
#
# accepts temperature values in degrees Celsius
# has a celsius property
# does not allow values below -273.15 (absolute zero)

print('-' * 10, 'Task 9:', sep = '\n')


class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        if temperature < -273.15:
            print('An impossible temperature')
            self._temperature = None
        else:
            self._temperature = temperature


t = Temperature(-293.15)

# Task 10: Email
# Description:
#
# Create a User class that:
#
# has an email address
# does not allow an email address to be set without an '@'

print('-' * 10, 'Task 10:', sep = '\n')


class User:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email:
            print('An email address must contain the @ symbol')
            self._email = None
        else:
                self._email = email


u = User('1111аа')
