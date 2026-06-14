# Task 1

def calculate_p(x, y):
    print('-' * 10)
    print(f'Perimeter: {2 * (x + y)}')
    print(f'Area: {x * y}')

calculate_p(10, 5)
calculate_p(15, 7)
calculate_p(11, 8)

# Task 2

print('~' * 20)

def multiply(x = 1, y = 1):
    print(x * y)

multiply(10, 5)
multiply(15)
multiply()