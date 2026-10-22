from domains import Student, Course, Mark
import os


def input_students(students):
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            print("Must be positive.")
        except ValueError:
            print("Invalid number.")
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("Student ID: ").strip()
        name = input("Name: ").strip()
        dob = input("DoB (dd/mm/yyyy): ").strip()
        students.append(Student(sid, name, dob))
    write_students(students)


def input_courses(courses):
    while True:
        try:
            n = int(input("Enter number of courses: "))
            if n > 0:
                break
            print("Must be positive.")
        except ValueError:
            print("Invalid number.")
    for i in range(n):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ").strip()
        name = input("Course name: ").strip()
        try:
            credits = int(input("Credits (default 3): ").strip() or "3")
        except ValueError:
            credits = 3
        courses.append(Course(cid, name, credits))
    write_courses(courses)


def input_marks(students, courses, marks):
    if not courses:
        print("No courses available.")
        return
    print("\nAvailable courses:")
    for c in courses:
        print(f"  {c}")
    cid = input("Select course ID: ").strip()
    course = next((c for c in courses if c.get_id() == cid), None)
    if not course:
        print("Course not found.")
        return
    print(f"\nInput marks for: {course.get_name()}")
    for s in students:
        while True:
            try:
                m = float(input(f"  Mark for {s.get_name()} ({s.get_id()}): "))
                marks.append(Mark(s.get_id(), cid, m))
                break
            except ValueError:
                print("Invalid mark.")
    write_marks(marks)


def write_students(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()}|{s.get_name()}|{s.get_dob()}\n")
    print("→ Saved students to students.txt")


def write_courses(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()}|{c.get_name()}|{c.get_credits()}\n")
    print("→ Saved courses to courses.txt")


def write_marks(marks):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for m in marks:
            f.write(f"{m.get_student_id()}|{m.get_course_id()}|{m.get_mark()}\n")
    print("→ Saved marks to marks.txt")


def load_students():
    students = []
    if not os.path.exists("students.txt"):
        return students
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                students.append(Student(parts[0], parts[1], parts[2]))
    return students


def load_courses():
    courses = []
    if not os.path.exists("courses.txt"):
        return courses
    with open("courses.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                courses.append(Course(parts[0], parts[1], int(parts[2])))
    return courses


def load_marks():
    marks = []
    if not os.path.exists("marks.txt"):
        return marks
    with open("marks.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                marks.append(Mark(parts[0], parts[1], float(parts[2])))
    return marks
