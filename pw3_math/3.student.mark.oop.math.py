# Practical Work 3: Student Mark Management with math, numpy and curses

import math
import numpy as np
import curses
from curses import wrapper


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
    def __init__(self, course_id, name, credits=3):
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


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        # Round down to 1 decimal place using math.floor
        self.__mark = math.floor(mark * 10) / 10

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

    def input_students(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter number of students: ")
        stdscr.refresh()
        n = int(stdscr.getstr().decode())
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Student {i+1} ---")
            stdscr.addstr(1, 0, "Student ID: ")
            sid = stdscr.getstr().decode().strip()
            stdscr.addstr(2, 0, "Name: ")
            name = stdscr.getstr().decode().strip()
            stdscr.addstr(3, 0, "DoB (dd/mm/yyyy): ")
            dob = stdscr.getstr().decode().strip()
            self.__students.append(Student(sid, name, dob))
        curses.noecho()

    def input_courses(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter number of courses: ")
        stdscr.refresh()
        n = int(stdscr.getstr().decode())
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Course {i+1} ---")
            stdscr.addstr(1, 0, "Course ID: ")
            cid = stdscr.getstr().decode().strip()
            stdscr.addstr(2, 0, "Course name: ")
            name = stdscr.getstr().decode().strip()
            stdscr.addstr(3, 0, "Credits: ")
            credits = int(stdscr.getstr().decode().strip() or "3")
            self.__courses.append(Course(cid, name, credits))
        curses.noecho()

    def input_marks(self, stdscr):
        if not self.__courses:
            return
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "Available courses:")
        for idx, c in enumerate(self.__courses):
            stdscr.addstr(idx + 1, 0, f"  {c.get_id()}: {c.get_name()}")
        stdscr.addstr(len(self.__courses) + 2, 0, "Select course ID: ")
        cid = stdscr.getstr().decode().strip()
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            return
        for i, s in enumerate(self.__students):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Mark for {s.get_name()} ({s.get_id()}) in {course.get_name()}: ")
            m = float(stdscr.getstr().decode())
            self.__marks.append(Mark(s.get_id(), cid, m))
        curses.noecho()

    def calculate_gpa(self, student_id):
        """Calculate weighted GPA using numpy"""
        student_marks = []
        credits = []
        for m in self.__marks:
            if m.get_student_id() == student_id:
                course = next((c for c in self.__courses if c.get_id() == m.get_course_id()), None)
                if course:
                    student_marks.append(m.get_mark())
                    credits.append(course.get_credits())
        if not student_marks:
            return 0.0
        marks_arr = np.array(student_marks)
        credits_arr = np.array(credits)
        gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        return round(gpa, 1)

    def update_all_gpa(self):
        for s in self.__students:
            gpa = self.calculate_gpa(s.get_id())
            s.set_gpa(gpa)

    def sort_by_gpa(self):
        self.update_all_gpa()
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_students(self, stdscr):
        self.update_all_gpa()
        stdscr.clear()
        stdscr.addstr(0, 0, "=== Students (sorted by GPA desc) ===")
        self.sort_by_gpa()
        for i, s in enumerate(self.__students):
            stdscr.addstr(i + 2, 0, str(s))
        stdscr.addstr(len(self.__students) + 3, 0, "Press any key to continue...")
        stdscr.getch()

    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "=== Courses ===")
        for i, c in enumerate(self.__courses):
            stdscr.addstr(i + 2, 0, str(c))
        stdscr.addstr(len(self.__courses) + 3, 0, "Press any key to continue...")
        stdscr.getch()

    def show_marks(self, stdscr):
        if not self.__courses:
            return
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "Available courses:")
        for idx, c in enumerate(self.__courses):
            stdscr.addstr(idx + 1, 0, f"  {c.get_id()}: {c.get_name()}")
        stdscr.addstr(len(self.__courses) + 2, 0, "Select course ID: ")
        cid = stdscr.getstr().decode().strip()
        curses.noecho()
        course = next((c for c in self.__courses if c.get_id() == cid), None)
        if not course:
            return
        stdscr.clear()
        stdscr.addstr(0, 0, f"=== Marks for {course.get_name()} ===")
        for i, s in enumerate(self.__students):
            mark_obj = next(
                (m for m in self.__marks
                 if m.get_student_id() == s.get_id() and m.get_course_id() == cid),
                None
            )
            mark_val = mark_obj.get_mark() if mark_obj else "N/A"
            stdscr.addstr(i + 2, 0, f"{s.get_name()} ({s.get_id()}): {mark_val}")
        stdscr.addstr(len(self.__students) + 3, 0, "Press any key to continue...")
        stdscr.getch()

    def run(self, stdscr):
        curses.curs_set(0)
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "===== STUDENT MARK MANAGEMENT (Math + Curses) =====")
            stdscr.addstr(2, 0, "1. Input students")
            stdscr.addstr(3, 0, "2. Input courses")
            stdscr.addstr(4, 0, "3. Input marks for a course")
            stdscr.addstr(5, 0, "4. List students (sorted by GPA)")
            stdscr.addstr(6, 0, "5. List courses")
            stdscr.addstr(7, 0, "6. Show marks for a course")
            stdscr.addstr(8, 0, "0. Exit")
            stdscr.addstr(10, 0, "Your choice: ")
            stdscr.refresh()
            key = stdscr.getch()
            if key == ord("1"):
                self.input_students(stdscr)
            elif key == ord("2"):
                self.input_courses(stdscr)
            elif key == ord("3"):
                self.input_marks(stdscr)
            elif key == ord("4"):
                self.list_students(stdscr)
            elif key == ord("5"):
                self.list_courses(stdscr)
            elif key == ord("6"):
                self.show_marks(stdscr)
            elif key == ord("0"):
                break


def main(stdscr):
    app = StudentMarkManagement()
    app.run(stdscr)


if __name__ == "__main__":
    wrapper(main)
