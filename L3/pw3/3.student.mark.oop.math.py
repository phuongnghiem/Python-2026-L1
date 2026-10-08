import math
import numpy as np
import curses

# =========================================================================
# 1. LỚP KHÓA HỌC (COURSE CLASS)
# =========================================================================
class Course:
    def __init__(self, course_id, name, credits):
        # Khởi tạo thông tin cơ bản của môn học bao gồm mã, tên và số tín chỉ
        self.id = course_id        # Mã môn học
        self.name = name          # Tên môn học
        self.credits = credits    # Số tín chỉ của môn học (dùng tính GPA có trọng số)

    def __str__(self):
        # Định dạng chuỗi hiển thị khi in đối tượng Course
        return f"ID: {self.id:<10} | Ten: {self.name:<25} | Tin chi: {self.credits}"


# =========================================================================
# 2. LỚP SINH VIÊN (STUDENT CLASS)
# =========================================================================
class Student:
    def __init__(self, student_id, name, dob):
        # Khởi tạo thuộc tính của sinh viên
        self.id = student_id      # Mã sinh viên
        self.name = name          # Họ và tên
        self.dob = dob            # Ngày sinh
        self.marks = {}           # Từ điển lưu điểm dạng: {course_id: mark_float}
        self.gpa = 0.0            # Điểm trung bình tích lũy GPA (mặc định ban đầu là 0.0)

    def add_mark(self, course_id, mark):
        """Thêm hoặc cập nhật điểm cho một môn học cụ thể"""
        self.marks[course_id] = mark

    def calculate_gpa(self, courses_dict):
        """
        YÊU CẦU PW3: Tính GPA có trọng số bằng NumPy Array:
        GPA = Tổng(Điểm môn i * Tín chỉ môn i) / Tổng(Tín chỉ các môn)
        """
        mark_list = []      # Danh sách chứa điểm số các môn đã học
        credit_list = []    # Danh sách chứa tín chỉ tương ứng của các môn đó

        # Lặp qua tất cả điểm môn học mà sinh viên này có
        for course_id, mark in self.marks.items():
            if course_id in courses_dict:
                mark_list.append(mark)
                credit_list.append(courses_dict[course_id].credits)

        # Kiểm tra nếu sinh viên đã có điểm và tổng tín chỉ > 0
        if credit_list and sum(credit_list) > 0:
            # Chuyển đổi danh sách Python thành NumPy Arrays
            marks_array = np.array(mark_list)
            credits_array = np.array(credit_list)

            # Tính tổng tích điểm * tín chỉ bằng NumPy
            weighted_sum = np.sum(marks_array * credits_array)
            # Tính tổng số tín chỉ bằng NumPy
            total_credits = np.sum(credits_array)

            # Điểm GPA bằng tổng điểm tích lũy chia cho tổng số tín chỉ
            self.gpa = float(weighted_sum / total_credits)
        else:
            self.gpa = 0.0

    def __str__(self):
        # Định dạng hiển thị sinh viên cùng với điểm GPA
        return f"ID: {self.id:<10} | Ho ten: {self.name:<20} | DoB: {self.dob:<12} | GPA: {self.gpa:.2f}"


