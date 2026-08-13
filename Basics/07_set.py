# Methods covered: add(), remove(), intersection(), symmetric_difference(), difference()

numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers2 = {4, 3433, 23, 32, 1, 34, 8, 6, 2, 3}

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