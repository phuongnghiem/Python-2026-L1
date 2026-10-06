students = []
courses = []
marks = {}

def input_number_of_students():
    while True:
        try:
            count = int(input("Enter number of students in class: "))
            if count > 0:
                return count
            print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

def input_student_info(num_students):
    print("\n--- INPUT STUDENT INFORMATION ---")
    for i in range(num_students):
        print(f"\nStudent {i + 1}:")
        s_id = input("  - Student ID: ").strip()
        s_name = input("  - Student Name: ").strip()
        s_dob = input("  - Date of Birth (DoB): ").strip()
        students.append({
            'id': s_id,
            'name': s_name,
            'dob': s_dob
        })

def input_number_of_courses():
    while True:
        try:
            count = int(input("Enter number of courses: "))
            if count > 0:
                return count
            print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

def input_course_info(num_courses):
    print("\n--- INPUT COURSE INFORMATION ---")
    for i in range(num_courses):
        print(f"\nCourse {i + 1}:")
        c_id = input("  - Course ID: ").strip()
        c_name = input("  - Course Name: ").strip()
        courses.append({
            'id': c_id,
            'name': c_name
        })

def input_marks_for_course():
    if not courses:
        print("\n[!] No courses available. Please input course information first.")
        return
    if not students:
        print("\n[!] No students available. Please input student information first.")
        return

    list_courses()
    selected_course_id = input("\nEnter Course ID to input marks for: ").strip()

    course_found = any(c['id'] == selected_course_id for c in courses)
    if not course_found:
        print("\n[!] Course ID not found.")
        return

    if selected_course_id not in marks:
        marks[selected_course_id] = {}

    print(f"\n--- INPUT MARKS FOR COURSE ID: {selected_course_id} ---")
    for s in students:
        while True:
            try:
                mark = float(input(f"  - Mark for '{s['name']}' (ID: {s['id']}): "))
                if 0 <= mark <= 20:
                    marks[selected_course_id][s['id']] = mark
                    break
                else:
                    print("    Mark must be between 0 and 20.")
            except ValueError:
                print("    Please enter a valid number.")

def list_courses():
    print("\n=== COURSE LIST ===")
    if not courses:
        print("No courses found.")
        return
    for index, c in enumerate(courses, 1):
        print(f"{index}. ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n=== STUDENT LIST ===")
    if not students:
        print("No students found.")
        return
    for index, s in enumerate(students, 1):
        print(f"{index}. ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks_for_course():
    if not courses:
        print("\n[!] No courses available.")
        return

    list_courses()
    selected_course_id = input("\nEnter Course ID to view marks: ").strip()

    if selected_course_id not in marks or not marks[selected_course_id]:
        print(f"\n[!] No marks recorded for Course ID: {selected_course_id}")
        return

    print(f"\n=== MARKS FOR COURSE ID: {selected_course_id} ===")
    for s in students:
        s_id = s['id']
        mark = marks[selected_course_id].get(s_id, "N/A")
        print(f"ID: {s_id} | Name: {s['name']} | Mark: {mark}")

def main():
    while True:
        print("\n" + "="*40)
        print("   STUDENT MARK MANAGEMENT (PRACTICAL 1)")
        print("="*40)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")
        print("="*40)

        choice = input("Select an option (0-6): ").strip()

        if choice == '1':
            n = input_number_of_students()
            input_student_info(n)
        elif choice == '2':
            m = input_number_of_courses()
            input_course_info(m)
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks_for_course()
        elif choice == '0':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please select from 0 to 6.")

if __name__ == "__main__":
    main()