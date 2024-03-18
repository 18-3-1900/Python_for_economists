"""Assignment: Manny
Created on 7 june 2021
Author: Jelmer Haverkate"""

# This program reads the amount someone wants to donate from input
# and asks again until the amount is over 50 euro. After that it prints a thank you message.

MINIMUM_AMOUNT_REQUESTED = 50.00

amount_donated = (float(input("Enter the amount you want to donate:\n")))

while amount_donated < MINIMUM_AMOUNT_REQUESTED:
    amount_donated = (float(input("Enter the amount you want to donate:\n")))

print("Thank you very much for your contribution of %.2f euro." % amount_donated)
