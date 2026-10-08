import math
import curses
from domains import Student, Course

def input_str(stdscr, row, col, prompt):
    """Hàm phụ trợ nhập chuỗi trực tiếp trên curses terminal"""
    curses.echo()                  # Bật hiển thị ký tự người dùng gõ
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()
    input_bytes = stdscr.getstr(row, col + len(prompt))
    curses.noecho()                # Tắt hiển thị ký tự tự do
    return input_bytes.decode('utf-8').strip()

def add_students(stdscr, students):
    """Chức năng nhập danh sách sinh viên mới"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== NHAP DU LIEU SINH VIEN ===", curses.A_BOLD)

    try:
        num_str = input_str(stdscr, 3, 2, "Nhap so luong sinh vien muon them: ")
        num_students = int(num_str)
    except ValueError:
        stdscr.addstr(5, 2, "So luong khong hop le! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    current_row = 5
    for i in range(num_students):
        stdscr.addstr(current_row, 2, f"--- Sinh vien thu {i+1} ---", curses.A_UNDERLINE)
        s_id = input_str(stdscr, current_row + 1, 2, "Ma sinh vien (ID): ")
        s_name = input_str(stdscr, current_row + 2, 2, "Ho va ten: ")
        s_dob = input_str(stdscr, current_row + 3, 2, "Ngay sinh (DoB): ")

        student = Student(s_id, s_name, s_dob)
        students[s_id] = student
        current_row += 5

        if current_row > curses.LINES - 6:
            stdscr.clear()
            stdscr.border(0)
            current_row = 2

    stdscr.addstr(current_row + 1, 2, "Them sinh vien thanh cong! Bam phim bat ky...")
    stdscr.getch()

def add_courses(stdscr, courses):
    """Chức năng nhập danh sách khóa học mới"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== NHAP DU LIEU KHOA HOC ===", curses.A_BOLD)

    try:
        num_str = input_str(stdscr, 3, 2, "Nhap so luong khoa hoc muon them: ")
        num_courses = int(num_str)
    except ValueError:
        stdscr.addstr(5, 2, "So luong khong hop le! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    current_row = 5
    for i in range(num_courses):
        stdscr.addstr(current_row, 2, f"--- Khoa hoc thu {i+1} ---", curses.A_UNDERLINE)
        c_id = input_str(stdscr, current_row + 1, 2, "Ma khoa hoc (ID): ")
        c_name = input_str(stdscr, current_row + 2, 2, "Ten khoa hoc: ")
        try:
            c_credits = float(input_str(stdscr, current_row + 3, 2, "So tin chi (Credits): "))
        except ValueError:
            c_credits = 1.0

        course = Course(c_id, c_name, c_credits)
        courses[c_id] = course
        current_row += 5

        if current_row > curses.LINES - 6:
            stdscr.clear()
            stdscr.border(0)
            current_row = 2

    stdscr.addstr(current_row + 1, 2, "Them khoa hoc thanh cong! Bam phim bat ky...")
    stdscr.getch()

def input_marks(stdscr, students, courses):
    """Chức năng nhập điểm và làm tròn xuống 1 chữ số thập phân bằng math.floor"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== NHAP DIEM SINH VIEN ===", curses.A_BOLD)

    if not courses:
        stdscr.addstr(3, 2, "Chua co khoa hoc nao! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return
    if not students:
        stdscr.addstr(3, 2, "Chua co sinh vien nao! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    c_id = input_str(stdscr, 3, 2, "Nhap Ma mon hoc muon nhap diem: ")
    if c_id not in courses:
        stdscr.addstr(5, 2, "Ma khoa hoc khong ton tai! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    current_row = 5
    course = courses[c_id]
    stdscr.addstr(current_row, 2, f"Nhap diem mon: {course.name} (So tin chi: {course.credits})", curses.A_UNDERLINE)
    current_row += 2

    for student_id, student in students.items():
        while True:
            try:
                mark_str = input_str(stdscr, current_row, 2, f"Diem cua SV {student.name} ({student.id}): ")
                raw_mark = float(mark_str)

                # Sử dụng math.floor làm tròn xuống 1 chữ số thập phân
                rounded_mark = math.floor(raw_mark * 10.0) / 10.0
                student.add_mark(c_id, rounded_mark)
                current_row += 1
                break
            except ValueError:
                stdscr.addstr(current_row + 1, 2, "Diem khong hop le, vui long nhap lai so!")
                current_row += 2

        if current_row > curses.LINES - 4:
            stdscr.clear()
            stdscr.border(0)
            current_row = 2

    # Tự động cập nhật lại GPA cho tất cả sinh viên
    for student in students.values():
        student.calculate_gpa(courses)

    stdscr.addstr(current_row + 1, 2, "Nhap diem thanh cong va da tinh lai GPA! Bam phim bat ky...")
    stdscr.getch()