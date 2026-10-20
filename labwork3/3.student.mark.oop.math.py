"""Practical work 3: math (floor), numpy (GPA + sort), curses (UI). Single file."""
import curses
import math

import numpy as np


# ---------- Classes ----------
class Course:
    def __init__(self, cid, name, credits):
        self.id = cid
        self.name = name
        self.credits = credits


class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> mark

    def gpa(self, courses):
        """Weighted sum of credits and marks, using numpy arrays."""
        ids = [c for c in self.marks if c in courses]
        if not ids:
            return 0.0
        marks = np.array([self.marks[c] for c in ids])
        credits = np.array([courses[c].credits for c in ids])
        return float(np.sum(marks * credits) / np.sum(credits))


class School:
    def __init__(self):
        self.students = []
        self.courses = {}

    def sort_by_gpa(self):
        """Sort student list by GPA, descending."""
        if not self.students:
            return
        gpas = np.array([s.gpa(self.courses) for s in self.students])
        order = np.argsort(-gpas, kind="stable")
        self.students = [self.students[i] for i in order]


# ---------- Curses helpers ----------
def move(win, y, x):
    """Move cursor; ignore errors when the terminal window is too small."""
    try:
        win.move(y, x)
    except curses.error:
        pass


def put(win, y, x, text, attr=0):
    try:
        win.addstr(y, x, text, attr)
    except curses.error:
        pass


def title(win, text):
    win.clear()
    _, w = win.getmaxyx()
    put(win, 0, 0, f" {text} ".ljust(w - 1), curses.color_pair(1) | curses.A_BOLD)
    move(win, 2, 0)


def ask(win, prompt):
    y, _ = win.getyx()
    put(win, y, 0, prompt)
    curses.flushinp()  # drop stray keys (e.g. Enter pressed after a menu choice)
    curses.echo()
    curses.curs_set(1)
    text = win.getstr().decode().strip()
    curses.noecho()
    curses.curs_set(0)
    return text


def ask_int(win, prompt, minimum=1):
    while True:
        try:
            n = int(ask(win, prompt))
            if n >= minimum:
                return n
        except ValueError:
            pass
        put(win, win.getyx()[0], 0, "Invalid number.", curses.color_pair(4))
        move(win, win.getyx()[0] + 1, 0)


def ask_mark(win, prompt):
    """Read mark in [0, 20], round DOWN to 1 decimal with math.floor()."""
    while True:
        try:
            m = float(ask(win, prompt))
            if 0 <= m <= 20:
                return math.floor(m * 10) / 10
        except ValueError:
            pass
        put(win, win.getyx()[0], 0, "Mark must be 0-20.", curses.color_pair(4))
        move(win, win.getyx()[0] + 1, 0)


def table(win, headers, rows, widths):
    y, _ = win.getyx()
    x = 0
    for h, w in zip(headers, widths):
        put(win, y, x, h.ljust(w), curses.color_pair(2) | curses.A_BOLD)
        x += w
    for i, row in enumerate(rows, 1):
        x = 0
        for cell, w in zip(row, widths):
            put(win, y + i, x, str(cell).ljust(w))
            x += w
    move(win, y + len(rows) + 1, 0)


def pause(win):
    put(win, win.getyx()[0] + 1, 0, "Press any key...", curses.A_DIM)
    win.refresh()
    curses.napms(300)   # let a stray Enter (typed right after the menu key) arrive...
    curses.flushinp()   # ...and throw it away, so the table stays on screen
    win.getch()


# ---------- Actions ----------
def add_students(win, sc):
    title(win, "ADD STUDENTS")
    for i in range(1, ask_int(win, "Number of students: ") + 1):
        put(win, win.getyx()[0], 0, f"Student {i}", curses.color_pair(2))
        move(win, win.getyx()[0] + 1, 0)
        sc.students.append(Student(ask(win, "  ID: "), ask(win, "  Name: "), ask(win, "  DoB: ")))


def add_courses(win, sc):
    title(win, "ADD COURSES")
    for i in range(1, ask_int(win, "Number of courses: ") + 1):
        put(win, win.getyx()[0], 0, f"Course {i}", curses.color_pair(2))
        move(win, win.getyx()[0] + 1, 0)
        cid, name = ask(win, "  ID: "), ask(win, "  Name: ")
        sc.courses[cid] = Course(cid, name, ask_int(win, "  Credits: "))


def pick_course(win, sc):
    """Show available courses, then read a course ID (case-insensitive)."""
    put(win, win.getyx()[0], 0, "Available courses:", curses.color_pair(2))
    move(win, win.getyx()[0] + 1, 0)
    for c in sc.courses.values():
        put(win, win.getyx()[0], 2, f"{c.id} - {c.name}")
        move(win, win.getyx()[0] + 1, 0)
    typed = ask(win, "Course ID: ").lower()
    for cid in sc.courses:
        if cid.lower() == typed:
            return cid
    put(win, win.getyx()[0], 0, "No such course.", curses.color_pair(4))
    move(win, win.getyx()[0] + 1, 0)
    pause(win)
    return None


def enter_marks(win, sc):
    title(win, "ENTER MARKS")
    if not sc.courses or not sc.students:
        put(win, 2, 0, "Add students and courses first.", curses.color_pair(4))
        move(win, 3, 0)
        pause(win)
        return
    cid = pick_course(win, sc)
    if cid is None:
        return
    for s in sc.students:
        s.marks[cid] = ask_mark(win, f"  Mark of {s.name} ({s.id}): ")
    move(win, win.getyx()[0] + 1, 0)
    put(win, win.getyx()[0], 0, f"Marks saved for {sc.courses[cid].name}.", curses.color_pair(2))
    move(win, win.getyx()[0] + 1, 0)
    pause(win)


def list_students(win, sc):
    title(win, "STUDENTS")
    rows = [(s.id, s.name, s.dob, f"{s.gpa(sc.courses):.2f}") for s in sc.students]
    table(win, ["ID", "Name", "DoB", "GPA"], rows, [10, 25, 14, 8])
    pause(win)


def list_courses(win, sc):
    title(win, "COURSES")
    rows = [(c.id, c.name, c.credits) for c in sc.courses.values()]
    table(win, ["ID", "Name", "Credits"], rows, [10, 30, 8])
    pause(win)


def ranking(win, sc):
    sc.sort_by_gpa()
    title(win, "GPA RANKING (descending)")
    rows = [(i, s.id, s.name, f"{s.gpa(sc.courses):.2f}") for i, s in enumerate(sc.students, 1)]
    table(win, ["#", "ID", "Name", "GPA"], rows, [5, 10, 25, 8])
    pause(win)


MENU = [("1", "Add students"), ("2", "Add courses"), ("3", "Enter marks"),
        ("4", "List students (GPA)"), ("5", "List courses"),
        ("6", "GPA ranking (sorted)"), ("0", "Exit")]


def run(win):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(4, curses.COLOR_YELLOW, -1)
    sc = School()
    actions = {"1": add_students, "2": add_courses, "3": enter_marks,
               "4": list_students, "5": list_courses, "6": ranking}
    while True:
        title(win, "STUDENT MARK MANAGEMENT")
        for i, (k, label) in enumerate(MENU, 2):
            put(win, i, 2, f"[{k}]", curses.color_pair(4) | curses.A_BOLD)
            put(win, i, 8, label)
        put(win, len(MENU) + 3, 2, "Choose: ")
        key = win.getkey()
        if key == "0":
            break
        if key in actions:
            actions[key](win, sc)


if __name__ == "__main__":
    curses.wrapper(run)