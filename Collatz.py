"""Assignment: Collatz
Created on 7 june 2021
Author: Jelmer Haverkate"""

# This program takes an positive integer from input
# and prints the corresponding Collatz sequence

n = int(input("Enter a positive integer: "))

print("%d" % n)

while n > 1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n/2
    print("%d" % n)
