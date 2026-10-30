import math
import numpy as np


class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10.0) / 10.0

    def calculate_gpa(self, courses_dict):
        if not self.marks:
            self.gpa = 0.0
            return 0.0

        marks_list = []
        credits_list = []

        for course_id, mark in self.marks.items():
            if course_id in courses_dict:
                marks_list.append(mark)
                credits_list.append(courses_dict[course_id].credit)

        if not credits_list or sum(credits_list) == 0:
            self.gpa = 0.0
            return 0.0

        marks_array = np.array(marks_list)
        credits_array = np.array(credits_list)

        weighted_sum = np.sum(marks_array * credits_array)
        total_credits = np.sum(credits_array)

        self.gpa = float(weighted_sum / total_credits)
        return self.gpa