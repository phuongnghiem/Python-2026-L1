class Student:
    """Represents an individual student with encapsulated attributes."""

    def __init__(self, student_id="", name="", dob=""):
        self._id = student_id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def input(self):
        self._id = input("Student ID: ").strip()
        self._name = input("Student name: ").strip()
        self._dob = input("Date of Birth (DD/MM/YYYY): ").strip()

    def list(self):
        print(f"ID: {self._id} | Name: {self._name} | DoB: {self._dob}")


class Course:
    """Represents an individual course with encapsulated attributes."""

    def __init__(self, course_id="", name=""):
        self._id = course_id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def input(self):
        self._id = input("Course ID: ").strip()
        self._name = input("Course name: ").strip()

    def list(self):
        print(f"ID: {self._id} | Name: {self._name}")


class StudentMarkManagement:
    """Manager class handling operational workflows and data storage."""

    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}  

    def input_students(self):
        num_students = int(input("Enter number of students in class: "))
        self._students = []
        for i in range(num_students):
            print(f"\n--- Enter information for student #{i + 1} ---")
            std = Student()
            std.input()
            self._students.append(std)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        self._courses = []
        for i in range(num_courses):
            print(f"\n--- Enter information for course #{i + 1} ---")
            crs = Course()
            crs.input()
            self._courses.append(crs)

    def input_marks(self):
        if not self._courses:
            print("No course data available. Please input courses first!")
            return
        if not self._students:
            print("No student data available. Please input students first!")
            return

        print("\nCourse list:")
        for crs in self._courses:
            crs.list()

        course_id = input("\nSelect a course ID to input marks: ").strip()
        selected_course = next((c for c in self._courses if c.get_id() == course_id), None)

        if not selected_course:
            print("Course not found!")
            return

        if course_id not in self._marks:
            self._marks[course_id] = {}

        print(f"\n--- Input marks for course: {selected_course.get_name()} ---")
        for std in self._students:
            mark = float(input(f"Enter mark for student {std.get_name()} (ID: {std.get_id()}): "))
            self._marks[course_id][std.get_id()] = mark

    def list_courses(self):
        if not self._courses:
            print("No courses available.")
            return
        print("\n=== COURSE LIST ===")
        for crs in self._courses:
            crs.list()

    def list_students(self):
        if not self._students:
            print("No students available.")
            return
        print("\n=== STUDENT LIST ===")
        for std in self._students:
            std.list()

    def show_student_marks(self):
        if not self._marks:
            print("No mark data available.")
            return

        course_id = input("Enter course ID to show marks: ").strip()
        if course_id not in self._marks:
            print("No marks recorded for this course or invalid course ID.")
            return

        selected_course = next((c for c in self._courses if c.get_id() == course_id), None)
        course_name = selected_course.get_name() if selected_course else course_id

        print(f"\n=== MARKS FOR COURSE: {course_name} ===")
        student_dict = {std.get_id(): std.get_name() for std in self._students}

        for std_id, mark in self._marks[course_id].items():
            std_name = student_dict.get(std_id, "Unknown")
            print(f"Student ID: {std_id} | Name: {std_name} | Mark: {mark}")

    def run(self):
        while True:
            print("\n" + "=" * 35)
            print("  STUDENT MARK MANAGEMENT (PW2 - OOP)")
            print("=" * 35)
            print("1. Input student list")
            print("2. Input course list")
            print("3. Select course and input marks")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks for a course")
            print("0. Exit")

            choice = input("Your choice (0-6): ").strip()

            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '0':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again!")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()