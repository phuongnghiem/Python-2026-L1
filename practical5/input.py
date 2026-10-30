import curses
from domains import Student, Course
import output as out_mod


def get_input_str(stdscr, prompt, y, x):
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    curses.echo()
    input_bytes = stdscr.getstr(y, x + len(prompt))
    curses.noecho()
    return input_bytes.decode('utf-8').strip()


def input_students(stdscr, students):
    out_mod.draw_header(stdscr, "INPUT STUDENTS")
    num_str = get_input_str(stdscr, "Enter number of students: ", 3, 2)
    try:
        num = int(num_str)
        for i in range(num):
            stdscr.addstr(5 + i * 4, 2, f"--- Student {i + 1} ---", curses.A_BOLD)
            sid = get_input_str(stdscr, "ID: ", 6 + i * 4, 2)
            sname = get_input_str(stdscr, "Name: ", 7 + i * 4, 2)
            sdob = get_input_str(stdscr, "DoB (DD/MM/YYYY): ", 8 + i * 4, 2)
            students.append(Student(sid, sname, sdob))
        out_mod.display_message(stdscr, "Students added successfully!")
    except ValueError:
        out_mod.display_message(stdscr, "Invalid number entered.")


def input_courses(stdscr, courses):
    out_mod.draw_header(stdscr, "INPUT COURSES")
    num_str = get_input_str(stdscr, "Enter number of courses: ", 3, 2)
    try:
        num = int(num_str)
        for i in range(num):
            stdscr.addstr(5 + i * 4, 2, f"--- Course {i + 1} ---", curses.A_BOLD)
            cid = get_input_str(stdscr, "Course ID: ", 6 + i * 4, 2)
            cname = get_input_str(stdscr, "Course Name: ", 7 + i * 4, 2)
            credit = float(get_input_str(stdscr, "Credits: ", 8 + i * 4, 2))
            courses[cid] = Course(cid, cname, credit)
        out_mod.display_message(stdscr, "Courses added successfully!")
    except ValueError:
        out_mod.display_message(stdscr, "Invalid input value.")


def input_marks(stdscr, students, courses):
    out_mod.draw_header(stdscr, "INPUT MARKS")
    if not courses:
        out_mod.display_message(stdscr, "No courses available. Please add courses first.")
        return
    if not students:
        out_mod.display_message(stdscr, "No students available. Please add students first.")
        return

    cid = get_input_str(stdscr, "Enter Course ID to input marks for: ", 3, 2)
    if cid not in courses:
        out_mod.display_message(stdscr, f"Course ID '{cid}' not found.")
        return

    y_offset = 5
    for student in students:
        mark_str = get_input_str(
            stdscr, f"Mark for {student.name} ({student.id}): ", y_offset, 2
        )
        try:
            raw_mark = float(mark_str)
            student.add_mark(cid, raw_mark)
        except ValueError:
            student.add_mark(cid, 0.0)
        y_offset += 1

    out_mod.display_message(stdscr, "Marks recorded successfully!")