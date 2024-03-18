"""Assignment: Palindrome 1
Created on 9 june 2021
Author: Jelmer Haverkate"""

# This program prints the palindrome of the alphabet.


def palindrome():
    output = ""
    for i in range(ord("a"), ord("z")):
        c = chr(i)
        output += c
    for j in range(ord("z"), ord("a") - 1, -1):
        d = chr(j)
        output += d
    print(output)


palindrome()
