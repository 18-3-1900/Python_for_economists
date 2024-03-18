"""Assignment: Geography Grades 2
Created on 15 june 2021
Author: Jelmer Haverkate"""

# This program reads the results for three tests from an input file for each student
# and calculates and prints the final grade for each student.


def student_name(line):
    name_results = line.split("_")
    return name_results[0]


def final_grade(line):
    name_results = line.split("_")
    grades = name_results[-1].split()
    sum_grades = 0

    for i in grades:
        sum_grades += float(i)

    average = float(sum_grades/len(grades))
    result = int(average * 2 + 0.5) / 2

    result = 6.0 if result == 5.5 else result

    return result


def report_geography(group_number, lines):
    print("Report for group %s" % group_number)

    for line in lines:
        print("%s has a final grade of %.1f" % (student_name(line), final_grade(line)))

    print("End of report")


file = open("geo_grades2.in.txt").read()
lines = file.splitlines()
group_number = input("Enter the group number: ")
report_geography(group_number, lines)