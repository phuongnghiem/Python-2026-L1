import numpy as np


class Student:
    def __init__(self, student_id: str, name: str, dob: str):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # {course_id: score}
        self.gpa = 0.0

    def calculate_gpa(self, courses_dict: dict) -> float:
        """Tính điểm GPA có trọng số dựa trên số tín chỉ bằng numpy."""
        marks_list = []
        credits_list = []

        for course_id, score in self.marks.items():
            if course_id in courses_dict:
                marks_list.append(score)
                credits_list.append(courses_dict[course_id].credits)

        if not marks_list or sum(credits_list) == 0:
            self.gpa = 0.0
            return 0.0

        marks_arr = np.array(marks_list, dtype=float)
        credits_arr = np.array(credits_list, dtype=float)

        weighted_sum = np.sum(marks_arr * credits_arr)
        total_credits = np.sum(credits_arr)
        self.gpa = float(weighted_sum / total_credits)
        return self.gpa