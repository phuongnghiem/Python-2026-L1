class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input(self):
        self.__id = input("Enter Student ID: ").strip()
        self.__name = input("Enter Student Name: ").strip()
        self.__dob = input("Enter Student DoB (DD/MM/YYYY): ").strip()

    def list(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name:<20} | DoB: {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input(self):
        self.__id = input("Enter Course ID: ").strip()
        self.__name = input("Enter Course Name: ").strip()

    def list(self):
        print(f"ID: {self.__id:<10} | Course Name: {self.__name}")


class Mark:
    def __init__(self, student_id="", course_id="", mark=0.0):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark = mark

    def get_student_id(self):
        return self.__student_id

    def get_course_id(self):
        return self.__course_id

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark

    def input(self, student_id, course_id):
        self.__student_id = student_id
        self.__course_id = course_id
        while True:
            try:
                val = float(input(f"Enter mark for Student ID {student_id}: "))
                if 0 <= val <= 20:
                    self.__mark = val
                    break
                print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def list(self):
        print(f"Student ID: {self.__student_id:<10} | Course ID: {self.__course_id:<10} | Mark: {self.__mark:.2f}")


class SchoolManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []

    def input_students(self):
        try:
            n = int(input("Enter number of students: "))
            for i in range(n):
                print(f"\n--- Student {i+1} ---")
                student = Student()
                student.input()
                self.__students.append(student)
        except ValueError:
            print("Invalid number.")

    def input_courses(self):
        try:
            n = int(input("Enter number of courses: "))
            for i in range(n):
                print(f"\n--- Course {i+1} ---")
                course = Course()
                course.input()
                self.__courses.append(course)
        except ValueError:
            print("Invalid number.")

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Please input students and courses first!")
            return

        print("\nAvailable Courses:")
        self.list_courses()
        c_id = input("Select Course ID to input marks for: ").strip()

        course_exists = any(c.get_id() == c_id for c in self.__courses)
        if not course_exists:
            print("Course ID not found.")
            return

        print(f"\nInputting marks for Course ID: {c_id}")
        for student in self.__students:
            mark_entry = None
            for m in self.__marks:
                if m.get_student_id() == student.get_id() and m.get_course_id() == c_id:
                    mark_entry = m
                    break
            
            if not mark_entry:
                mark_entry = Mark()
                mark_entry.input(student.get_id(), c_id)
                self.__marks.append(mark_entry)
            else:
                mark_entry.input(student.get_id(), c_id)

    def list_students(self):
        if not self.__students:
            print("No students registered.")
            return
        print("\n=== Student List ===")
        for s in self.__students:
            s.list()

    def list_courses(self):
        if not self.__courses:
            print("No courses registered.")
            return
        print("\n=== Course List ===")
        for c in self.__courses:
            c.list()

    def list_marks(self):
        if not self.__courses:
            print("No courses available.")
            return
        
        c_id = input("Enter Course ID to view marks: ").strip()
        course_marks = [m for m in self.__marks if m.get_course_id() == c_id]

        if not course_marks:
            print(f"No marks found for Course ID: {c_id}")
            return

        print(f"\n=== Marks for Course {c_id} ===")
        for m in course_marks:
            m.list()

    def menu(self):
        while True:
            print("\n" + "="*35)
            print("  STUDENT MARK MANAGEMENT SYSTEM")
            print("="*35)
            print("1. Input Students")
            print("2. Input Courses")
            print("3. Input Marks for Course")
            print("4. List Students")
            print("5. List Courses")
            print("6. Show Marks for Course")
            print("0. Exit")
            
            choice = input("Enter choice (0-6): ").strip()
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.list_marks()
            elif choice == "0":
                print("Exiting program.")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    app = SchoolManagement()
    app.menu()