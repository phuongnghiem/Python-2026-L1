import curses
import input as input_module
import output as output_module

# Khởi tạo hai từ điển dữ liệu toàn cục để quản lý sinh viên và khóa học
students = {}
courses = {}

def main_menu(stdscr):
    """Menu chính điều khiển ứng dụng bằng Curses"""
    curses.curs_set(1)

    while True:
        stdscr.clear()
        stdscr.border(0)

        stdscr.addstr(1, 2, "================================================", curses.A_BOLD)
        stdscr.addstr(2, 2, "    HE THONG QUAN LY DIEM SINH VIEN (PW4)       ", curses.A_BOLD)
        stdscr.addstr(3, 2, "================================================", curses.A_BOLD)

        stdscr.addstr(5, 4, "1. Nhap thong tin Sinh vien")
        stdscr.addstr(6, 4, "2. Nhap thong tin Khoa hoc (Bao gom so Tin chi)")
        stdscr.addstr(7, 4, "3. Nhap diem mon hoc (Lam tron xuong bang math.floor)")
        stdscr.addstr(8, 4, "4. Hien thi danh sach Sinh vien (Sap xep theo GPA giam dan)")
        stdscr.addstr(9, 4, "5. Hien thi danh sach Khoa hoc")
        stdscr.addstr(10, 4, "6. Hien thi Bang diem theo mon hoc")
        stdscr.addstr(11, 4, "0. Thoat chuong trinh")

        stdscr.addstr(13, 2, "------------------------------------------------")
        choice = input_module.input_str(stdscr, 14, 2, "Vui long chon chuc nang (0-6): ")

        if choice == '1':
            input_module.add_students(stdscr, students)
        elif choice == '2':
            input_module.add_courses(stdscr, courses)
        elif choice == '3':
            input_module.input_marks(stdscr, students, courses)
        elif choice == '4':
            output_module.list_students(stdscr, students, courses)
        elif choice == '5':
            output_module.list_courses(stdscr, courses)
        elif choice == '6':
            output_module.show_marks(stdscr, students, courses)
        elif choice == '0':
            break

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()