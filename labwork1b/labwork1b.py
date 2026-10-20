"""
Practical Work 1: Student Mark Management
-------------------------------------------
Functions:
  Input functions:
    - input_num_students()
    - input_students(n)
    - input_num_courses()
    - input_courses(n)
    - input_marks(students, courses, marks)
  Listing functions:
    - list_courses(courses)
    - list_students(students)
    - show_marks_for_course(courses, marks, students)
"""


# ---------------------- INPUT FUNCTIONS ----------------------

def input_num_students():
    """Ask the user how many students are in the class."""
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                return n
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter an integer.")


def input_students(n):
    """Input information (id, name, DoB) for n students.
    Returns a list of dicts: {'id':..., 'name':..., 'dob':...}
    """
    students = []
    for i in range(n):
        print(f"\n-- Student {i + 1} --")
        sid = input("  ID: ").strip()
        name = input("  Name: ").strip()
        dob = input("  Date of birth (dd/mm/yyyy): ").strip()
        students.append({"id": sid, "name": name, "dob": dob})
    return students


def input_num_courses():
    """Ask the user how many courses there are."""
    while True:
        try:
            n = int(input("Enter number of courses: "))
            if n > 0:
                return n
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter an integer.")


def input_courses(n):
    """Input information (id, name) for n courses.
    Returns a list of dicts: {'id':..., 'name':...}
    """
    courses = []
    for i in range(n):
        print(f"\n-- Course {i + 1} --")
        cid = input("  Course ID: ").strip()
        name = input("  Course name: ").strip()
        courses.append({"id": cid, "name": name})
    return courses


def find_course(courses, cid):
    for c in courses:
        if c["id"] == cid:
            return c
    return None


def find_student(students, sid):
    for s in students:
        if s["id"] == sid:
            return s
    return None


def input_marks(students, courses, marks):
    """Select a course, then input marks for every student in that course.
    marks is a dict: {course_id: {student_id: mark}}
    """
    if not courses:
        print("No courses available. Please input courses first.")
        return
    if not students:
        print("No students available. Please input students first.")
        return

    list_courses(courses)
    cid = input("Enter the ID of the course to input marks for: ").strip()
    course = find_course(courses, cid)
    if course is None:
        print("Course not found.")
        return

    marks.setdefault(cid, {})
    for s in students:
        while True:
            try:
                mark = float(input(f"  Mark for {s['name']} (id={s['id']}): "))
                marks[cid][s["id"]] = mark
                break
            except ValueError:
                print("  Invalid mark, please enter a number.")
    print(f"Marks for course '{course['name']}' have been recorded.")


# ---------------------- LISTING FUNCTIONS ----------------------

def list_courses(courses):
    """Print all courses."""
    print("\n=== List of Courses ===")
    if not courses:
        print("(no courses)")
        return
    for c in courses:
        print(f"  ID: {c['id']:<6} Name: {c['name']}")


def list_students(students):
    """Print all students."""
    print("\n=== List of Students ===")
    if not students:
        print("(no students)")
        return
    for s in students:
        print(f"  ID: {s['id']:<6} Name: {s['name']:<20} DoB: {s['dob']}")


def show_marks_for_course(courses, marks, students):
    """Show all student marks for a chosen course."""
    if not courses:
        print("No courses available.")
        return

    list_courses(courses)
    cid = input("Enter the ID of the course to show marks for: ").strip()
    course = find_course(courses, cid)
    if course is None:
        print("Course not found.")
        return

    course_marks = marks.get(cid)
    if not course_marks:
        print(f"No marks have been recorded yet for '{course['name']}'.")
        return

    print(f"\n=== Marks for course '{course['name']}' ===")
    for sid, mark in course_marks.items():
        student = find_student(students, sid)
        name = student["name"] if student else "(unknown)"
        print(f"  ID: {sid:<6} Name: {name:<20} Mark: {mark}")


# ---------------------- MAIN MENU ----------------------

def print_menu():
    print("\n===== STUDENT MARK MANAGEMENT =====")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. Show marks for a course")
    print("0. Exit")


def main():
    students = []
    courses = []
    marks = {}  # {course_id: {student_id: mark}}

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            n = input_num_students()
            students = input_students(n)
        elif choice == "2":
            n = input_num_courses()
            courses = input_courses(n)
        elif choice == "3":
            input_marks(students, courses, marks)
        elif choice == "4":
            list_courses(courses)
        elif choice == "5":
            list_students(students)
        elif choice == "6":
            show_marks_for_course(courses, marks, students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()