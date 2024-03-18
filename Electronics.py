"""Assignment: Electronics
Created on 4 june 2021
Author: Jelmer Haverkate"""

# This program reads the prices of 3 products from input
# and prints the discount and final price.

DISCOUNT_PERCENT = 15

price_first_article = float(input("Enter the price of the first article: "))

price_second_article = float(input("Enter the price of the second article: "))

price_third_article = float(input("Enter the price of the third article: "))

if price_first_article > price_second_article and price_first_article > price_third_article:
    most_expensive_article = price_first_article
elif price_second_article > price_third_article:
    most_expensive_article = price_second_article
else:
    most_expensive_article = price_third_article

discount = DISCOUNT_PERCENT/100 * most_expensive_article

final_price = price_first_article + price_second_article + price_third_article - discount

print("Discount: %.2f" % discount)

print("Total: %.2f" % final_price)
