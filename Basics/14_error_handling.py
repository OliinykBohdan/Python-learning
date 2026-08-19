def get1():
    while True:
        try:
            num1 = float(input('Enter a number 1: '))
            break

        except ValueError:
            print('You did not enter a number.')

    return num1


def get_op():
    while True:
        operator = input('Operator: ')

        if operator in '/*+-':
            break

        print('Only /, *, +, -')

    return operator


def get2():
    while True:
        try:
            num2 = float(input('Enter a number 2: '))
            break

        except ValueError:
            print('You did not enter a number.')

    return num2


def main():
    num1 = get1()
    operator = get_op()
    num2 = get2()

    if operator == '/':
        while True:
            try:
                result = num1 / num2
                break

            except ZeroDivisionError:
                print('You can\'t divide by 0.')
                num2 = get2()

    elif operator == '*':
        result = num1 * num2

    elif operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    return round(result, 2)


print('Result:', main())
