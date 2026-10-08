import os
import zipfile
from domains import Student, Course

DATA_FILE = "students.dat"
TXT_FILES = ["courses.txt", "students.txt", "marks.txt"]

def save_data(students, courses):
    """
    Xuất dữ liệu từ bộ nhớ ra các file văn bản (sử dụng phương thức to_dict())
    và nén toàn bộ thành file students.dat trước khi thoát chương trình.
    """
    # 1. Ghi thông tin danh sách môn học
    with open("courses.txt", "w", encoding="utf-8") as f:
        for course in courses.values():
            c_data = course.to_dict()
            f.write(f"{c_data['id']}|{c_data['name']}|{c_data['credits']}\n")

    # 2. Ghi thông tin danh sách sinh viên
    with open("students.txt", "w", encoding="utf-8") as f:
        for student in students.values():
            s_data = student.to_dict()
            f.write(f"{s_data['id']}|{s_data['name']}|{s_data['dob']}\n")

    # 3. Ghi điểm số môn học của sinh viên
    with open("marks.txt", "w", encoding="utf-8") as f:
        for student in students.values():
            s_data = student.to_dict()
            for course_id, mark in s_data['marks'].items():
                f.write(f"{s_data['id']}|{course_id}|{mark}\n")

    # 4. Nén các file văn bản tạm thành file students.dat
    with zipfile.ZipFile(DATA_FILE, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_name in TXT_FILES:
            if os.path.exists(file_name):
                zf.write(file_name)
                os.remove(file_name)  # Xóa các file .txt tạm sau khi đã đóng gói vào ZIP


def load_data(students, courses):
    """
    Kiểm tra file students.dat khi khởi động chương trình.
    Nếu tồn tại, thực hiện giải nén và nạp lại toàn bộ dữ liệu vào bộ nhớ.
    """
    if not os.path.exists(DATA_FILE):
        return

    # 1. Giải nén tất cả file từ students.dat
    try:
        with zipfile.ZipFile(DATA_FILE, "r") as zf:
            zf.extractall()
    except Exception:
        return

    # 2. Đọc và khởi tạo danh sách Môn học (Course)
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        c_id, c_name, c_credits = parts
                        courses[c_id] = Course(c_id, c_name, c_credits)
        os.remove("courses.txt")

    # 3. Đọc và khởi tạo danh sách Sinh viên (Student)
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        s_id, s_name, s_dob = parts
                        students[s_id] = Student(s_id, s_name, s_dob)
        os.remove("students.txt")

    # 4. Đọc và gán lại Điểm số (Marks) cho từng Sinh viên
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        s_id, c_id, mark = parts
                        if s_id in students:
                            students[s_id].add_mark(c_id, float(mark))
        os.remove("marks.txt")

    # 5. Tự động cập nhật và tính lại GPA tích lũy cho toàn bộ sinh viên
    for student in students.values():
        student.calculate_gpa(courses)