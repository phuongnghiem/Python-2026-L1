# Practical Work 8: Multithreaded Student Mark Management

from input import (
    input_students, input_courses, input_marks,
    load_students, load_courses, load_marks
)
from output import list_students, list_courses, show_marks
from persistence import compress_data_async, decompress_and_load
import os
import time


def main():
    if os.path.exists("students.dat"):
        students, courses, marks = decompress_and_load()
    else:
        students = load_students()
        courses = load_courses()
        marks = load_marks()
        if students or courses or marks:
            print("→ Loaded from text files")

    print("===== STUDENT MARK MANAGEMENT (PW8 - Multithreaded) =====")
    save_thread = None

    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students (sorted by GPA)")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Compress & Save (background thread)")
        print("0. Exit (wait for background save)")
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
            save_thread = compress_data_async(students, courses, marks)
        elif choice == "0":
            save_thread = compress_data_async(students, courses, marks)
            if save_thread and save_thread.is_alive():
                print("Waiting for background save to finish...")
                save_thread.join(timeout=5)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
