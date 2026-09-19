import math #import used in Task 12

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

# Task 12: Area of a rectangle
#
# Extend the class using __round__, __ceil__ and __floor__
# An object representing a rectangle must support passing itself as an argument to the functions round,
# math.ceil and math.floor. The rectangle’s main characteristic—its area—is used as the property for rounding.
#
# Complete the implementation of the __round__, __ceil__ and __floor__ methods.
#
# When an instance is passed to the corresponding functions round,
# math.ceil and math.floor, the rounded value of the rectangle’s area (area) must be returned.

print('-' * 10, 'Task 12:', sep = '\n')


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __round__(self, ndigits):
        return round(self.area(), ndigits)

    def __ceil__(self):
        return math.ceil(self.area())

    def __floor__(self):
        return math.floor(self.area())


rectangle = Rectangle(4.4, 5.1)

print('Rounding of area:', round(rectangle, 1))
print('Rounding the area up:', math.ceil(rectangle))
print('Rounding an area down:', math.floor(rectangle))

# Task 13: Does the text contain spam?
# Create a Message class with a text attribute and a spam attribute.
# The text of the message is passed to the text attribute when the object is created,
# whilst the spam attribute is initially set to None.
#
# Add the following methods:
# - is_spam – which checks whether the text contains any of the words
# defined as spam criteria, and returns True or False
# - when the is_spam method is called, in addition to returning True or False,
# the self.spam attribute is set to the corresponding value.
# - and add __len__, which returns the length of the text.

print('-' * 10, 'Task 13:', sep = '\n')


class Message:
    def __init__(self, text):
        self.text = text.lower()
        self.spam = None

    def is_spam(self, text_spam):
        for word in text_spam:
            if word in self.text:
                self.spam = True
                return True

        self.spam = False
        return False

    def __len__(self):
        return len(self.text)


some_text = Message('Hello, my friend!')

print('Presence of spam in the text:', some_text.is_spam(('buy', 'sell', 'exchange')))
print('Text length:', len(some_text))

# Task 14: Password checker
#
# Description:
# Create a class called PasswordChecker. The check method returns True if the password:
# - is at least 8 characters long
# - contains at least one digit

print('-' * 10, 'Task 14:', sep = '\n')


class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check(self):
        digits = '1234567890'

        if len(self.password) < 8:
            return False

        for char in self.password:
            if char in digits:
                return True

        return False


passw = PasswordChecker('dddH2Ioo')

print('Result:', passw.check())

# Task 15: OOP
#
# Description:
# Create a class ShoppingCart that stores products and their quantities.
#
# The object should be created like this:
# cart = ShoppingCart()
#
# Methods:
# - add_item(name, quantity) — adds an item to the cart; if the item already exists, increase its quantity;
# - remove_item(name, quantity) — decreases the quantity of an item;
# - show_cart() — returns a dictionary containing the current contents of the cart.
#
# Conditions:
# - the quantity must be greater than 0;
# - if the item does not exist when removing it — do nothing;
# - if the quantity becomes 0 after removing an item — completely remove the item;
# - the cart state must be stored inside the object.
#
# Example:
# cart.add_item('Apple', 3)
# cart.add_item('Apple', 2)
# cart.add_item('Banana', 4)
#
# cart.remove_item('Apple', 1)
#
# print(cart.show_cart())
#
# Expected result:
# {'Apple': 4, 'Banana': 4}

print('-' * 10, 'Task 15:', sep = '\n')


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if quantity <= 0:
            return

        self.items[name] = self.items.get(name, 0) + quantity

    def remove_item(self, name, quantity):
        if quantity <= 0:
            return

        if name not in self.items:
            return

        self.items[name] -= quantity

        if self.items[name] <= 0:
            del self.items[name]

    def show_cart(self):
        return self.items.copy()


cart = ShoppingCart()

cart.add_item('Apple', 3)
cart.add_item('Apple', 2)
cart.add_item('Banana', 4)

cart.remove_item('Apple', 1)

print('Cart:', cart.show_cart(), sep='\n')

# Task 16: Library Book
#
# Description:
# Create a Book class representing a book in a library.
#
# The class should have:
# - title — book title;
# - author — author;
# - is_borrowed — whether the book is currently borrowed.
#
# Methods:
# borrow()
# return_book()
#
# Rules:
# - borrow() can borrow the book only if it is available;
# - if the book is already borrowed, do nothing;
# - return_book() returns the book;
# - if the book is already returned, do nothing.
#
# Also add:
# get_status()
# which returns either 'available' or 'borrowed'.
#
# Bonus: add a borrow_count attribute that tracks how many times the book has been borrowed.

print('-' * 10, 'Task 16:', sep = '\n')


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrow_count = 0

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrow_count += 1

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

    def get_status(self):
        if not self.is_borrowed:
            return f'Book \'{self.title}\' is available.'

        return f'Book \'{self.title}\' is borrowed.'


book = Book('The Witcher: The Last Wish', 'Andrzej Sapkowski')

book.borrow()

print(book.get_status())

