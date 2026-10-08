students = []
courses = []
marks = {}

n = int(input("Enter number of students: "))
for i in range(n):
    print("Student", i + 1)

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth: ")

    student = [student_id, name, dob]
    students.append(student)
m = int(input("Enter number of courses: "))
for i in range(m):
    print("Course", i + 1)

    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")

    course = [course_id, course_name]
    courses.append(course)
print("\nSTUDENTS")

for student in students:
    print(student[0], student[1],  student[2])

print("\nCOURSES ")

for course in courses:
    print(course[0], course[1])

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

print(" \nSTUDENT MARKS ")
for course in courses:
    course_id = course[0]
    course_name = course[1]
    print("Courses:",course_name)
    
    for student in students:
        student_id= student[0]
        student_name=student[1]
        print(name, ":", marks[course_id][student_id])