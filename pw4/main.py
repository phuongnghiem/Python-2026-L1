# Practical Work 4: Modularized Student Mark Management

from input import input_students, input_courses, input_marks
from output import list_students, list_courses, show_marks


def main():
    students = []
    courses = []
    marks = []

    print("===== STUDENT MARK MANAGEMENT (Modular - PW4) =====")
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students (sorted by GPA)")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            input_students(students)
        elif choice == "2":
            input_courses(courses)
        elif choice == "3":
            input_marks(students, courses, marks)
        elif choice == "4":
            list_students(students, marks, courses)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            show_marks(students, courses, marks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