# Task 17: Player Score
#
# Description:
# Create a Player class that stores a player's results.
# The class should have name, score, and games attributes. Initially, score and games should be 0.
# Implement add_game(points), reset_score(), and average_score().
#
# Requirements:
# - add_game(points) adds points to the total score and increases the number of games by 1;
# - if points < 0, do nothing;
# - reset_score() resets both score and games;
# - average_score() returns the average score per game;
# - if no games have been played, return 0.
#
# Bonus: add a best_game(points) method and determine what additional
# state the object needs to remember the best result.

print('-' * 10, 'Task 17:', sep = '\n')


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.max_score = 0
        self.games = 0

    def add_game(self, points):
        if points < 0:
            return

        self.score += points
        self.games += 1

        if points > self.max_score:
            self.max_score = points

    def reset_score(self):
        self.score = 0
        self.games = 0
        self.max_score = 0

    def average_score(self):
        if self.games == 0:
            return 0

        return self.score / self.games

    def show_result(self):
        return (f'name: {self.name}\n'
                f'number of games: {self.games}\n'
                f'score: {self.score}\n'
                f'max score: {self.max_score}')


player_1 = Player('Alex')

player_1.add_game(5)
player_1.add_game(10)
player_1.add_game(7)

print(player_1.show_result())

# Task 18: Fuel Tank
#
# Description:
# Create a FuelTank class that represents a car's fuel tank.
#
# The class should have capacity and fuel attributes. Initially, fuel should be 0.
# Implement fill(amount), use(amount), and get_percentage().
#
# Requirements:
# - fill(amount) adds fuel;
# - fuel cannot exceed capacity;
# - if too much fuel is added, fill the tank to its maximum capacity;
# - use(amount) consumes fuel;
# - if there is not enough fuel, do nothing;
# - if amount <= 0, fill() and use() should do nothing;
# - get_percentage() returns the current fuel level as a percentage.
#
# Bonus: add a total_used attribute that tracks the total amount of successfully consumed fuel.

print('-' * 10, 'Task 18:', sep = '\n')


class FuelTank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.fuel = 0
        self.total_used = 0

    def fill(self, amount):
        if amount > 0:
            if self.fuel + amount < self.capacity:
                self.fuel += amount
            else:
                self.fuel = self.capacity

    def use(self, amount):
        if amount > 0:
            if self.fuel - amount >= 0:
                self.fuel -= amount
                self.total_used += amount
            else:
                return

    def get_percentage(self):
        return self.fuel * 100 / self.capacity


tank = FuelTank(50)

tank.fill(30)
tank.use(10)

print(f'Current fuel level: {tank.fuel}')
print(f'Current fuel level as a percentage: {tank.get_percentage()} %')

# Task 19: Inventory Item
#
# Description:
# Create an InventoryItem class that represents an item in stock.
# The class should store name, price, and quantity.
# Implement add_stock(amount), sell(amount), and get_total_value().
#
# Requirements:
# - add_stock(amount) increases the quantity;
# - if amount <= 0, do nothing;
# - sell(amount) decreases the quantity;
# - an item cannot be sold if there is not enough stock;
# - an unsuccessful sale should not change the object;
# - get_total_value() returns price * quantity.
#
# Bonus: add a total_sold attribute that tracks the total number of successfully sold units.

print('-' * 10, 'Task 19:', sep = '\n')


class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_sold = 0

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount

    def sell(self, amount):
        if amount > 0 and amount <= self.quantity:
            self.quantity -= amount
            self.total_sold += amount

    def get_total_value(self):
        return self.price * self.quantity


item = InventoryItem('Keyboard', 50, 10)

item.add_stock(3)
item.sell(7)

print('The total value of the remaining goods:', item.get_total_value())

# Task 20: Shopping Wallet
#
# Description:
# Create a Wallet class that represents an electronic wallet.
# The class should store the owner's name and current balance.
# Implement deposit(amount), withdraw(amount), and transfer(other_wallet, amount).
#
# Requirements:
# - deposit(amount) adds money to the balance;
# - if amount <= 0, do nothing;
# - withdraw(amount) removes money from the balance;
# - do not allow the balance to become negative;
# - withdrawing the entire balance is allowed;
# - transfer(other_wallet, amount) transfers money from the current wallet to another wallet;
# - a transfer is successful only if the amount is positive and there is enough money;
# - an unsuccessful transfer must not change either wallet.
#
# Bonus: add a transaction_count attribute that tracks
# the number of successful operations for each wallet.

print('-' * 10, 'Task 20:', sep = '\n')


