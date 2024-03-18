"""Assignment: Pyramid
Created on 11 june 2021
Author: Jelmer Haverkate"""

# This program calculates the number of different pizza's Mario and Luigi can make and compares the numbers.

MARIO_INGREDIENTS_TOTAL = 10
MARIO_INGREDIENTS_PER_PIZZA = 3
LUIGI_INGREDIENTS_TOTAL = 9
LUIGI_INGREDIENTS_PER_PIZZA = 4


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def binomial_coefficient(n, k):
    result = (factorial(n))/(factorial(k)*factorial(n - k))
    return int(result)


mario_number_of_different_pizzas = binomial_coefficient(MARIO_INGREDIENTS_TOTAL, MARIO_INGREDIENTS_PER_PIZZA)
luigi_number_of_different_pizzas = binomial_coefficient(LUIGI_INGREDIENTS_TOTAL, LUIGI_INGREDIENTS_PER_PIZZA)

if mario_number_of_different_pizzas > luigi_number_of_different_pizzas:
    winner = "Mario"
else:
    winner = "Luigi"

print("Mario can make %d pizzas." % mario_number_of_different_pizzas)
print("Luigi can make %d pizzas." % luigi_number_of_different_pizzas)
print("%s has won the bet." % winner)
