# Methods covered:
# add(), remove(), intersection(), symmetric_difference(), difference(), union(),
# issubset(), issuperset()

numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers2 = {4, 3433, 23, 32, 1, 34, 8, 6, 2, 3}
numbers3 = {1, 3, 7}

numbers1.add(11)
numbers2.remove(4)

print('add():', numbers1, sep='\n')
print('remove():', numbers2, sep='\n')

# Elements present in both sets
result = numbers1.intersection(numbers2)
print('intersection():', result, sep='\n')

# Elements unique to each set
result = numbers1.symmetric_difference(numbers2)
print('symmetric_difference():', result, sep='\n')

# Elements only in numbers1
result = numbers1.difference(numbers2)
print('difference():', result, sep='\n')

# Combines sets into one
result = numbers1.union(numbers2)
print('union():', result, sep='\n')

# Checks whether all elements of the set are contained in the other set
result = numbers3.issubset(numbers1)
print('issubset():', result, sep='\n')

# Shows the same thing as issubset(), just the other way around
result = numbers1.issuperset(numbers3)
print('issuperset():', result, sep='\n')
