# Task 1 Create variables:
# a = 2 (int)
# b = 5.3 (float)
# c = '5' (str)
# Print the type of each variable using type()
# Perform operations:
# a + b
# a - b
# a * b
# a / b
#
# Question:
# What is the result type in each operation?

print('-' * 10, 'Task 1:', sep='\n')

a = 2
b = 5.3
c = '5'

print('Integer: ', type(a), 'Float: ', type(b), 'String: ', type(c), sep='\n')
print('Addition: ', a+b, 'Subtraction: ', a-b, 'Multiplication: ', a*b, 'Division: ', a/b, sep='\n')

# What is the result type in each operation? Float

# Task 2 Convert:
# c (string '5') to a number
# a to float
#
# Perform calculation:
# result = a + int(c)
#
# Question:
# What happens if you do a + c without conversion?

print('-' * 10, 'Task 2:', sep='\n')

Add = float(a) + int(c)

print(Add)

# What happens if you do a + c without conversion? There will be a "TypeError"

# Task 3 Given:
# x = 10
# y = 3
#
# Find:
# regular division /
# floor division //
# remainder %
# power
#
# Explain the difference between:
# / and //
# % and //

print('-' * 10, 'Task 3:', sep='\n')

x = 10
y = 3

print('Division: ', x / y, 'Division to an integer: ', x // y, 'Remainder from division: ', x % y, '', 'Power: ', x ** y, sep='\n')

# Explanation of the difference between:
# / and // - the first is regular division, the second is floor division (rounds down)
# % and // - the first shows the remainder of division, the second shows how many times one number fits into another

# Task 4 Bus station. You need to determine how many buses to dispatch, depending on the number of tickets sold, as well as the number of passengers who could not be accommodated on a fully occupied bus.
#
# Clarification of the task:
# 1) You need to determine the number of fully occupied buses.
# 2) You need to determine the number of remaining passengers (tickets purchased) who could not be accommodated on a full bus.
#
# Technical aspects of the task:
# 1) The number of tickets purchased and the capacity of the buses are known.
# 2) Do not change the names of the initial variables num_tickets and bus_capacity.
# 3) Do not assign new values resulting from calculations to the variables num_tickets and bus_capacity within the program; create new variables for the results.
# 4) However, you may change the initial values of these variables. The values must be positive integers of type int.
# 5) You may use as many variables as you need to solve the problem.
# 6) Output the result using the print function. The first argument is the number of buses; the second, separated by a comma, is the number of remaining passengers.
#
# Example: print(num_bus, num_left_passengers)

print('-' * 10, 'Task 4:', sep='\n')

num_tickets = 237
bus_capacity = 48

num_bus = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print('Number of full buses:', num_bus, '\nRemaining passengers:', num_left_passengers)
