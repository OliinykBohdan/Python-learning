import subprocess
import sys

# Task 1: Process Communication
#
# Description:
# Create two files:
# main.py
# worker.py
#
# worker.py:
# - receive two numbers through stdin;
# - convert them to numbers;
# - calculate their sum;
# - send the result through stdout.
#
# main.py:
# - start worker.py using subprocess;
# - send two numbers to it through stdin;
# - receive the result through stdout;
# - convert the received value to a number;
# - multiply it by 2;
# - print the final result.
#
# Example:
# main.py sends: 5 and 7
# worker.py calculates: 5 + 7 = 12
# main.py receives 12 and prints:
# 24
#
# Conditions:
# - use subprocess;
# - pass the numbers through stdin;
# - receive the result through stdout;
# - worker.py and main.py must not import each other.

print('-' * 10, 'Task 1:', sep='\n')

result = subprocess.run(
    [sys.executable, 'worker.py'],
    input='5 7',
    capture_output=True,
    text=True
)

print('Result:', int(result.stdout) * 2)
