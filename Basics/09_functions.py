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

exchangers = (['53443', 0.91], ['73443', 0.9], ['90443', 0.9],
              ['53423', 0.92], ['53219', 0.91], ['74055', 0.91])

exchange_rate = 0.89


def percent_of(value, part, /, numeric=True):
    if value <= 0 or part < 0:
        return False

    precent = part / value * 100

    if numeric:
        return round(precent, 2)
    return str(round(precent, 2)) + ' %'


percent_list = []

for exchanger in exchangers:
    precent = percent_of(exchange_rate, exchanger[1])
    percent_list.append(precent)
    exchanger.append(precent)

print('Result:', percent_list)
print(exchangers)
