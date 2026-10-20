"""Curses output helpers."""
import curses

TITLE, HEAD, OK, WARN = 1, 2, 3, 4


def move(win, y, x):
    """Move cursor; ignore errors when the terminal window is too small."""
    try:
        win.move(y, x)
    except curses.error:
        pass


def init(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(TITLE, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(HEAD, curses.COLOR_CYAN, -1)
    curses.init_pair(OK, curses.COLOR_GREEN, -1)
    curses.init_pair(WARN, curses.COLOR_YELLOW, -1)


def put(win, y, x, text, attr=0):
    try:
        win.addstr(y, x, text, attr)
    except curses.error:
        pass


def title(win, text):
    win.clear()
    _, w = win.getmaxyx()
    put(win, 0, 0, f" {text} ".ljust(w - 1), curses.color_pair(TITLE) | curses.A_BOLD)
    move(win, 2, 0)
    return 2


def message(win, text, color=OK):
    y, _ = win.getyx()
    put(win, y + 1, 0, text, curses.color_pair(color))
    move(win, y + 2, 0)


def wait_key(win):
    y, _ = win.getyx()
    put(win, y + 1, 0, "Press any key to continue...", curses.A_DIM)
    win.refresh()
    curses.napms(300)   # let a stray Enter (typed right after the menu key) arrive...
    curses.flushinp()   # ...and throw it away, so the table stays on screen
    win.getch()


def table(win, headers, rows, widths):
    y, _ = win.getyx()
    x = 0
    for h, w in zip(headers, widths):
        put(win, y, x, h.ljust(w), curses.color_pair(HEAD) | curses.A_BOLD)
        x += w
    for i, row in enumerate(rows, 1):
        x = 0
        for cell, w in zip(row, widths):
            put(win, y + i, x, str(cell).ljust(w))
            x += w
    move(win, y + len(rows) + 1, 0)


def show_menu(win, items):
    title(win, "STUDENT MARK MANAGEMENT")
    y = 2
    for key, label in items:
        put(win, y, 2, f"[{key}]", curses.color_pair(WARN) | curses.A_BOLD)
        put(win, y, 8, label)
        y += 1
    put(win, y + 1, 2, "Choose: ")
    return win.getkey()


def show_students(win, school):
    title(win, "STUDENTS")
    rows = [(s.id, s.name, s.dob, f"{s.gpa(school.courses):.2f}") for s in school.students]
    table(win, ["ID", "Name", "DoB", "GPA"], rows, [10, 25, 14, 8])
    wait_key(win)


def show_courses(win, school):
    title(win, "COURSES")
    rows = [(c.id, c.name, c.credits) for c in school.courses.values()]
    table(win, ["ID", "Name", "Credits"], rows, [10, 30, 8])
    wait_key(win)


def show_course_marks(win, school, cid):
    title(win, f"MARKS - {school.courses[cid].name}")
    rows = [(s.id, s.name, s.marks.get(cid, "-")) for s in school.students]
    table(win, ["ID", "Name", "Mark"], rows, [10, 25, 8])
    wait_key(win)


def show_ranking(win, school):
    school.sort_by_gpa()
    title(win, "GPA RANKING (descending)")
    rows = [(i, s.id, s.name, f"{s.gpa(school.courses):.2f}")
            for i, s in enumerate(school.students, 1)]
    table(win, ["#", "ID", "Name", "GPA"], rows, [5, 10, 25, 8])
    wait_key(win)