class Wallet:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_count = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1

    def transfer(self, other_wallet, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_wallet.balance += amount

            self.transaction_count += 1
            other_wallet.transaction_count += 1


wallet_1 = Wallet('Alex', 100)
wallet_2 = Wallet('John', 50)

wallet_1.transfer(wallet_2, 30)

print(f'{wallet_1.name} balance: {wallet_1.balance}')
print(f'{wallet_2.name} balance: {wallet_2.balance}')

# Task 21: Parking Lot
#
# Description:
# Create a ParkingLot class that represents a small parking lot.
#
# The class should store its capacity and a list of currently parked cars.
#
# Implement park(car_number), leave(car_number), and free_spaces().
#
# Requirements:
# - park(car_number) adds a car to the parking lot;
# - do not allow more cars than the parking capacity;
# - the same car number cannot be parked twice;
# - leave(car_number) removes the specified car;
# - if the car is not parked, do nothing;
# - free_spaces() returns the number of available parking spaces.
#
# Bonus: add a total_parked attribute that tracks the total number of successful parking operations.

print('-' * 10, 'Task 21:', sep = '\n')


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []
        self.total_parked = 0

    def park(self, car_number):
        if self.capacity > len(self.cars) and car_number not in self.cars:
            self.cars.append(car_number)
            self.total_parked += 1

    def leave(self, car_number):
        if car_number in self.cars:
            self.cars.remove(car_number)

    def free_spaces(self):
        return self.capacity - len(self.cars)


parking = ParkingLot(3)

parking.park('AA1234BB')
parking.park('BC5678CD')

print('Free spaces:', parking.free_spaces())

parking.leave('AA1234BB')

print('Free spaces:', parking.free_spaces())

# Task 22: Course Progress
#
# Description:
# Create a Course class that tracks a student's progress through a course.
#
# The class should store name, total_lessons, and completed_lessons.
# Initially, completed_lessons should be 0.
# Implement complete_lesson(), reset_progress(), and get_progress().
#
# Requirements: complete_lesson() increases the number of completed lessons
# by one but cannot exceed total_lessons; reset_progress() resets the progress to zero;
# get_progress() returns the completion percentage.
#
# Bonus: add a complete_multiple(amount) method that completes several lessons at once.
# Ignore non-positive values and never allow completed_lessons to exceed total_lessons.

print('-' * 10, 'Task 22:', sep = '\n')


class Course:
    def __init__(self, name, total_lessons):
        self.name = name
        self.total_lessons = total_lessons
        self.completed_lessons = 0

    def complete_lesson(self):
        if self.completed_lessons < self.total_lessons:
            self.completed_lessons += 1

    def reset_progress(self):
        self.completed_lessons = 0

    def get_progress(self):
        return self.completed_lessons * 100 / self.total_lessons

    def complete_multiple(self, amount):
        if amount > 0:
            if self.completed_lessons + amount <= self.total_lessons:
                self.completed_lessons += amount
            else:
                self.completed_lessons = self.total_lessons


course = Course('Python Basics', 5)

course.complete_lesson()
course.complete_lesson()
course.complete_multiple(3)

print('Completed lessons:', course.completed_lessons)
print(f'Completion percentage: {course.get_progress()}%')

# Task 23: Battery
#
# Description:
# Create a Battery class that represents a device battery.
# The battery should initially be fully charged.
#
# Implement use(amount), charge_battery(amount), and get_percentage().
#
# Requirements:
# - use(amount) decreases the current charge;
# - ignore non-positive amounts;
# - do not allow the charge to become negative;
# - using the entire remaining charge is allowed;
# - charge_battery(amount) increases the charge;
# - the charge cannot exceed the battery capacity;
# - get_percentage() returns the current charge level as a percentage.
#
# Bonus: add a total_used attribute that tracks the total amount of successfully used charge.

print('-' * 10, 'Task 23:', sep = '\n')


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
        self.charge = self.capacity
        self.total_used = 0

    def use(self, amount):
        if amount > 0:
            if self.charge - amount >= 0:
                self.charge -= amount
                self.total_used += amount

    def charge_battery(self, amount):
        if amount > 0:
            if self.charge + amount <= self.capacity:
                self.charge += amount
            else:
                self.charge = self.capacity

    def get_percentage(self):
        return self.charge * 100 / self.capacity


battery = Battery(100)

battery.use(30)
battery.charge_battery(10)

print(f'Battery level: {battery.get_percentage()}%')

# Task 24: Elevator
#
# Description:
# Create an Elevator class that represents an elevator in a building.
# The elevator starts on floor 1.
#
# Implement move_to(floor). A valid floor must be between 1 and max_floor.
# Invalid moves and moves to the current floor should do nothing.
#
# The total_moves attribute must track the total number of floors traveled,
# not the number of method calls.
# Also implement get_current_floor() to return the current floor.
#
# Bonus: add return_to_first_floor(), which returns the elevator to floor 1 and
# correctly updates total_moves.

print('-' * 10, 'Task 24:', sep = '\n')


class Elevator:
    def __init__(self, max_floor):
        self.max_floor = max_floor
        self.current_floor = 1
        self.total_moves = 0

    def move_to(self, floor):
        if self.max_floor >= floor > 0 and floor != self.current_floor:
            self.total_moves += abs(floor - self.current_floor)
            self.current_floor = floor

    def return_to_first_floor(self):
        if self.current_floor != 1:
            self.total_moves += abs(1 - self.current_floor)
            self.current_floor = 1

    def get_current_floor(self):
        return self.current_floor


elevator = Elevator(10)

elevator.move_to(5)
elevator.move_to(2)

print('Current floor:', elevator.get_current_floor())
print('Total floors covered:', elevator.total_moves)