# =========================================================================
# 3. LỚP QUẢN LÝ HỆ THỐNG VÀ GIAO DIỆN CURSES (APP CLASS)
# =========================================================================
class StudentMarkApp:
    def __init__(self):
        # Quản lý toàn bộ danh sách sinh viên và khóa học dưới dạng từ điển
        self.students = {}  # {student_id: Student_Object}
        self.courses = {}   # {course_id: Course_Object}

    def input_str(self, stdscr, row, col, prompt):
        """Hàm phụ trợ hỗ trợ nhập chuỗi dữ liệu trực tiếp trên giao diện Curses"""
        curses.echo()                  # Bật hiển thị ký tự người dùng gõ vào
        stdscr.addstr(row, col, prompt) # In chuỗi yêu cầu (prompt) ra màn hình
        stdscr.refresh()               # Cập nhật màn hình terminal
        # Nhập dữ liệu byte từ bàn phím
        input_bytes = stdscr.getstr(row, col + len(prompt))
        curses.noecho()                # Tắt lại chế độ hiển thị tự do
        # Giải mã từ Bytes sang chuỗi UTF-8 và cắt bỏ khoảng trắng thừa
        return input_bytes.decode('utf-8').strip()

    def add_students_ui(self, stdscr):
        """Giao diện nhập danh sách sinh viên mới"""
        stdscr.clear()                 # Xóa màn hình Curses
        stdscr.border(0)               # Vẽ khung viền màn hình
        stdscr.addstr(1, 2, "=== NHAP DU LIEU SINH VIEN ===", curses.A_BOLD)
        
        try:
            num_str = self.input_str(stdscr, 3, 2, "Nhap so luong sinh vien muon them: ")
            num_students = int(num_str)
        except ValueError:
            stdscr.addstr(5, 2, "So luong khong hop le! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        current_row = 5
        for i in range(num_students):
            stdscr.addstr(current_row, 2, f"--- Sinh vien thu {i+1} ---", curses.A_UNDERLINE)
            s_id = self.input_str(stdscr, current_row + 1, 2, "Ma sinh vien (ID): ")
            s_name = self.input_str(stdscr, current_row + 2, 2, "Ho va ten: ")
            s_dob = self.input_str(stdscr, current_row + 3, 2, "Ngay sinh (DoB): ")

            # Khởi tạo đối tượng Student và thêm vào từ điển quản lý
            student = Student(s_id, s_name, s_dob)
            self.students[s_id] = student
            current_row += 5

            # Reset màn hình nếu vượt quá chiều cao dòng hiển thị của Terminal
            if current_row > curses.LINES - 6:
                stdscr.clear()
                stdscr.border(0)
                current_row = 2

        stdscr.addstr(current_row + 1, 2, "Them sinh vien thanh cong! Bam phim bat ky de tiep tuc...")
        stdscr.getch()

    def add_courses_ui(self, stdscr):
        """Giao diện nhập danh sách khóa học mới"""
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "=== NHAP DU LIEU KHOA HOC ===", curses.A_BOLD)
        
        try:
            num_str = self.input_str(stdscr, 3, 2, "Nhap so luong khoa hoc muon them: ")
            num_courses = int(num_str)
        except ValueError:
            stdscr.addstr(5, 2, "So luong khong hop le! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        current_row = 5
        for i in range(num_courses):
            stdscr.addstr(current_row, 2, f"--- Khoa hoc thu {i+1} ---", curses.A_UNDERLINE)
            c_id = self.input_str(stdscr, current_row + 1, 2, "Ma khoa hoc (ID): ")
            c_name = self.input_str(stdscr, current_row + 2, 2, "Ten khoa hoc: ")
            try:
                c_credits = float(self.input_str(stdscr, current_row + 3, 2, "So tin chi (Credits): "))
            except ValueError:
                c_credits = 1.0  # Mặc định tín chỉ là 1.0 nếu người dùng nhập sai

            # Khởi tạo đối tượng Course và thêm vào từ điển quản lý
            course = Course(c_id, c_name, c_credits)
            self.courses[c_id] = course
            current_row += 5

            if current_row > curses.LINES - 6:
                stdscr.clear()
                stdscr.border(0)
                current_row = 2

        stdscr.addstr(current_row + 1, 2, "Them khoa hoc thanh cong! Bam phim bat ky de tiep tuc...")
        stdscr.getch()

    def input_marks_ui(self, stdscr):
        """Giao diện nhập điểm và sử dụng math.floor() làm tròn xuống 1 chữ số thập phân"""
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "=== NHAP DIEM SINH VIEN ===", curses.A_BOLD)

        # Kiểm tra điều kiện phải có sinh viên và môn học trước khi nhập điểm
        if not self.courses:
            stdscr.addstr(3, 2, "Chua co khoa hoc nao! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return
        if not self.students:
            stdscr.addstr(3, 2, "Chua co sinh vien nao! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        c_id = self.input_str(stdscr, 3, 2, "Nhap Ma mon hoc muon nhap diem: ")
        if c_id not in self.courses:
            stdscr.addstr(5, 2, "Ma khoa hoc khong ton tai! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        current_row = 5
        course = self.courses[c_id]
        stdscr.addstr(current_row, 2, f"Nhap diem mon: {course.name} (So tin chi: {course.credits})", curses.A_UNDERLINE)
        current_row += 2

        for student_id, student in self.students.items():
            while True:
                try:
                    mark_str = self.input_str(stdscr, current_row, 2, f"Diem cua SV {student.name} ({student.id}): ")
                    raw_mark = float(mark_str)
                    
                    # YÊU CẦU PW3: Dùng module math làm tròn xuống 1 chữ số thập phân (floor)
                    rounded_mark = math.floor(raw_mark * 10.0) / 10.0

                    # Lưu điểm vào đối tượng sinh viên
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

        # Cập nhật lại GPA mới cho tất cả sinh viên ngay sau khi bổ sung điểm
        self.update_all_gpas()

        stdscr.addstr(current_row + 1, 2, "Nhap diem thanh cong va da tinh lai GPA! Bam phim bat ky...")
        stdscr.getch()

    def update_all_gpas(self):
        """Cập nhật điểm GPA cho toàn bộ sinh viên bằng phương thức calculate_gpa"""
        for student in self.students.values():
            student.calculate_gpa(self.courses)

    def list_students_ui(self, stdscr):
        """Giao diện hiển thị danh sách sinh viên sắp xếp theo GPA giảm dần"""
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "=== DANH SACH SINH VIEN (SAP XEP THEO GPA GIAM DAN) ===", curses.A_BOLD)

        if not self.students:
            stdscr.addstr(3, 2, "Chua co du lieu sinh vien! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        # Đảm bảo tính toán lại GPA mới nhất trước khi sắp xếp
        self.update_all_gpas()

        # YÊU CẦU PW3: Chuyển danh sách và sắp xếp sinh viên theo điểm GPA giảm dần (reverse=True)
        student_list = list(self.students.values())
        student_list.sort(key=lambda s: s.gpa, reverse=True)

        row = 3
        # In tiêu đề bảng điểm
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

    def list_courses_ui(self, stdscr):
        """Giao diện hiển thị danh sách tất cả các khóa học"""
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "=== DANH SACH KHOA HOC ===", curses.A_BOLD)

        if not self.courses:
            stdscr.addstr(3, 2, "Chua co du lieu khoa hoc! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        row = 3
        stdscr.addstr(row, 2, f"{'STT':<5} | {'MA MON':<10} | {'TEN MON HOC':<30} | {'TIN CHI':<10}", curses.A_REVERSE)
        row += 1

        for idx, course in enumerate(self.courses.values(), start=1):
            line = f"{idx:<5} | {course.id:<10} | {course.name:<30} | {course.credits:<10.1f}"
            stdscr.addstr(row, 2, line)
            row += 1

        stdscr.addstr(row + 1, 2, "Nhan phim bat ky de quay lai Menu chinh...")
        stdscr.getch()

    def show_marks_ui(self, stdscr):
        """Giao diện hiển thị bảng điểm của từng sinh viên theo môn học"""
        stdscr.clear()
        stdscr.border(0)
        stdscr.addstr(1, 2, "=== BANG DIEM THEO MON HOC ===", curses.A_BOLD)

        if not self.courses:
            stdscr.addstr(3, 2, "Chua co du lieu khoa hoc! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        c_id = self.input_str(stdscr, 3, 2, "Nhap Ma mon hoc muon xem diem: ")
        if c_id not in self.courses:
            stdscr.addstr(5, 2, "Khoa hoc khong ton tai! Bam phim bat ky de quay lai...")
            stdscr.getch()
            return

        course = self.courses[c_id]
        row = 5
        stdscr.addstr(row, 2, f"BANG DIEM MON: {course.name} ({course.id}) - Tin chi: {course.credits}", curses.A_UNDERLINE)
        row += 2

        stdscr.addstr(row, 2, f"{'MA SV':<10} | {'HO VA TEN':<20} | {'DIEM (DA LAM TRON DOWN)':<25}", curses.A_REVERSE)
        row += 1

        has_mark = False
        for student in self.students.values():
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

    def main_menu(self, stdscr):
        """Hàm điều khiển Menu chính của Curses UI"""
        curses.curs_set(1)  # Hiển thị con trỏ nhập liệu

        while True:
            stdscr.clear()
            stdscr.border(0)  # Vẽ viền khung giao diện

            # Khối tiêu đề trang trí
            stdscr.addstr(1, 2, "================================================", curses.A_BOLD)
            stdscr.addstr(2, 2, "    HE THONG QUAN LY DIEM SINH VIEN (PW3)       ", curses.A_BOLD)
            stdscr.addstr(3, 2, "================================================", curses.A_BOLD)

            # Các chức năng trong Menu
            stdscr.addstr(5, 4, "1. Nhap thong tin Sinh vien")
            stdscr.addstr(6, 4, "2. Nhap thong tin Khoa hoc (Bao gom so Tin chi)")
            stdscr.addstr(7, 4, "3. Nhap diem mon hoc (Lam tron xuong bang math.floor)")
            stdscr.addstr(8, 4, "4. Hien thi danh sach Sinh vien (Sap xep theo GPA giam dan)")
            stdscr.addstr(9, 4, "5. Hien thi danh sach Khoa hoc")
            stdscr.addstr(10, 4, "6. Hien thi Bang diem theo mon hoc")
            stdscr.addstr(11, 4, "0. Thoat chuong trinh")

            stdscr.addstr(13, 2, "------------------------------------------------")
            choice = self.input_str(stdscr, 14, 2, "Vui long chon chuc nang (0-6): ")

            if choice == '1':
                self.add_students_ui(stdscr)
            elif choice == '2':
                self.add_courses_ui(stdscr)
            elif choice == '3':
                self.input_marks_ui(stdscr)
            elif choice == '4':
                self.list_students_ui(stdscr)
            elif choice == '5':
                self.list_courses_ui(stdscr)
            elif choice == '6':
                self.show_marks_ui(stdscr)
            elif choice == '0':
                break


# =========================================================================
# 4. ĐIỂM KHỞI CHẠY CHƯƠNG TRÌNH (ENTRY POINT)
# =========================================================================
def main():
    app = StudentMarkApp()
    # Sử dụng curses.wrapper để tự động khởi tạo màn hình terminal và khôi phục khi thoát
    curses.wrapper(app.main_menu)

if __name__ == "__main__":
    main()