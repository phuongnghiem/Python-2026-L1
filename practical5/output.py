import curses


def draw_header(stdscr, title):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, f"=== {title} ===", curses.A_BOLD | curses.A_UNDERLINE)


def display_message(stdscr, message, y=18, x=2):
    stdscr.addstr(y, x, message, curses.A_BOLD)
    stdscr.addstr(y + 1, x, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


def display_courses(stdscr, courses):
    draw_header(stdscr, "COURSE LIST")
    if not courses:
        stdscr.addstr(3, 2, "No courses found.")
    else:
        stdscr.addstr(3, 2, f"{'ID':<10} {'Course Name':<25} {'Credits':<10}", curses.A_BOLD)
        row = 4
        for c in courses.values():
            stdscr.addstr(row, 2, f"{c.id:<10} {c.name:<25} {c.credit:<10.1f}")
            row += 1
    display_message(stdscr, "", y=18, x=2)


def display_students_gpa(stdscr, students, courses):
    draw_header(stdscr, "STUDENT GPA LIST (SORTED DESCENDING)")
    if not students:
        stdscr.addstr(3, 2, "No students found.")
    else:
        for s in students:
            s.calculate_gpa(courses)
        students.sort(key=lambda s: s.gpa, reverse=True)

        stdscr.addstr(3, 2, f"{'ID':<10} {'Name':<20} {'DoB':<12} {'GPA':<8}", curses.A_BOLD)
        row = 4
        for student in students:
            stdscr.addstr(
                row, 2,
                f"{student.id:<10} {student.name:<20} {student.dob:<12} {student.gpa:<8.2f}"
            )
            row += 1
    display_message(stdscr, "", y=18, x=2)