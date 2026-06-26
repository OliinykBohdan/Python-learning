# Description:
#
# Create 2 functions:
#
# Function 1: get_even_numbers
#
# Create a function that:
#
# takes a list of numbers
# returns a new list with only even numbers
# Function 2: sum_list
#
# Create a function that:
#
# takes a list
# returns the sum of all elements
#  Main Goal
#
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# You need to:
#
# get even numbers
# pass them to the second function
# print the result
# Requirements:
# do NOT use print inside functions
# use return
# split logic into 2 functions
# Expected output:
# 12

numbers_list = [1, 2, 3, 4, 5, 6]


def even_numbers(numbers):
    even_number_list = []
    for i in numbers:
        if i % 2 == 0:
            even_number_list.append(i)
    return even_number_list


def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


print(sum_numbers(even_numbers(numbers_list)))