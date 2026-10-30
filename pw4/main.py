import curses
import input as in_mod
import output as out_mod


def main_curses(stdscr):
    curses.curs_set(1)
    students = []
    courses = {}

    while True:
        out_mod.draw_header(stdscr, "STUDENT MARK MANAGEMENT SYSTEM (PW4)")
        stdscr.addstr(3, 4, "1. Input Student Information")
        stdscr.addstr(4, 4, "2. Input Course Information")
        stdscr.addstr(5, 4, "3. Input Marks for Course")
        stdscr.addstr(6, 4, "4. List Courses")
        stdscr.addstr(7, 4, "5. List Students & Calculated GPAs (Sorted Descending)")
        stdscr.addstr(8, 4, "6. Exit")

        choice = in_mod.get_input_str(stdscr, "Select an option (1-6): ", 10, 4)

        if choice == '1':
            in_mod.input_students(stdscr, students)
        elif choice == '2':
            in_mod.input_courses(stdscr, courses)
        elif choice == '3':
            in_mod.input_marks(stdscr, students, courses)
        elif choice == '4':
            out_mod.display_courses(stdscr, courses)
        elif choice == '5':
            out_mod.display_students_gpa(stdscr, students, courses)
        elif choice == '6':
            break


def main():
    curses.wrapper(main_curses)


if __name__ == "__main__":
    main()