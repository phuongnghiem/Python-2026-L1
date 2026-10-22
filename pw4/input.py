from domains import Student, Course, Mark


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
