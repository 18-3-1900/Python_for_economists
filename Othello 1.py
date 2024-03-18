"""Assignment: Othello 1
Created on 3 june 2021
Author: Jelmer Haverkate"""

# This program reads the number of black and white pieces on a Othello board from input
# and prints the percentage of black pieces of total pieces & the percentage of the board covered by black pieces.

TOTAL_NUMBER_OF_SQUARES = 64

number_of_white_pieces = int(input("Enter the number of white pieces on the board: "))

number_of_black_pieces = int(input("Enter the number of black pieces on the board: "))

total_number_of_pieces = number_of_white_pieces + number_of_black_pieces

percent_board_covered_by_black_pieces = float((number_of_black_pieces/TOTAL_NUMBER_OF_SQUARES)*100)

percent_black_pieces_of_all_pieces = float((number_of_black_pieces/total_number_of_pieces)*100)

print("The percentage of black pieces on the board is: %.2f%%" % percent_board_covered_by_black_pieces)

print("The percentage of black pieces of all the pieces on the board is: %.2f%%" % percent_black_pieces_of_all_pieces)
