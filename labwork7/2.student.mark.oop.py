"""Practical work 2: OOP'ed student mark management.

Same functions as practical work 1 (input students/courses/marks, list students/courses,
show marks of a course), now organised as classes:
  - Entity   : abstract base class, defines the polymorphic .input() and .list() methods
  - Student  : an Entity with private attributes and its own marks
  - Course   : an Entity
  - School   : manages the students/courses and drives the menu
"""
from abc import ABC, abstractmethod


# ---------- helpers ----------
def read_int(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
        except ValueError:
            pass
        print("  Please enter a whole number >=", minimum)


def read_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 20:
                return mark
        except ValueError:
            pass
        print("  Mark must be a number between 0 and 20")


# ---------- polymorphism: one interface, many entities ----------
class Entity(ABC):
    @abstractmethod
    def input(self):
        """Read this entity's information from the keyboard."""

    @abstractmethod
    def list(self):
        """Print this entity on one line."""


class Student(Entity):
    def __init__(self, sid="", name="", dob=""):
        # private attributes (encapsulation): outside code uses the properties below
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}  # course id -> mark

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def dob(self):
        return self.__dob

    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id)  # None when no mark yet

    def input(self):
        self.__id = input("  Student ID: ").strip()
        self.__name = input("  Student name: ").strip()
        self.__dob = input("  Student date of birth: ").strip()

    def list(self):
        print(f"{self.__id:<10}{self.__name:<25}{self.__dob}")


class Course(Entity):
    def __init__(self, cid="", name=""):
        self.__id = cid
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def input(self):
        self.__id = input("  Course ID: ").strip()
        self.__name = input("  Course name: ").strip()

    def list(self):
        print(f"{self.__id:<10}{self.__name}")


# ---------- the system ----------
class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def __input_entities(self, entity_class, label):
        """Works for ANY Entity subclass thanks to polymorphism (.input())."""
        n = read_int(f"Number of {label}s: ", 1)
        entities = []
        for i in range(1, n + 1):
            print(f"{label.capitalize()} {i}")
            entity = entity_class()
            entity.input()
            entities.append(entity)
        return entities

    @staticmethod
    def __list_entities(title, entities):
        """Works for ANY Entity subclass thanks to polymorphism (.list())."""
        print(f"\n--- {title} ---")
        for entity in entities:
            entity.list()

    def input_students(self):
        self.__students.extend(self.__input_entities(Student, "student"))

    def input_courses(self):
        self.__courses.extend(self.__input_entities(Course, "course"))

    def __find_course(self, course_id):
        return next((c for c in self.__courses if c.id == course_id), None)

    def __choose_course(self):
        self.list_courses()
        course = self.__find_course(input("Course ID: ").strip())
        if course is None:
            print("No such course.")
        return course

    def input_marks(self):
        if not self.__students or not self.__courses:
            print("Add students and courses first.")
            return
        course = self.__choose_course()
        if course is None:
            return
        for student in self.__students:
            student.set_mark(course.id, read_mark(f"  Mark of {student.name} ({student.id}): "))

    def list_students(self):
        self.__list_entities("Students", self.__students)

    def list_courses(self):
        self.__list_entities("Courses", self.__courses)

    def show_marks_for_course(self):
        course = self.__choose_course()
        if course is None:
            return
        print(f"\n--- Marks of {course.name} ---")
        for student in self.__students:
            mark = student.get_mark(course.id)
            print(f"{student.id:<10}{student.name:<25}{'-' if mark is None else mark}")

    def run(self):
        menu = {
            "1": ("Input students", self.input_students),
            "2": ("Input courses", self.input_courses),
            "3": ("Input marks for a course", self.input_marks),
            "4": ("List students", self.list_students),
            "5": ("List courses", self.list_courses),
            "6": ("Show marks for a course", self.show_marks_for_course),
            "0": ("Exit", None),
        }
        while True:
            print("\n=== Student mark management ===")
            for key, (label, _) in menu.items():
                print(f"[{key}] {label}")
            choice = input("Choose: ").strip()
            if choice == "0":
                break
            if choice in menu:
                menu[choice][1]()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    School().run()
