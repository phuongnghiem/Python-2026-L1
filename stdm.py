# Data structures
students = []
courses = []
marks = {}  # Structure: {course_id: {student_id: mark}}

# 1. Input Functions
def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        s_id = input("  Enter student ID: ")
        name = input("  Enter student name: ")
        dob = input("  Enter Date of Birth (dd/mm/yyyy): ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    num_courses = int(input("\nEnter number of courses: "))
    for _ in range(num_courses):
        c_id = input("  Enter course ID: ")
        name = input("  Enter course name: ")
        courses.append({"id": c_id, "name": name})

def input_marks():
    if not courses or not students:
        print("Please enter student and course information first!")
        return
    
    course_id = input("\nEnter course ID to input marks: ")
    # Check if the course ID exists
    if not any(c['id'] == course_id for c in courses):
        print("Course does not exist!")
        return

    marks[course_id] = {}
    print(f"--- Input marks for course {course_id} ---")
    for s in students:
        mark = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
        marks[course_id][s['id']] = mark

# 2. Listing Functions
def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_course_marks():
    course_id = input("\nEnter course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course!")
        return

    print(f"\n--- Marks for course {course_id} ---")
    for s in students:
        s_id = s['id']
        mark = marks[course_id].get(s_id, "N/A")
        print(f"Student: {s['name']} (ID: {s_id}) -> Mark: {mark}")

# 3. Main Program Loop
def main():
    input_students()
    input_courses()
    
    while True:
        print("\n=== STUDENT MARK MANAGEMENT ===")
        print("1. Input course marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show course marks")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        if choice == '1':
            input_marks()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            list_students()
        elif choice == '4':
            show_course_marks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()