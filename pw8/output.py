import numpy as np


def calculate_gpa(student_id, marks, courses):
    student_marks = []
    credits = []
    for m in marks:
        if m.get_student_id() == student_id:
            course = next((c for c in courses if c.get_id() == m.get_course_id()), None)
            if course:
                student_marks.append(m.get_mark())
                credits.append(course.get_credits())
    if not student_marks:
        return 0.0
    marks_arr = np.array(student_marks)
    credits_arr = np.array(credits)
    gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
    return round(float(gpa), 1)


def update_all_gpa(students, marks, courses):
    for s in students:
        gpa = calculate_gpa(s.get_id(), marks, courses)
        s.set_gpa(gpa)


def list_students(students, marks, courses):
    update_all_gpa(students, marks, courses)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)
    print("\n=== Students (sorted by GPA descending) ===")
    if not students:
        print("No students.")
        return
    for s in students:
        print(f"  {s}")


def list_courses(courses):
    print("\n=== Courses ===")
    if not courses:
        print("No courses.")
        return
    for c in courses:
        print(f"  {c}")


def show_marks(students, courses, marks):
    if not courses:
        print("No courses.")
        return
    print("\nAvailable courses:")
    for c in courses:
        print(f"  {c}")
    cid = input("Select course ID: ").strip()
    course = next((c for c in courses if c.get_id() == cid), None)
    if not course:
        print("Course not found.")
        return
    print(f"\n=== Marks for {course.get_name()} ===")
    for s in students:
        mark_obj = next(
            (m for m in marks
             if m.get_student_id() == s.get_id() and m.get_course_id() == cid),
            None
        )
        mark_val = mark_obj.get_mark() if mark_obj else "N/A"
        print(f"  {s.get_name()} ({s.get_id()}): {mark_val}")
