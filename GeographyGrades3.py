"""Assignment: Geography Grades 3
Created on 15 june 2021
Author: Jelmer Haverkate"""

# This program reads the results for three tests from an input file for each student
# and calculates and prints the final grade for each student per group.


def student_name(line):
    name_results = line.split("_")
    return name_results[0]


def final_grade(line):
    name_results = line.split("_")
    grades = name_results[-1].split()
    sum_grades = 0

    for i in grades:
        sum_grades += float(i)

    average = sum_grades/len(grades)
    result = int(average * 2 + 0.5) / 2

    result = 6.0 if result == 5.5 else result

    return result


def report_geography(group_number, lines):
    print("Report for group %s" % group_number)

    for line in lines:
        print("%s has a final grade of %.1f" % (student_name(line), final_grade(line)))

    print("End of report\n")


file = open("geo_grades3.in.txt").read()
groups = file.split("=\n")

for group in groups:
    group = group.splitlines()
    lines = group[1::]
    group_number = group[0]
    report_geography(group_number, lines)
