"""Assignment: Administration
Created on 16 june 2021
Author: Jelmer Haverkate"""

# This program reads students results and similarities between student programs from an input file
# and calculates the final grade and prints it together with a graph of similarity scores.


def final_grade(grades):
    sum_grades = 0

    for grade in grades:
        sum_grades += float(grade)

    average = sum_grades / len(grades)
    result = int(average * 2 + 0.5) / 2

    if 6 > result >= 5.5:
        result = "6-"

    return str(result)


def graph_similarity_scores(similarity_scores):
    output = "\t"

    for i in similarity_scores:
        if int(i) == 0:
            output += "_"
        elif int(i) < 20:
            output += "-"
        else:
            output += "^"

    print("%s" % output)


def print_matches(matches):
    for match in matches:
        if len(match) == 0:
            print("\tNo matches found")
        else:
            print("\t%s" % match)


def report_grades_and_plagiarism(lines):
    for line in lines:
        if line in lines[::2]:
            line = line.split("_")
            student_name = line[0]
            grades = line[-1].split()
            print(" %s has an average of %s" % (student_name, final_grade(grades)))
        else:
            line = line.split(";")
            similarity_scores = line[0].split("=")
            matches = line[1].split(",")
            graph_similarity_scores(similarity_scores)
            print_matches(matches)


file = open("administration.input.txt").read().strip()
lines = file.splitlines()
report_grades_and_plagiarism(lines)
