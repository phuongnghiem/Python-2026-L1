"""Persistence: text files (students.txt, courses.txt, marks.txt) + students.dat archive."""
import csv
import os
import zipfile

from domains import Course, Student

# Always store files next to this script, whatever the current directory is.
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENTS_TXT = "students.txt"
COURSES_TXT = "courses.txt"
MARKS_TXT = "marks.txt"
ARCHIVE = "students.dat"
TXT_FILES = (STUDENTS_TXT, COURSES_TXT, MARKS_TXT)


def _path(name):
    return os.path.join(DATA_DIR, name)


def _write(name, rows):
    with open(_path(name), "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


def _read(name):
    path = _path(name)
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [row for row in csv.reader(f) if row]


# ---------- written right after each input ----------
def write_students(school):
    _write(STUDENTS_TXT, ([s.id, s.name, s.dob] for s in school.students))


def write_courses(school):
    _write(COURSES_TXT, ([c.id, c.name, c.credits] for c in school.courses.values()))


def write_marks(school):
    _write(MARKS_TXT, ([s.id, cid, mark] for s in school.students
                       for cid, mark in s.marks.items()))


# ---------- on exit: compress everything into students.dat ----------
def save(school):
    write_students(school)
    write_courses(school)
    write_marks(school)
    with zipfile.ZipFile(_path(ARCHIVE), "w", zipfile.ZIP_DEFLATED) as z:
        for name in TXT_FILES:
            z.write(_path(name), arcname=name)


# ---------- on start: decompress students.dat and load data ----------
def load(school):
    """Return True if data was loaded from students.dat."""
    if not os.path.exists(_path(ARCHIVE)):
        return False
    try:
        with zipfile.ZipFile(_path(ARCHIVE)) as z:
            z.extractall(DATA_DIR)
    except zipfile.BadZipFile:
        return False
    for sid, name, dob in _read(STUDENTS_TXT):
        school.add_student(Student(sid, name, dob))
    for cid, name, credits in _read(COURSES_TXT):
        school.add_course(Course(cid, name, int(credits)))
    for sid, cid, mark in _read(MARKS_TXT):
        student = school.find_student(sid)
        if student:
            student.set_mark(cid, float(mark))
    return True
