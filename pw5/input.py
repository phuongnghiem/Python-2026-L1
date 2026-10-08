import curses
import math
from domains.student import Student
from domains.course import Course


def round_down_score(score: float) -> float:
    """Làm tròn xuống 1 chữ số thập phân bằng math.floor."""
    return math.floor(score * 10) / 10


def get_str_input(stdscr, prompt: str) -> str:
    """Hàm phụ trợ hiển thị câu nhắc và nhận chuỗi ký tự từ bàn phím."""
    stdscr.clear()
    stdscr.addstr(2, 2, prompt, curses.A_BOLD)
    curses.echo()
    stdscr.refresh()
    user_input = stdscr.getstr(3, 2).decode("utf-8").strip()
    curses.noecho()
    return user_input


def input_students(stdscr) -> list:
    """Nhập danh sách sinh viên."""
    students = []
    num_str = get_str_input(stdscr, "Nhap so luong sinh vien: ")
    if num_str.isdigit():
        num = int(num_str)
        for i in range(num):
            sid = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap ma sinh vien (ID): ")
            name = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap ho ten sinh vien: ")
            dob = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap ngay sinh (YYYY-MM-DD): ")
            students.append(Student(sid, name, dob))
    return students


def input_courses(stdscr) -> dict:
    """Nhập danh sách môn học kèm số tín chỉ."""
    courses = {}
    num_str = get_str_input(stdscr, "Nhap so luong mon hoc: ")
    if num_str.isdigit():
        num = int(num_str)
        for i in range(num):
            cid = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap ma mon hoc (ID): ")
            name = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap ten mon hoc: ")
            credits_str = get_str_input(stdscr, f"[{i + 1}/{num}] Nhap so tin chi: ")
            credits = int(credits_str) if credits_str.isdigit() else 3
            courses[cid] = Course(cid, name, credits)
    return courses


def input_marks_for_course(stdscr, students: list, courses: dict):
    """Nhập điểm cho từng sinh viên theo môn học đã chọn."""
    cid = get_str_input(stdscr, "Nhap ma mon hoc can vao diem: ")
    if cid not in courses:
        return False, f"Khong tim thay mon hoc co ma: {cid}"

    for s in students:
        score_str = get_str_input(stdscr, f"Diem mon {courses[cid].name} cho SV {s.name} ({s.id}): ")
        try:
            raw_score = float(score_str)
            s.marks[cid] = round_down_score(raw_score)
        except ValueError:
            s.marks[cid] = 0.0

    return True, f"Nhap diem cho mon {courses[cid].name} hoan tat!"