import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        # Khởi tạo thuộc tính của sinh viên
        self.id = student_id      # Mã sinh viên
        self.name = name          # Họ và tên
        self.dob = dob            # Ngày sinh
        self.marks = {}           # Từ điển lưu điểm dạng: {course_id: mark_float}
        self.gpa = 0.0            # Điểm trung bình tích lũy GPA

    def add_mark(self, course_id, mark):
        """Thêm hoặc cập nhật điểm cho một môn học"""
        self.marks[course_id] = mark

    def calculate_gpa(self, courses_dict):
        """Tính GPA có trọng số bằng NumPy Array"""
        mark_list = []
        credit_list = []

        for course_id, mark in self.marks.items():
            if course_id in courses_dict:
                mark_list.append(mark)
                credit_list.append(courses_dict[course_id].credits)

        if credit_list and sum(credit_list) > 0:
            marks_array = np.array(mark_list)
            credits_array = np.array(credit_list)

            weighted_sum = np.sum(marks_array * credits_array)
            total_credits = np.sum(credits_array)

            self.gpa = float(weighted_sum / total_credits)
        else:
            self.gpa = 0.0

    def __str__(self):
        return f"ID: {self.id:<10} | Ho ten: {self.name:<20} | DoB: {self.dob:<12} | GPA: {self.gpa:.2f}"