# Task 1

print('-' * 10, 'Task 1:', sep='\n')

def calculate_p(x, y):
    print('-' * 10)
    print(f'Perimeter: {2 * (x + y)}')
    print(f'Area: {x * y}')

calculate_p(10, 5)
calculate_p(15, 7)
calculate_p(11, 8)

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

def multiply(x = 1, y = 1):
    print(x * y)

multiply(10, 5)
multiply(15)
multiply()

print('Result: done')

# Task 3

print('-' * 10, 'Task 3:', sep='\n')

raw_url = 'example.com'

def func(url):
    if 'www' not in url:
        url = 'https://www.' + url

    elif 'https://' not in url:
        url = 'https://' + url

    return url

print('Result:', func(raw_url))

# Task 4

print('-' * 10, 'Task 4:', sep='\n')

def percent_of(value, part, /):
    if value <= 0 or part < 0:
        return False

    precent = part / value * 100
    return str(round(precent, 2)) + ' %'

result = percent_of(100,20)

print('Result:', result)
