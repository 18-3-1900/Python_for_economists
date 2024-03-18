"""Assignment: VAT
Created on 4 june 2021
Author: Jelmer Haverkate"""

# This program reads prices including VAT from input
# and prints them without VAT.

VAT_PERCENTAGE = 21.00

price_incl_vat = float(input("Enter the price of an article including VAT: "))

price_exl_vat = 1/(1 + VAT_PERCENTAGE/100) * price_incl_vat

print("This article will cost %.2f euro without %.2f%% VAT." % (price_exl_vat, VAT_PERCENTAGE))
