import curses
import math
import numpy as np


class Student:
    def __init__(self, student_id: str, name: str, dob: str):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Cấu trúc: {course_id: score}
        self.gpa = 0.0

    def calculate_gpa(self, courses_dict: dict) -> float:
        """Tính GPA có trọng số theo số tín chỉ bằng thư viện numpy."""
        marks_list = []
        credits_list = []

        for course_id, score in self.marks.items():
            if course_id in courses_dict:
                marks_list.append(score)
                credits_list.append(courses_dict[course_id].credits)

        if not marks_list or sum(credits_list) == 0:
            self.gpa = 0.0
            return 0.0

        # Sử dụng numpy array để tính tổng có trọng số
        marks_arr = np.array(marks_list, dtype=float)
        credits_arr = np.array(credits_list, dtype=float)

        weighted_sum = np.sum(marks_arr * credits_arr)
        total_credits = np.sum(credits_arr)
        self.gpa = float(weighted_sum / total_credits)
        return self.gpa


class Course:
    def __init__(self, course_id: str, name: str, credits: int):
        self.id = course_id
        self.name = name
        self.credits = credits


def round_down_score(score: float) -> float:
    """Làm tròn xuống 1 chữ số thập phân bằng math.floor()."""
    return math.floor(score * 10) / 10


def get_input(stdscr, prompt: str) -> str:
    """Hỗ trợ nhập dữ liệu dạng chuỗi qua giao diện curses."""
    stdscr.clear()
    stdscr.addstr(2, 2, prompt, curses.A_BOLD)
    curses.echo()
    stdscr.refresh()
    user_input = stdscr.getstr(3, 2).decode("utf-8").strip()
    curses.noecho()
    return user_input


def display_notification(stdscr, message: str):
    """Hiển thị thông báo trạng thái và chờ nhấn phím."""
    stdscr.clear()
    stdscr.addstr(2, 2, message, curses.A_BOLD)
    stdscr.addstr(4, 2, "Nhan phim bat ky de quay lai menu...")
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    # Khởi tạo giao diện curses
    curses.curs_set(0)

    students = []
    courses = {}  # {course_id: Course}

    while True:
        stdscr.clear()

        # Kiểm tra kích thước cửa sổ để tránh lỗi crash addwstr
        max_y, max_x = stdscr.getmaxyx()
        if max_y < 16 or max_x < 55:
            stdscr.addstr(0, 0, "Terminal qua nho! Vui long keo rong terminal de tiep tuc.")
            stdscr.refresh()
            stdscr.getch()
            continue

        stdscr.addstr(1, 2, "==========================================", curses.A_BOLD)
        stdscr.addstr(2, 2, "     CHUONG TRINH QUAN LY DIEM (LAB 3)    ", curses.A_BOLD)
        stdscr.addstr(3, 2, "==========================================", curses.A_BOLD)
        stdscr.addstr(4, 2, f"So luong: {len(students)} sinh vien | {len(courses)} mon hoc")
        stdscr.addstr(6, 4, "1. Nhap danh sach sinh vien")
        stdscr.addstr(7, 4, "2. Nhap danh sach mon hoc (kem tin chi)")
        stdscr.addstr(8, 4, "3. Nhap diem mon hoc cho sinh vien")
        stdscr.addstr(9, 4, "4. Xem danh sach sinh vien va GPA giam dan")
        stdscr.addstr(10, 4, "5. Thoat chuong trinh")
        stdscr.addstr(12, 2, "Chon chuc nang (1-5): ")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            num_str = get_input(stdscr, "Nhap so luong sinh vien: ")
            if num_str.isdigit():
                num = int(num_str)
                for i in range(num):
                    sid = get_input(stdscr, f"[{i + 1}/{num}] Nhap ma sinh vien (ID): ")
                    name = get_input(stdscr, f"[{i + 1}/{num}] Nhap ho ten sinh vien: ")
                    dob = get_input(stdscr, f"[{i + 1}/{num}] Nhap ngay sinh (YYYY-MM-DD): ")
                    students.append(Student(sid, name, dob))
                display_notification(stdscr, f"Them thanh cong {num} sinh vien!")
            else:
                display_notification(stdscr, "So luong nhap vao khong hop le!")

        elif key == ord('2'):
            num_str = get_input(stdscr, "Nhap so luong mon hoc: ")
            if num_str.isdigit():
                num = int(num_str)
                for i in range(num):
                    cid = get_input(stdscr, f"[{i + 1}/{num}] Nhap ma mon hoc (ID): ")
                    name = get_input(stdscr, f"[{i + 1}/{num}] Nhap ten mon hoc: ")
                    credits_str = get_input(stdscr, f"[{i + 1}/{num}] Nhap so tin chi: ")
                    credits = int(credits_str) if credits_str.isdigit() else 3
                    courses[cid] = Course(cid, name, credits)
                display_notification(stdscr, f"Them thanh cong {num} mon hoc!")
            else:
                display_notification(stdscr, "So luong nhap vao khong hop le!")

        elif key == ord('3'):
            if not courses:
                display_notification(stdscr, "Chua co mon hoc nao trong he thong!")
                continue
            if not students:
                display_notification(stdscr, "Chua co sinh vien nao trong he thong!")
                continue

            cid = get_input(stdscr, "Nhap ma mon hoc can vao diem: ")
            if cid not in courses:
                display_notification(stdscr, f"Khong tim thay mon hoc co ma: {cid}")
                continue

            for s in students:
                score_str = get_input(stdscr, f"Diem mon {courses[cid].name} cho SV {s.name} ({s.id}): ")
                try:
                    raw_score = float(score_str)
                    # Làm tròn điểm xuống 1 chữ số thập phân bằng math.floor
                    final_score = round_down_score(raw_score)
                    s.marks[cid] = final_score
                except ValueError:
                    s.marks[cid] = 0.0

            display_notification(stdscr, f"Nhap diem mon {courses[cid].name} hoan tat!")

        elif key == ord('4'):
            if not students:
                display_notification(stdscr, "Danh sach sinh vien hien dang trong!")
                continue

            # Tính lại điểm trung bình GPA cho từng sinh viên
            for s in students:
                s.calculate_gpa(courses)

            # Sắp xếp danh sách sinh viên theo thứ tự GPA giảm dần
            students.sort(key=lambda s: s.gpa, reverse=True)

            stdscr.clear()
            stdscr.addstr(1, 2, "=== DANH SACH SINH VIEN THEO GPA GIAM DAN ===", curses.A_BOLD)
            stdscr.addstr(3, 2, f"{'ID':<10} {'Ho va ten':<25} {'Ngay sinh':<15} {'GPA':<6}", curses.A_UNDERLINE)

            row = 4
            for s in students:
                stdscr.addstr(row, 2, f"{s.id:<10} {s.name:<25} {s.dob:<15} {s.gpa:<6.2f}")
                row += 1

            stdscr.addstr(row + 2, 2, "Nhan phim bat ky de quay lai menu...")
            stdscr.refresh()
            stdscr.getch()

        elif key == ord('5'):
            break


if __name__ == "__main__":
    curses.wrapper(main)