"""Assignment: Plumber
Created on 3 june 2021
Author: Jelmer Haverkate"""

# This program reads the number of hours worked from input
# and prints the cost of a repair.

CALL_OUT_COSTS = 16.00

hourly_wage = float(input("Enter the hourly wages: "))

billable_hours = int(float(input("Enter the number of hours worked: "))+0.5)

repair_costs = hourly_wage * billable_hours + CALL_OUT_COSTS

print("The total cost of this repair is: %.2f euro" % repair_costs)
