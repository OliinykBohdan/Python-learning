# Task 1: Method Overriding (Basic)
#
# Description:
#
# Create a base class Animal
#
# Task:
#
# method speak() → prints 'Some sound'
#
# Create:
#
# Dog → 'Woof'
# Cat → 'Meow'
#
# Create objects and call speak()

print('-' * 10, 'Task 1:', sep = '\n')

class Animal:
    def speak(self):
        print('Some sound')

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

pet1 = Dog()
pet2 = Cat()

pet1.speak()
pet2.speak()

# Task 2: Same Method – Different Behavior
#
# Description:
#
# Polymorphism = same method, different behaviour
#
# Task:
#
# Create class Shape
#
# method area()
#
# Create:
#
# Rectangle → width, height
# Circle → radius
#
# Each class must implement its own area()
#
# Print areas

print('-' * 10, 'Task 2:', sep = '\n')

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

figure1 = Rectangle(5, 8)
figure2 = Circle(8)

print(figure1.area())
print(figure2.area())

# Task 3: Loop Polymorphism
#
# Description:
#
# Use polymorphism in loop
#
# Task:
#
# Create:
#
# Dog → speak()
# Cat → speak()
# Cow → speak()
#
# Store objects in list
#
# Loop and call speak()

print('-' * 10, 'Task 3:', sep = '\n')

class Animal:
    def speak(self):
        print('Some sound')

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Cow(Animal):
    def speak(self):
        print('Myy')

creatures = [Dog(), Cat(), Cow()]

for creature in creatures:
    creature.speak()

# Task 4: Function Polymorphism
#
# Description:
#
# Function works with different objects
#
# Task:
#
# Create function:
#
# def make_sound(animal):
#     animal.speak()
#
# Pass:
#
# Dog
# Cat

print('-' * 10, 'Task 4:', sep = '\n')

class Dog:
    def speak(self):
        print('Woof')

class Cat:
    def speak(self):
        print('Meow')

def make_sound(animal):
    animal.speak()

creature1 = Dog()
creature2 = Cat()

make_sound(creature1)
make_sound(creature2)

# Task 5: Without Inheritance (Duck Typing)
#
# Description:
#
# Polymorphism without inheritance
#
# Task:
#
# Create:
#
# class Car → method move()
# class Bird → method move()
#
# Car → 'Driving'
# Bird → 'Flying'
#
# Call both using a single function

print('-' * 10, 'Task 5:', sep = '\n')

class Car:
    def move(self):
        print('Driving')

class Bird:
    def move(self):
        print('Flying')

def movement(unit):
    unit.move()

car = Car()
bird = Bird()

movement(car)
movement(bird)

# Task 6: Override + super()
#
# Description:
#
# Extend parent behavior
#
# Task:
#
# Base class Employee:
#
# method work() → 'Working'
#
# Child class Developer:
#
# override work()
# call parent method
# add: 'Writing code'

print('-' * 10, 'Task 6:', sep = '\n')

class Employee:
    def work(self):
        print('Working')

class Developer(Employee):
    def work(self):
        super().work()
        print('Writing code')

person = Developer()

person.work()

# Task 7: Real-life Polymorphism
#
# Description:
#
# Payment system
#
# Task:
#
# Create base class Payment:
#
# method pay()
#
# Create:
#
# CardPayment → 'Paid with card'
# CashPayment → 'Paid with cash'
#
# Function:
#
# def process_payment(payment):
#     payment.pay()

print('-' * 10, 'Task 7:', sep = '\n')

class Payment:
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        print('Paid with card')

class CashPayment(Payment):
    def pay(self):
        print('Paid with cash')

def process_payment(payment):
    payment.pay()

process_payment(CardPayment())
process_payment(CashPayment())

# Task 8: Return Values
#
# Description:
#
# Polymorphism with return
#
# Task:
#
# Create:
#
# Dog → speak() returns 'Woof'
# Cat → returns 'Meow'
#
# Store in list
#
# Return all sounds as list:
#
# ['Woof', 'Meow']

print('-' * 10, 'Task 8:', sep = '\n')

class Animal:
    def speak(self):
        return 'Some sound'

class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'

animals = [Dog(), Cat()]

sounds = [animal.speak() for animal in animals]

print(sounds)

# Task 9: Mini Challenge
#
# Description:
#
# Mix everything
#
# Task:
#
# Create:
#
# class Animal
# subclasses: Dog, Cat, Bird
#
# Each has:
#
# speak()
# move()
#
# Dog → run
# Bird → fly
# Cat → walk
#
# Loop:
#
# animals = [...]
#
# Print:
#
# Woof - run
# Meow - walk
# Tweet - fly

print('-' * 10, 'Task 9:', sep = '\n')

class Animal:
    def speak(self):
        return 'Some sound'

    def move(self):
        return 'Some move'

class Dog(Animal):
    def speak(self):
        return 'Woof'

    def move(self):
        return 'run'

class Cat(Animal):
    def speak(self):
        return 'Meow'

    def move(self):
        return 'walk'

class Bird(Animal):
    def speak(self):
        return 'Tweet'

    def move(self):
        return 'fly'

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(f'{animal.speak()} - {animal.move()}')
