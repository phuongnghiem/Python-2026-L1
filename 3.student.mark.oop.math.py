import math
import numpy as np

students = []
courses = []
marks = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth: ")

    student = [student_id, name, dob]
    students.append(student)

m = int(input("\nEnter number of courses: "))

for i in range(m):
    print("\nCourse", i + 1)

    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))

    course = [course_id, course_name, credits]
    courses.append(course)

print("\nSTUDENTS")

for student in students:
    print(student[0], student[1], student[2])

print("\nCOURSES")

for course in courses:
    print(course[0], course[1], course[2])

for course in courses:
    course_id = course[0]
    course_name = course[1]

    print("\nEnter marks for", course_name)

    marks[course_id] = {}

    for student in students:
        student_id = student[0]
        student_name = student[1]

        mark = float(input("Enter mark for " + student_name + ": "))

        marks[course_id][student_id] = mark

print("\nSTUDENT MARKS")

for course in courses:
    course_id = course[0]
    course_name = course[1]

    print("\nCourse:", course_name)

    for student in students:
        student_id = student[0]
        student_name = student[1]

        print(student_name, ":", marks[course_id][student_id])

def calculate_gpa(student_id):
    total_credits = 0
    total_weighted_marks = 0

    for course in courses:
        course_id = course[0]
        credits = course[2]
        mark = marks[course_id][student_id]

        total_weighted_marks += mark * credits
        total_credits += credits

    if total_credits == 0:
        return 0

    return total_weighted_marks / total_credits

gpa_list = []

for student in students:
    student_id = student[0]
    student_name = student[1]

    gpa = calculate_gpa(student_id)

    gpa_list.append([student_id, student_name, gpa])

gpa_array = np.array(gpa_list, dtype=object)

gpa_array = gpa_array[
    np.argsort(gpa_array[:, 2].astype(float))[::-1]
]

print("\nSTUDENTS GPA")

for student in gpa_array:
    print(
        student[0],
        student[1],
        "GPA:",
        round(float(student[2]), 2)
    )

print("\nSTUDENT RANKING")

for i in range(len(gpa_array)):
    print(
        "Rank", i + 1,
        ":", gpa_array[i][1],
        "| ID:", gpa_array[i][0],
        "| GPA:", round(float(gpa_array[i][2]), 2)
    )