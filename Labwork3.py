import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob} | GPA: {self.__gpa:.1f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}"


class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def calculate_gpa(self, student_id):
        student_marks = []
        course_credits = []
        for course in self.courses:
            c_id = course.get_id()
            if c_id in self.marks and student_id in self.marks[c_id]:
                student_marks.append(self.marks[c_id][student_id])
                course_credits.append(course.get_credits())

        if not student_marks or sum(course_credits) == 0:
            return 0.0

        marks_arr = np.array(student_marks)
        credits_arr = np.array(course_credits)
        weighted_gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        return math.floor(weighted_gpa * 10) / 10.0

    def update_gpas(self):
        for student in self.students:
            gpa = self.calculate_gpa(student.get_id())
            student.set_gpa(gpa)

    def sort_students_by_gpa(self):
        self.update_gpas()
        if not self.students:
            return
        gpas = np.array([s.get_gpa() for s in self.students])
        sorted_indices = np.argsort(-gpas)
        self.students = [self.students[i] for i in sorted_indices]


def prompt(stdscr, row, col, text):
    stdscr.addstr(row, col, text)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(row, col + len(text)).decode('utf-8').strip()
    curses.noecho()
    return val


def main(stdscr):
    system = Management()
    curses.curs_set(1)

    while True:
        stdscr.clear()
        stdscr.addstr(1, 0, "   STUDENT MARK MANAGEMENT")
        stdscr.addstr(3, 0, "1. Input Students")
        stdscr.addstr(4, 0, "2. Input Courses")
        stdscr.addstr(5, 0, "3. Input Marks for Course")
        stdscr.addstr(6, 0, "4. List Students (Sorted by GPA)")
        stdscr.addstr(7, 0, "5. List Courses")
        stdscr.addstr(8, 0, "6. Show Marks for Course")
        stdscr.addstr(9, 0, "0. Exit")

        choice = prompt(stdscr, 11, 0, "Select option (0-6): ")

        if choice == '1':
            stdscr.clear()
            num = int(prompt(stdscr, 0, 0, "Enter number of students: "))
            row = 2
            for i in range(num):
                stdscr.addstr(row, 0, f"Student {i+1}:")
                s_id = prompt(stdscr, row+1, 2, "ID: ")
                s_name = prompt(stdscr, row+2, 2, "Name: ")
                s_dob = prompt(stdscr, row+3, 2, "DoB: ")
                system.students.append(Student(s_id, s_name, s_dob))
                row += 5

        elif choice == '2':
            stdscr.clear()
            num = int(prompt(stdscr, 0, 0, "Enter number of courses: "))
            row = 2
            for i in range(num):
                stdscr.addstr(row, 0, f"Course {i+1}:")
                c_id = prompt(stdscr, row+1, 2, "ID: ")
                c_name = prompt(stdscr, row+2, 2, "Name: ")
                c_credits = int(prompt(stdscr, row+3, 2, "Credits: "))
                system.courses.append(Course(c_id, c_name, c_credits))
                row += 5

        elif choice == '3':
            stdscr.clear()
            c_id = prompt(stdscr, 0, 0, "Enter Course ID to input marks: ")
            if c_id not in system.marks:
                system.marks[c_id] = {}
            row = 2
            for s in system.students:
                raw_mark = float(prompt(stdscr, row, 0, f"Mark for {s.get_name()} ({s.get_id()}): "))
                system.marks[c_id][s.get_id()] = math.floor(raw_mark * 10) / 10.0
                row += 1

        elif choice == '4':
            stdscr.clear()
            system.sort_students_by_gpa()
            stdscr.addstr(0, 0, "STUDENT LIST")
            row = 2
            for idx, s in enumerate(system.students, 1):
                stdscr.addstr(row, 0, f"{idx}. {s}")
                row += 1
            prompt(stdscr, row + 1, 0, "Press Enter to return...")

        elif choice == '5':
            stdscr.clear()
            stdscr.addstr(0, 0, "COURSE LIST")
            row = 2
            for idx, c in enumerate(system.courses, 1):
                stdscr.addstr(row, 0, f"{idx}. {c}")
                row += 1
            prompt(stdscr, row + 1, 0, "Press Enter to return")

        elif choice == '6':
            stdscr.clear()
            c_id = prompt(stdscr, 0, 0, "Enter Course ID: ")
            stdscr.clear()
            stdscr.addstr(0, 0, f"MARKS FOR COURSE: {c_id}")
            row = 2
            if c_id in system.marks:
                for s in system.students:
                    m = system.marks[c_id].get(s.get_id(), "N/A")
                    stdscr.addstr(row, 0, f"ID: {s.get_id()} | Name: {s.get_name()} | Mark: {m}")
                    row += 1
            prompt(stdscr, row + 1, 0, "Press Enter to return")

        elif choice == '0':
            break


if __name__ == "__main__":
    curses.wrapper(main)