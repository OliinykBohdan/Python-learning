# Task 1

print('-' * 10, 'Task 1:', sep='\n')

def say_name(name):
    def say_hello():
        print(f'Hello {name}!')
    return say_hello

f = say_name('Bohdan')
f()

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

def strip_spring (strip_chars = ' '):
    def do_strip (striping):
        return striping.strip(strip_chars)
    return do_strip

strip1 = strip_spring()
strip2 = strip_spring(' !?,.')

print(strip1('Hello ,. ! '))
print(strip2('Hello ,. ! '))