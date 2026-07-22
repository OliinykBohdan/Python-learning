# Task 1

def decorator (func):
    def inner ():
        print('start')
        func()
        print('end')
    return inner


@decorator
def say_name1 ():
    print('Bohdan')


@decorator
def say_name2 ():
    print('Vika')


say_name1()

say_name2()

# Task 2

def decorator_1(func):
    def inner():
        print(10 * '~')
        func()
        print(10 * '~')
    return inner


def decorator_2(func):
    def inner():
        print(10 * '#')
        func()
        print(10 * '#')
    return inner


@decorator_2
@decorator_1
def func_1():
    print('Main content')


func_1()

# Task 3

def decorator_maker():
    def decorator_3(func):
        def inner(*args, **kwargs):
            print(10 * '$')
            func(*args, **kwargs)
            print(10 * '$')
        return inner
    return decorator_3


@decorator_maker()
def func_1(name):
    print(f'Main content {name}')


func_1('123')

# Task 4

def repeat(num = 3):
    def decorator_3(func):
        def inner(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return inner
    return decorator_3


@repeat(5)
def func_1(name):
    print(f'Main content {name}')


@repeat()
def func_2(name):
    print(f'Main content {name}')


func_1('123')
func_2('54754')
