"""Curses input helpers."""
import curses
import math

import output
import storage
from domains import Course, Student


def ask(win, prompt):
    y, _ = win.getyx()
    output.put(win, y, 0, prompt)
    curses.flushinp()  # drop stray keys (e.g. Enter pressed after a menu choice)
    curses.echo()
    curses.curs_set(1)
    text = win.getstr().decode().strip()
    curses.noecho()
    curses.curs_set(0)
    return text


def ask_int(win, prompt, minimum=0):
    while True:
        try:
            n = int(ask(win, prompt))
            if n >= minimum:
                return n
        except ValueError:
            pass
        output.message(win, "Invalid number, try again.", output.WARN)


def ask_mark(win, prompt):
    """Read a mark in [0, 20] and round DOWN to 1 decimal with math.floor."""
    while True:
        try:
            m = float(ask(win, prompt))
            if 0 <= m <= 20:
                return math.floor(m * 10) / 10
        except ValueError:
            pass
        output.message(win, "Mark must be a number between 0 and 20.", output.WARN)


def ask_new_id(win, prompt, exists):
    """Ask for an ID until it is not empty and not already used."""
    while True:
        value = ask(win, prompt)
        if value and not exists(value):
            return value
        output.message(win, "ID is empty or already used, try again.", output.WARN)


def input_students(win, school):
    output.title(win, "ADD STUDENTS")
    n = ask_int(win, "Number of students: ", 1)
    for i in range(1, n + 1):
        output.message(win, f"Student {i}", output.HEAD)
        sid = ask_new_id(win, "  ID: ", lambda v: school.find_student(v) is not None)
        name = ask(win, "  Name: ")
        dob = ask(win, "  DoB: ")
        school.add_student(Student(sid, name, dob))
    storage.write_students(school)


def input_courses(win, school):
    output.title(win, "ADD COURSES")
    n = ask_int(win, "Number of courses: ", 1)
    for i in range(1, n + 1):
        output.message(win, f"Course {i}", output.HEAD)
        cid = ask_new_id(win, "  ID: ", lambda v: v.lower() in [c.lower() for c in school.courses])
        name = ask(win, "  Name: ")
        credits = ask_int(win, "  Credits: ", 1)
        school.add_course(Course(cid, name, credits))
    storage.write_courses(school)


def choose_course(win, school):
    """Show available courses, then read a course ID (case-insensitive)."""
    y, _ = win.getyx()
    output.put(win, y, 0, "Available courses:", curses.color_pair(output.HEAD))
    for i, c in enumerate(school.courses.values(), 1):
        output.put(win, y + i, 2, f"{c.id} - {c.name}")
    output.move(win, y + len(school.courses) + 1, 0)
    typed = ask(win, "Course ID: ").lower()
    for cid in school.courses:
        if cid.lower() == typed:
            return cid
    output.message(win, "No such course.", output.WARN)
    output.wait_key(win)
    return None


def input_marks(win, school):
    output.title(win, "ENTER MARKS")
    if not school.courses or not school.students:
        output.message(win, "Add students and courses first.", output.WARN)
        output.wait_key(win)
        return
    cid = choose_course(win, school)
    if cid is None:
        return
    for s in school.students:
        s.set_mark(cid, ask_mark(win, f"  Mark of {s.name} ({s.id}): "))
    storage.write_marks(school)
    output.message(win, f"Marks saved for {school.courses[cid].name}.", output.OK)
    output.wait_key(win)
