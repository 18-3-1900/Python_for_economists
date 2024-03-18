"""Assignment: Geography Grades 1
Created on 16 june 2021
Author: Jelmer Haverkate"""

# This program reads the results for three tests from an input file for each student
# and calculates and prints the average grade for each student.


def name_and_results(line):
    return line.split("_")


def student_name(line):
    return name_and_results(line)[0]


def average_grade(line):
    grades = name_and_results(line)[-1].split()
    sum_grades = 0

    for i in grades:
        sum_grades += float(i)

    result = float(sum_grades/len(grades))
    return result


def report_geography(group_number, lines):
    print("Report for group %s" % group_number)

    for line in lines:
        print("%s has an average grade of %.1f" % (student_name(line), average_grade(line)))

    print("End of report")


file = open("geo_grades1.in.txt").read()
lines = file.splitlines()
group_number = input("Enter the group number: ")
report_geography(group_number, lines)

