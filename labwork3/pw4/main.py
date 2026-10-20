import curses

import input as inp
import output
from domains import School

MENU = [
    ("1", "Add students"),
    ("2", "Add courses"),
    ("3", "Enter marks for a course"),
    ("4", "List students (with GPA)"),
    ("5", "List courses"),
    ("6", "Show marks of a course"),
    ("7", "GPA ranking (sorted descending)"),
    ("0", "Exit"),
]


def run(stdscr):
    curses.curs_set(0)
    output.init(stdscr)
    school = School()
    while True:
        key = output.show_menu(stdscr, MENU)
        if key == "0":
            break
        elif key == "1":
            inp.input_students(stdscr, school)
        elif key == "2":
            inp.input_courses(stdscr, school)
        elif key == "3":
            inp.input_marks(stdscr, school)
        elif key == "4":
            output.show_students(stdscr, school)
        elif key == "5":
            output.show_courses(stdscr, school)
        elif key == "6":
            output.title(stdscr, "SHOW MARKS")
            cid = inp.choose_course(stdscr, school)
            if cid:
                output.show_course_marks(stdscr, school, cid)
        elif key == "7":
            output.show_ranking(stdscr, school)


if __name__ == "__main__":
    curses.wrapper(run)
