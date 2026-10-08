import curses


def display_notification(stdscr, message: str):
    """Hiển thị thông báo trạng thái và chờ nhấn phím."""
    stdscr.clear()
    stdscr.addstr(2, 2, message, curses.A_BOLD)
    stdscr.addstr(4, 2, "Nhan phim bat ky de quay lai menu...")
    stdscr.refresh()
    stdscr.getch()


def display_menu(stdscr, num_students: int, num_courses: int) -> bool:
    """Hiển thị menu chính, trả về False nếu kích thước màn hình quá nhỏ."""
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    if max_y < 16 or max_x < 55:
        stdscr.addstr(0, 0, "Terminal qua nho! Vui long keo rong terminal de tiep tuc.")
        stdscr.refresh()
        stdscr.getch()
        return False

    stdscr.addstr(1, 2, "==========================================", curses.A_BOLD)
    stdscr.addstr(2, 2, "       CHUONG TRINH QUAN LY DIEM (PW4)    ", curses.A_BOLD)
    stdscr.addstr(3, 2, "==========================================", curses.A_BOLD)
    stdscr.addstr(4, 2, f"Hien co: {num_students} sinh vien | {num_courses} mon hoc")
    stdscr.addstr(6, 4, "1. Nhap danh sach sinh vien")
    stdscr.addstr(7, 4, "2. Nhap danh sach mon hoc (kem tin chi)")
    stdscr.addstr(8, 4, "3. Nhap diem mon hoc cho sinh vien")
    stdscr.addstr(9, 4, "4. Xem danh sach sinh vien va GPA giam dan")
    stdscr.addstr(10, 4, "5. Thoat")
    stdscr.addstr(12, 2, "Chon chuc nang (1-5): ")
    stdscr.refresh()
    return True


def display_students_gpa(stdscr, students: list):
    """Hiển thị bảng danh sách sinh viên sắp xếp theo GPA giảm dần."""
    stdscr.clear()
    stdscr.addstr(1, 2, "=== DANH SACH SINH VIEN SAP XEP THEO GPA GIAM DAN ===", curses.A_BOLD)
    stdscr.addstr(3, 2, f"{'ID':<10} {'Ho va ten':<25} {'Ngay sinh':<15} {'GPA':<6}", curses.A_UNDERLINE)

    row = 4
    for s in students:
        stdscr.addstr(row, 2, f"{s.id:<10} {s.name:<25} {s.dob:<15} {s.gpa:<6.2f}")
        row += 1

    stdscr.addstr(row + 2, 2, "Nhan phim bat ky de quay lai menu...")
    stdscr.refresh()
    stdscr.getch()