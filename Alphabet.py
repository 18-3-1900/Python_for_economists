"""Assignment: Alphabet
Created on 5 june 2021
Author: Jelmer Haverkate"""

# This program prints the alphabet on a single line

output = ""

for i in range(ord("a"), ord("z") + 1):
    c = chr(i)
    output = output + c

print(output)
