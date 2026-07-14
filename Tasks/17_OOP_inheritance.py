# Task 1: Basic Inheritance
#
# Description:
#
# Create a base class Animal
#
# Task:
#
# attribute: name
# method: speak() → prints 'Some sound'
#
# Create a child class Dog(Animal)
#
# create object
# call speak()

print('-' * 10, 'Task 1:', sep = '\n')


class Animal:
    name = 'Rex'

    def speak(self):
        print('Some sound', self.name)


class Dog(Animal):
    pass


pet = Dog()
pet.speak()

# Task 2: Override Constructor
#
# Description:
#
# In class Animal:
#
# __init__(self, name)
#
# In class Cat(Animal):
#
# add attribute color
# use super()
#
# Create object:
#
# name = 'Tom'
# color = 'gray'
#
# Print both values

print('-' * 10, 'Task 2:', sep = '\n')


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Name:', self.name)


class Cat(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        super().speak()
        print('Color:', self.color)


pet1 = Cat('Tom', 'gray')
pet1.speak()

# Task 3: Add New Method in Child
#
# Description:
#
# Base class Vehicle:
#
# attribute: brand
#
# Child class Car(Vehicle):
#
# add method drive()
# print 'Car is driving'
#
# Create object and call both:
#
# access brand
# call drive()

print('-' * 10, 'Task 3:', sep = '\n')


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):

    def drive(self):
        print('Car is driving', self.brand)


c = Car('Audi')
print(c.brand)
c.drive()

# Task 4: Reuse Parent Method
#
# Description:
#
# Base class Person:
#
# method greet() → 'Hello'
#
# Child class Student(Person):
#
# attribute: name
#
# Create object:
#
# call greet()
# print name

print('-' * 10, 'Task 4:', sep = '\n')


class Person:
    def greet(self):
        print('Hello')


class Student(Person):
    def __init__(self, name):
        self.name = name


p = Student('Bohdan')
p.greet()
print(p.name)

# Task 5: super() Practice
#
# Description:
#
# Base class Employee:
#
# __init__(self, name, salary)
#
# Child class Manager(Employee):
#
# add bonus
# use super()
#
# Create object and print:
#
# name
# salary
# bonus

print('-' * 10, 'Task 5:', sep = '\n')


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        print('Name:', self.name, 'Salary:', self.salary)


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_info(self):
        super().get_info()
        print('Bonus:', self.bonus)


person = Manager('Bohdan', 2000, 500)
person.get_info()

# Task 6: Multi-level Inheritance
#
# Description:
#
# Create:
#
# Animal → Mammal → Dog
#
# Animal → name
# Mammal → add has_fur = True
# Dog → method bark() → 'Woof!'
#
# Create object and print:
#
# name
# has_fur
# call bark()

print('-' * 10, 'Task 6:', sep = '\n')


class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_fur = True


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print('Woof!')


d = Dog('Rex')

print('Name:', d.name)
print('Has fur:', d.has_fur)
d.bark()

# Task 7: Inheritance with super()
#
# Use inheritance to create a Rectangle3D class based on the Rectangle2D class,
# whose instances will have a third parameter: height.
#
# What needs to be implemented:
# 1) The Rectangle3D class inherits from Rectangle2D.
# 2) When instances of Rectangle3D are created, three arguments are passed to them immediately:
# Rectangle3D(length, width, height).
# 3) Use super() in the overridden __init__ method to reuse the __init__ code from the parent class.
# 4) Consider how to handle the different numbers of parameters in the two __init__ methods.
# 5) Define a volume method that returns the volume (length × width × height) for Rectangle3D instances.

print('-' * 10, 'Task 7:', sep = '\n')


class Rectangle2D:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Rectangle3D(Rectangle2D):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return super().area() * self.height


rec2D = Rectangle2D(2, 3)
rec3D = Rectangle3D(2, 3, 4)

print('Area of a rectangle 2D:', rec2D.area())
print('Volume of a rectangle 3D:', rec3D.volume())
