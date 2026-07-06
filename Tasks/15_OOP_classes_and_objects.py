# Task 1: Create Class Person
#
# add attributes:
# name
# age
#
# create object
#
# print both values

print('-' * 10, 'Task 1:', sep = '\n')


class Person:
    name = None
    age = None

p = Person()
p.name = 'Bohdan'
p.age = 30


print('Name:', p.name)
print('Age:', p.age)

# Task 2: Method Inside Class
#
# method greet()
#
# should print:
# Hello, my name is <name>

print('-' * 10, 'Task 2:', sep = '\n')


class Person:
    name = None
    age = None

    def set_name(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, my name is {self.name}')


p = Person()
p.set_name('Bohdan')

p.greet()

# Task 3: Constructor (__init__)
#
# initialize name and age via __init__
# create 2 objects with different data
#
# call method from Task 2

print('-' * 10, 'Task 3:', sep = '\n')


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}, my age is {self.age}')


p1 = Person('Bohdan', 30)
p2 = Person('Victoria', 30)

p1.greet()
p2.greet()

# Task 4: Update Attributes
#
# create method have_birthday()
# increase age by 1
#
# print updated age

print('-' * 10, 'Task 4:', sep = '\n')


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1
        print(f'Now I am {self.age}')


p = Person('Bohdan', 30)
p.have_birthday()

# Task 5: Shopping Cart Item
#
# Create class Product:
# attributes:
# name
# price
# quantity
#
# method:
# total_price()
#
# → returns price * quantity

print('-' * 10, 'Task 5:', sep = '\n')


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


p = Product('banana', 10, 5)

print(f'Total price: {p.total_price()}')

# Task 6: Class with Multiple Objects
#
# create 3 products
# store in list
# loop through list
#
# print total price for each

print('-' * 10, 'Task 6:', sep = '\n')


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


p1 = Product('banana', 10, 5)
p2 = Product('apple', 11, 7)
p3 = Product('orange', 15, 6)

cart = [p1, p2, p3]

print('The total price:')
for product in cart:
    print(product.total_price())

# Task 7: Bank Account (Mini Project)
#
# Create class BankAccount:
# attribute:
# balance
#
# methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
#
# Rules:
# cannot withdraw more than balance
#
# print message if not enough money

print('-' * 10, 'Task 7:', sep = '\n')


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('Enter a positive number')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money')
        elif amount <= 0:
            print('Enter a positive number')
        else:
            self.balance -= amount

    def show_balance(self):
        print('Your balance:', self.balance)


user = BankAccount(110)
user.deposit(10)
user.withdraw(110)
user.show_balance()

# Task 8: Shared variable
#
# create class User
#
# add class variable:
# user_count = 0
# increase it each time new object created
#
# print total users

print('-' * 10, 'Task 8:', sep = '\n')


class User:
    user_count = 0

    def __init__(self, balance):
        self.balance = balance
        User.user_count += 1

    def deposit(self, amount):
        if amount <= 0:
            print('Enter a positive number')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money')
        elif amount <= 0:
            print('Enter a positive number')
        else:
            self.balance -= amount


user1 = User(100)
user2 = User(100)
user3 = User(100)

print(User.user_count)

# Task 9: __str__ Method
#
#
# add __str__ to class Person
#
# format:
# Name: Bohdan, Age: 30

print('-' * 10, 'Task 9:', sep = '\n')


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello, my name is {self.name}, my age is {self.age}'


p1 = Person('Bohdan', 30)
p2 = Person('Victoria', 30)

print(p1)
print(p2)

# Task 10: URL Parser
#
# Create a URL class.
#
# Parse a URL into:
# - protocol
# - domain
# - path
#
# Implement:
# - get_protocol()
# - get_domain()
# - get_bread_crumbs()
#
# Return None if the protocol or path is missing.

print('-' * 10, 'Task 10:', sep = '\n')


class URL:
    def __init__(self, url):
        self.url = url

        if '://' in self.url:
            self.protocol, remainder = self.url.split('://', 1)
        else:
            self.protocol = None
            remainder = self.url

        if '/' in remainder:
            self.domain, bread_crumbs = remainder.split('/', 1)
            self.bread_crumbs = '/' + bread_crumbs if bread_crumbs else None
        else:
            self.domain = remainder
            self.bread_crumbs = None

    def get_protocol(self):
        return self.protocol

    def get_domain(self):
        return self.domain

    def get_bread_crumbs(self):
        return self.bread_crumbs


example_url_1 = URL('www.google.com')
example_url_2 = URL('www.google.com/')
example_url_3 = URL('https://www.udemy.com/python-full-course')

print('Protocol:', example_url_1.get_protocol())
print('Protocol:', example_url_2.get_protocol())
print('Protocol:', example_url_3.get_protocol())

print('Domain:', example_url_1.get_domain())
print('Domain:', example_url_2.get_domain())
print('Domain:', example_url_3.get_domain())

print('Bread crumbs:',example_url_1.get_bread_crumbs())
print('Bread crumbs:',example_url_2.get_bread_crumbs())
print('Bread crumbs:',example_url_3.get_bread_crumbs())

# Task 11: URL Objects (continuation of Task 10)
#
# Create a list of URL objects from the given list of URL strings.
#
# Remove all objects that contain bread crumbs (path).
#
# Print:
# 1. The list of remaining objects.
# 2. Each object using a for loop.
#
# Note:
# The list should contain only URLs without a path.

print('-' * 10, 'Task 11:', sep = '\n')

urls = ['https://www.udemy.com/python-full-course',
        'https://www.udemy.com',
        'https://www.google.com',
        'https://www.youtube.com',
        'https://www.youtube.com/shorts',
        'https://www.youtube.com/feed/subscriptions'
        ]

urls_like_obj = []

for url in urls:
    urls_like_obj.append(URL(url))

index = 0

while index < len(urls_like_obj):
    if urls_like_obj[index].get_bread_crumbs():
        del urls_like_obj[index]
    else:
        index += 1

for item in urls_like_obj:
    print(item.url)

print('Result: done')
