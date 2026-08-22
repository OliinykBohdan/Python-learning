# Task 1
#
# Create a Dog class that:
#
# has the following attributes: name, age
#
# has a method called bark(), which prints:
#
# Woof! My name is <name>

print('-' * 10, 'Task 1:', sep = '\n')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'Woof! My name is {self.name}')


animal = Dog('Rex', 1)

animal.bark()

# Task 2
#
# Make a small change right now:
#
# Task:
# Add the info() method
# It should output:
# Dog: Rex, age: 1

print('-' * 10, 'Task 2:', sep = '\n')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Dog: {self.name}, age: {self.age}')


dog = Dog('Rex', 2)

dog.info()

# Task 3
#
# Create 3 dogs with different details:
#
# Rex, 2 years old
# Bobby, 5 years old
# Luna, 1 year old
#
# And call info() for each one.

print('-' * 10, 'Task 3:', sep = '\n')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name}, {self.age} years old')


dog1 = Dog('Rex', 2)
dog2 = Dog('Bobby', 5)
dog3 = Dog('Luna', 1)

dog1.info()
dog2.info()
dog3.info()

# Task 4
#
# Modify the class so that:
#
# the `age` variable cannot be modified directly
# create a method:
# `set_age(new_age)`
# And implement the following check:
# if `new_age` < 0 → display ‘Invalid age’
# and do not change the value

print('-' * 10, 'Task 4:', sep = '\n')


class Dog:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            print('Invalid age')
        else:
            self.__age = age

    def set_age (self, new_age):
        if new_age < 0:
            print('Invalid age')
        else:
            self.__age = new_age

    def info(self):
        print(f'{self.name}, {self.__age} years old')


dog1 = Dog('Rex', 2)
dog2 = Dog('Bobby', 5)
dog3 = Dog('Luna', 1)

dog1.set_age(19)

dog1.info()
dog2.info()
dog3.info()

# Task 5:
# Create a base class:
# class Animal:
#
# with a method:
#
# make_sound()
# Create:
# class Dog(Animal)
# class Cat(Animal)
# Implement:
# Dog → 'Woof'
# Cat → 'Meow'
# Create a list:
# animals
#
# and call:
#
# loop for

print('-' * 10, 'Task 5:', sep = '\n')


class Animal:
    def make_sound(self):
        print('Some sound')


class Dog(Animal):
    def make_sound(self):
        print('Woof')


class Cat(Animal):
    def make_sound(self):
        print('Meow')


animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()

# Task 6
#
# Add:
#
# In 'Animal':
# def __init__(self, name):
#     self.name = name
# Use this name in 'Dog' and 'Cat'
# Modify 'make_sound()':
# print(f'{self.name}: Woof')
# Create:
# animals = [Dog('Rex'), Cat('Milo')]

print('-' * 10, 'Task 6:', sep = '\n')


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Some sound')


class Dog(Animal):
    def make_sound(self):
        print(f'{self.name}: Woof')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.name}: Meow')


animals = [Dog('Rex'), Cat('Milo')]

for animal in animals:
    animal.make_sound()

# Task 7: Employee System
#
# Imagine you are building a system for a company.
#
# 1. Base class
#
# Create a class:
#
# Employee
# It must have:
# name
#
# Basic behaviour:
#
# calculate_salary()
#
# 2. Inheritance
#
# Create several types of employees:
#
# FullTimeEmployee
# PartTimeEmployee
# Freelancer
#
# 3. Salary logic (different for each)
# FullTimeEmployee:
# has a fixed monthly salary
# PartTimeEmployee:
# has an hourly rate
# and the number of hours worked
# Freelancer:
# is paid per project
# and the number of projects completed
# 4. Encapsulation (MANDATORY)
# make at least one variable ‘protected’
# add method(s) to modify data with validations
# (for example: negative hours / salary / projects cannot be set)
#
# 5. Polymorphism
#
# Create a list:
#
# employees = [...]
#
# with different types of employees
#
# And write a loop:
#
# for emp in employees:
#     print(emp.calculate_salary())

print('-' * 10, 'Task 7:', sep = '\n')


class Employee:

    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError('Subclass must implement this method')


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return f'Employee {self.name}, salary: {3000}'


class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked):
        super().__init__(name)
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return f'Employee {self.name}, salary: {self.__hours_worked * 20}'

    def set_hours_worked(self, time):
        if time < 0:
            print('Enter positive integer')
        else:
            self.__hours_worked = time


class Freelancer(Employee):
    def __init__(self, name, number_project):
        super().__init__(name)
        self.number_project = number_project

    def calculate_salary(self):
        return f'Employee {self.name }, salary: {500 * self.number_project}'


employees = [FullTimeEmployee('John'), PartTimeEmployee('Will', 130), Freelancer('Martin', 3)]

for employee in employees:
    print(employee.calculate_salary())

# Task 8: Payment System
# Requirements
#
# Create a system for processing payments.
#
# 1. Abstract Class
#
# Create a base class:
#
# PaymentMethod
#
# It must:
#
# contain the method:
#
# pay(amount)
# this method must NOT have any implementations
# 2. Implementations
#
# Create the following classes:
#
# CreditCard
# PayPal
# CryptoWallet
# 3. Logic
#
# Each class must implement pay(amount) in its own way:
#
# CreditCard → ‘Paid {amount} using Credit Card’
# PayPal → ‘Paid {amount} using PayPal’
# CryptoWallet → ‘Paid {amount} using Crypto’
# 4. Polymorphism
#
# Create a list:
#
# payments = [...]
#
# And call:
#
# for payment in payments:
#     payment.pay(100)
# 5. Additional (important)
# You cannot create a PaymentMethod object
# Use Python’s abstraction mechanism

print('-' * 10, 'Task 8:', sep = '\n')

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f'Paid {amount} using Credit Card')

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f'Paid {amount} using PayPal')

class CryptoWallet(PaymentMethod):
    def pay(self, amount):
        print(f'Paid {amount} using Crypto')


payments = [CreditCard(), PayPal(), CryptoWallet()]

for payment in payments:
    payment.pay(100)

# Task 9: Geometric Shapes
# Problem Statement
#
# Create a system for working with shapes.
#
# 1. Abstract class
# Shape
#
# Methods:
#
# area()
# perimeter()
#
# without implementation
#
# 2. Implementations
#
# Create the following classes:
#
# Rectangle
# Circle
# Triangle
# 3. Logic
#
# Each class must:
#
# accept the necessary parameters (sides, radius, etc.)
# implement:
# area()
# perimeter()
# 4. Polymorphism
# shapes = [...]
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())
# 5. Condition
# do not use if type(...)
# each class is responsible for its own logic

print('-' * 10, 'Task 9:', sep = '\n')

import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        if a < 1 or b < 1:
            raise ValueError('Sides must be positive')

        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b


class Circle(Shape):
    def __init__(self, r):
        if r < 1:
            raise ValueError('Radius must be positive')

        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return math.pi * self.r * 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a < 1 or b < 1 or c < 1:
            raise ValueError('Sides must be positive')

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle")

        self.a = a
        self.b = b
        self.c = c

    def _semi_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def area(self):
        p = self._semi_perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Rectangle(7, 10), Circle(7), Triangle(8, 7, 6)]

for shape in shapes:
    print(f'{shape.__class__.__name__} area: {shape.area()}')
    print(f'{shape.__class__.__name__} perimeter: {shape.perimeter()}')
