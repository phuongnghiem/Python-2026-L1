
def input_number_of_students():
    return int(input("Enter number of students in class: "))

def input_students(num_students):
    students = []
    for i in range(num_students):
        print(f"\n--- Enter information for student #{i + 1} ---")
        std_id = input("Student ID: ").strip()
        name = input("Student name: ").strip()
        dob = input("Date of Birth (DD/MM/YYYY): ").strip()
        students.append({"id": std_id, "name": name, "dob": dob})
    return students

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_courses(num_courses):
    courses = []
    for i in range(num_courses):
        print(f"\n--- Enter information for course #{i + 1} ---")
        course_id = input("Course ID: ").strip()
        name = input("Course name: ").strip()
        courses.append({"id": course_id, "name": name})
    return courses

def input_marks(students, courses, marks):
    if not courses:
        print("No course data available. Please input courses first!")
        return
    if not students:
        print("No student data available. Please input students first!")
        return

    print("\nCourse list:")
    for course in courses:
        print(f"- ID: {course['id']} | Name: {course['name']}")

    course_id = input("\nSelect a course ID to input marks: ").strip()
    
    selected_course = next((c for c in courses if c['id'] == course_id), None)
    if not selected_course:
        print("Course not found!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\n--- Input marks for course: {selected_course['name']} ---")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark


def list_courses(courses):
    if not courses:
        print("No courses available.")
        return
    print("\n=== COURSE LIST ===")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

def list_students(students):
    if not students:
        print("No students available.")
        return
    print("\n=== STUDENT LIST ===")
    for std in students:
        print(f"ID: {std['id']} | Name: {std['name']} | DoB: {std['dob']}")

def show_student_marks(students, courses, marks):
    if not marks:
        print("No mark data available.")
        return

    course_id = input("Enter course ID to show marks: ").strip()
    if course_id not in marks:
        print("No marks recorded for this course or invalid course ID.")
        return

    selected_course = next((c for c in courses if c['id'] == course_id), None)
    course_name = selected_course['name'] if selected_course else course_id

    print(f"\n=== MARKS FOR COURSE: {course_name} ===")
    student_dict = {std['id']: std['name'] for std in students}
    
    for std_id, mark in marks[course_id].items():
        std_name = student_dict.get(std_id, "Unknown")
        print(f"Student ID: {std_id} | Name: {std_name} | Mark: {mark}")


def main():
    students = []
    courses = []
    marks = {}  # Data structure: {course_id: {student_id: mark}}

    while True:
        print("\n" + "="*35)
        print("  STUDENT MARK MANAGEMENT (PW1)")
        print("="*35)
        print("1. Input student list")
        print("2. Input course list")
        print("3. Select course and input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a course")
        print("0. Exit")
        
        choice = input("Your choice (0-6): ").strip()
        
        if choice == '1':
            num = input_number_of_students()
            students = input_students(num)
        elif choice == '2':
            num = input_number_of_courses()
            courses = input_courses(num)
        elif choice == '3':
            input_marks(students, courses, marks)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            show_student_marks(students, courses, marks)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()