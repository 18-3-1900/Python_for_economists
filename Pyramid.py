"""Assignment: Pyramid
Created on 11 june 2021
Author: Jelmer Haverkate"""

# This program prints a pyramid made of letters.

SCREEN_WIDTH = 80


def palindrome(letter):
    output = ""
    for i in range(ord("a"), ord(letter)):
        c = chr(i)
        output += c
    for j in range(ord(letter), ord("a") - 1, -1):
        d = chr(j)
        output += d
    return output


def pyramid(number_of_levels):
    for i in range(number_of_levels):
        letter = chr(ord("a") + i)
        number_of_spaces = int(((SCREEN_WIDTH - len(palindrome(letter)))/2)) * " "
        print(number_of_spaces + palindrome(letter))


pyramid(15)
