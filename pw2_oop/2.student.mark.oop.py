# Practical Work 2: OOP'ed Student Mark Management

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name}"


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark = mark

    def get_student_id(self):
        return self.__student_id

    def get_course_id(self):
        return self.__course_id

    def get_mark(self):
        return self.__mark


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []

    # ---------- Input methods ----------
    def input_students(self):
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
            self.__students.append(Student(sid, name, dob))

    def input_courses(self):
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
            self.__courses.append(Course(cid, name))

    def input_marks(self):
        if not self.__courses:
            print("No courses available.")
            return
        print("\nAvailable courses:")
        for c in self.__courses:
            print(f"  {c}")
        cid = input("Select course ID: ").strip()
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            print("Course not found.")
            return
        print(f"\nInput marks for: {course.get_name()}")
        for s in self.__students:
            while True:
                try:
                    m = float(input(f"  Mark for {s.get_name()} ({s.get_id()}): "))
                    self.__marks.append(Mark(s.get_id(), cid, m))
                    break
                except ValueError:
                    print("Invalid mark.")

    # ---------- List methods ----------
    def list_students(self):
        print("\n=== Students ===")
        if not self.__students:
            print("No students.")
            return
        for s in self.__students:
            print(f"  {s}")

    def list_courses(self):
        print("\n=== Courses ===")
        if not self.__courses:
            print("No courses.")
            return
        for c in self.__courses:
            print(f"  {c}")

    def show_marks(self):
        if not self.__courses:
            print("No courses.")
            return
        print("\nAvailable courses:")
        for c in self.__courses:
            print(f"  {c}")
        cid = input("Select course ID: ").strip()
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            print("Course not found.")
            return
        print(f"\n=== Marks for {course.get_name()} ===")
        for s in self.__students:
            mark_obj = next(
                (m for m in self.__marks
                 if m.get_student_id() == s.get_id() and m.get_course_id() == cid),
                None
            )
            mark_val = mark_obj.get_mark() if mark_obj else "N/A"
            print(f"  {s.get_name()} ({s.get_id()}): {mark_val}")

    # ---------- Main menu ----------
    def run(self):
        print("===== STUDENT MARK MANAGEMENT (OOP) =====")
        while True:
            print("\n1. Input students")
            print("2. Input courses")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("0. Exit")
            choice = input("Your choice: ").strip()
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
                self.show_marks()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()
