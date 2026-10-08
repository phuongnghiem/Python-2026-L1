import curses

def list_students(stdscr, students, courses):
    """Chức năng hiển thị danh sách sinh viên sắp xếp theo GPA giảm dần"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== DANH SACH SINH VIEN (SAP XEP THEO GPA GIAM DAN) ===", curses.A_BOLD)

    if not students:
        stdscr.addstr(3, 2, "Chua co du lieu sinh vien! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    # Cập nhật GPA mới nhất
    for student in students.values():
        student.calculate_gpa(courses)

    # Sắp xếp danh sách sinh viên theo điểm GPA giảm dần
    student_list = list(students.values())
    student_list.sort(key=lambda s: s.gpa, reverse=True)

    row = 3
    stdscr.addstr(row, 2, f"{'STT':<5} | {'MA SV':<10} | {'HO VA TEN':<20} | {'NGAY SINH':<12} | {'GPA':<6}", curses.A_REVERSE)
    row += 1

    for idx, student in enumerate(student_list, start=1):
        line = f"{idx:<5} | {student.id:<10} | {student.name:<20} | {student.dob:<12} | {student.gpa:<6.2f}"
        stdscr.addstr(row, 2, line)
        row += 1

        if row > curses.LINES - 3:
            stdscr.addstr(row, 2, "--- Nhan phim bat ky de xem trang tiep ---")
            stdscr.getch()
            stdscr.clear()
            stdscr.border(0)
            row = 2

    stdscr.addstr(row + 1, 2, "Nhan phim bat ky de quay lai Menu chinh...")
    stdscr.getch()

def list_courses(stdscr, courses):
    """Chức năng hiển thị danh sách các khóa học"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== DANH SACH KHOA HOC ===", curses.A_BOLD)

    if not courses:
        stdscr.addstr(3, 2, "Chua co du lieu khoa hoc! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    row = 3
    stdscr.addstr(row, 2, f"{'STT':<5} | {'MA MON':<10} | {'TEN MON HOC':<30} | {'TIN CHI':<10}", curses.A_REVERSE)
    row += 1

    for idx, course in enumerate(courses.values(), start=1):
        line = f"{idx:<5} | {course.id:<10} | {course.name:<30} | {course.credits:<10.1f}"
        stdscr.addstr(row, 2, line)
        row += 1

    stdscr.addstr(row + 1, 2, "Nhan phim bat ky de quay lai Menu chinh...")
    stdscr.getch()

def show_marks(stdscr, students, courses):
    """Chức năng hiển thị bảng điểm theo môn học"""
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== BANG DIEM THEO MON HOC ===", curses.A_BOLD)

    if not courses:
        stdscr.addstr(3, 2, "Chua co du lieu khoa hoc! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    from input import input_str
    c_id = input_str(stdscr, 3, 2, "Nhap Ma mon hoc muon xem diem: ")
    if c_id not in courses:
        stdscr.addstr(5, 2, "Khoa hoc khong ton tai! Bam phim bat ky de quay lai...")
        stdscr.getch()
        return

    course = courses[c_id]
    row = 5
    stdscr.addstr(row, 2, f"BANG DIEM MON: {course.name} ({course.id}) - Tin chi: {course.credits}", curses.A_UNDERLINE)
    row += 2

    stdscr.addstr(row, 2, f"{'MA SV':<10} | {'HO VA TEN':<20} | {'DIEM (DA LAM TRON DOWN)':<25}", curses.A_REVERSE)
    row += 1

    has_mark = False
    for student in students.values():
        if c_id in student.marks:
            has_mark = True
            mark_val = student.marks[c_id]
            stdscr.addstr(row, 2, f"{student.id:<10} | {student.name:<20} | {mark_val:<25.1f}")
            row += 1

    if not has_mark:
        stdscr.addstr(row, 2, "Chua co sinh vien nao co diem mon nay!")
        row += 1

    stdscr.addstr(row + 1, 2, "Nhan phim bat ky de quay lai Menu chinh...")
    stdscr.getch()