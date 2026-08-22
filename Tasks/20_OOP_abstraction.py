# Task 1: Abstract Class (Basic)
# Description:
#
# Create an abstract base class
#
# Task:
#
# Create class:
#
# from abc import ABC, abstractmethod
# class Animal(ABC):
# Add:
# abstract method speak()
# Create:
# Dog → 'Woof'
# Cat → 'Meow'
# Call:
# animals = [Dog(), Cat()]
#
# Loop and print sounds

print('-' * 10, 'Task 1:', sep = '\n')

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
       pass

class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Task 2: Cannot Instantiate Abstract Class
# Description:
#
# Understand restriction
#
# Task:
#
# Try:
#
# a = Animal()
# Expected:
#
# Error
#
# Question:
#
# Why does this happen?

print('-' * 10, 'Task 2:', sep = '\n')

class Animal(ABC):
    @abstractmethod
    def speak(self):
       pass

try:
    a = Animal()

except TypeError:
    print('TypeError')

# Why does this happen? Because the speak method must be implemented (a subclass containing this method must be created)

# Task 3: Abstract Method with Multiple Methods
# Description:
#
# Multiple required methods
#
# Task:
#
# Create:
#
# class Shape(ABC):
# Methods:
# area()
# perimeter()
# Create:
# Rectangle
# Circle
# Print:
#
# area + perimeter

print('-' * 10, 'Task 3:', sep = '\n')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 3.14 * 2 * self.radius

rectangle = Rectangle(10, 20)
circle = Circle(5)

print('Area rectangle:', rectangle.area())
print('Perimeter rectangle:', rectangle.perimeter())
print('Area circle:', circle.area())
print('Perimeter circle:', circle.perimeter())

# Task 4: Real Example (Payment System)
# Description:
#
# Same idea, real-world
#
# Task:
#
# Create abstract class:
#
# class Payment(ABC):
# Method:
# pay(amount)
# Create:
# CardPayment
# CryptoPayment
# Call:
# payments = [CardPayment(), CryptoPayment()]
#
# Loop and call pay(100)

print('-' * 10, 'Task 4:', sep = '\n')

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        return f'Paid {amount} with card'

class CryptoPayment(Payment):
    def pay(self, amount):
        return f'Paid {amount} with crypto'

payments = [CardPayment(), CryptoPayment()]

for payment in payments:
    print(payment.pay(100))


# Task 5: Partial Implementation
# Description:
#
# Abstract + normal method
#
# Task:
# class Animal(ABC):
# Add:
# abstract speak()
# normal method info() → 'I am an animal'
# Create Dog
#
# Call:
#
# speak()
# info()

print('-' * 10, 'Task 5:', sep='\n')

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def info(self):
        return 'I am an animal'

class Dog(Animal):
    def speak(self):
        return 'Woof'

dog = Dog()

print(dog.speak())
print(dog.info())

# Task 6: Template Method Pattern (Light)
# Description:
#
# One method uses abstract method
#
# Task:
# class Report(ABC):
# Create:
# def generate(self):
#     self.get_data()
#     self.format_data()
#     print('Report ready')
# Abstract methods:
# get_data()
# format_data()
# Create:
# SalesReport
# Call:
# r = SalesReport()
# r.generate()

print('-' * 10, 'Task 6:', sep='\n')

class Report(ABC):
    def generate(self):
        self.get_data()
        self.format_data()
        print('Report ready')

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def format_data(self):
        pass

class SalesReport(Report):
    def get_data(self):
        print('Sales ready')

    def format_data(self):
        print('Data formatting')

r = SalesReport()

r.generate()

# Task 7: Abstract Property (advanced-lite)
# Description:
#
# Not only methods can be abstract
#
# Task:
#
# Create:
#
# class Vehicle(ABC):
# Add:
# abstract property speed
# Create:
# Car → speed = 120
# Print:
# print(car.speed)

print ('-' * 10, 'Task 7:', sep='\n')

class Vehicle(ABC):
    @property
    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self, value):
        self._speed = value

    @property
    def speed(self):
        return self._speed

car = Car(120)

print('Car.speed:', car.speed)
