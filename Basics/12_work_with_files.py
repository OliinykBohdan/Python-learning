import os

BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, 'work_with_files_(test)')

test_1_file = os.path.join(FILES_DIR, 'test_1.txt')
test_2_file = os.path.join(FILES_DIR, 'test_2.txt')

# Task 1

print('-' * 10, 'Task 1:', sep = '\n')

with open(test_1_file, 'r') as file:
    data = file.read()

print(data)

# Task 2

print('-' * 10, 'Task 2:', sep = '\n')

file = open(test_2_file, 'a')
hobby = input('Hobby: ')
file.write(hobby + '\n')
file.close()

# Task 3

print('-' * 10, 'Task 3:', sep = '\n')

file_2 = open('12_work_with_files.py', encoding='utf-8')

text = file_2.read()

print(file_2)
print(text)
