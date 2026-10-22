students = []  # list of dicts: {"id": ..., "name": ..., "dob": ...}
courses = []   # list of dicts: {"id": ..., "name": ...}
marks = {}     # {(student_id, course_id): mark}


def input_number_of_students():
    while True:
        try:
            n = int(input("Enter number of students in class: "))
            if n > 0:
                return n
            print("Number must be positive.")
        except ValueError:
            print("Please enter a valid integer.")


def input_student_info(n):
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        dob = input("Enter date of birth (dd/mm/yyyy): ").strip()
        students.append({"id": sid, "name": name, "dob": dob})


def input_number_of_courses():
    while True:
        try:
            n = int(input("Enter number of courses: "))
            if n > 0:
                return n
            print("Number must be positive.")
        except ValueError:
            print("Please enter a valid integer.")


def input_course_info(n):
    for i in range(n):
        print(f"\n--- Course {i+1} ---")
        cid = input("Enter course ID: ").strip()
        name = input("Enter course name: ").strip()
        courses.append({"id": cid, "name": name})


def select_course_and_input_marks():
    if not courses:
        print("No courses available.")
        return
    print("\nAvailable courses:")
    for c in courses:
        print(f"  {c['id']}: {c['name']}")
    cid = input("Select course ID to input marks: ").strip()
    course = next((c for c in courses if c["id"] == cid), None)
    if not course:
        print("Course not found.")
        return
    print(f"\nInput marks for course: {course['name']}")
    for s in students:
        while True:
            try:
                m = float(input(f"  Mark for {s['name']} ({s['id']}): "))
                marks[(s["id"], cid)] = m
                break
            except ValueError:
                print("Invalid mark. Try again.")


def list_courses():
    print("\n=== Courses ===")
    if not courses:
        print("No courses.")
        return
    for c in courses:
        print(f"  ID: {c['id']} | Name: {c['name']}")


def list_students():
    print("\n=== Students ===")
    if not students:
        print("No students.")
        return
    for s in students:
        print(f"  ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")


def show_student_marks():
    if not courses:
        print("No courses available.")
        return
    print("\nAvailable courses:")
    for c in courses:
        print(f"  {c['id']}: {c['name']}")
    cid = input("Select course ID to show marks: ").strip()
    course = next((c for c in courses if c["id"] == cid), None)
    if not course:
        print("Course not found.")
        return
    print(f"\n=== Marks for {course['name']} ===")
    for s in students:
        key = (s["id"], cid)
        mark = marks.get(key, "N/A")
        print(f"  {s['name']} ({s['id']}): {mark}")


def main():
    print("===== STUDENT MARK MANAGEMENT SYSTEM =====")
    while True:
        print("\n1. Input number of students + student info")
        print("2. Input number of courses + course info")
        print("3. Select a course and input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("0. Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            n = input_number_of_students()
            input_student_info(n)
        elif choice == "2":
            n = input_number_of_courses()
            input_course_info(n)
        elif choice == "3":
            select_course_and_input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
