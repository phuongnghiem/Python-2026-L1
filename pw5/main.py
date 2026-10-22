# Practical Work 5: Persistent Student Mark Management

from input import (
    input_students, input_courses, input_marks,
    load_students, load_courses, load_marks
)
from output import list_students, list_courses, show_marks
from persistence import compress_data, decompress_and_load
import os


def main():
    # Try to load from compressed file first
    if os.path.exists("students.dat"):
        students, courses, marks = decompress_and_load()
    else:
        students = load_students()
        courses = load_courses()
        marks = load_marks()
        if students or courses or marks:
            print("→ Loaded from text files")

    print("===== STUDENT MARK MANAGEMENT (PW5 - Persistent) =====")
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students (sorted by GPA)")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Compress & Save (students.dat)")
        print("0. Exit (auto-compress)")
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
        elif choice == "7":
            compress_data(students, courses, marks)
        elif choice == "0":
            compress_data(students, courses, marks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
