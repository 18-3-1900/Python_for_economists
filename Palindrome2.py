"""Assignment: Palindrome 2
Created on 9 june 2021
Author: Jelmer Haverkate"""

# This program takes a letter from input
# and prints a palindrome up to this letter.


def palindrome(letter):
    output = ""
    for i in range(ord("a"), ord(letter)):
        c = chr(i)
        output += c
    for j in range(ord(letter), ord("a") - 1, -1):
        d = chr(j)
        output += d
    print(output)


palindrome(input("Enter a letter: "))
