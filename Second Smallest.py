"""Assignment: Second Smallest
Created on 7 june 2021
Author: Jelmer Haverkate"""

# This program takes a number of positive integers from input
# and prints the second smallest integer.

numbers = input()
numbers = numbers.split()

lowest_number = int(numbers[0])
second_lowest_number = int(numbers[1])

for number in numbers:
    number = int(number)
    if number < lowest_number:
        second_lowest_number = lowest_number
        lowest_number = number
    elif number < second_lowest_number:
        second_lowest_number = number

print("The second smallest number is:%d" % second_lowest_number)
