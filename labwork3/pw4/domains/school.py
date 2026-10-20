import numpy as np


class School:
    def __init__(self):
        self.students = []
        self.courses = {}  # id -> Course

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses[course.id] = course

    def find_student(self, sid):
        return next((s for s in self.students if s.id == sid), None)

    def sort_by_gpa(self):
        """Sort student list by GPA, descending."""
        if not self.students:
            return
        gpas = np.array([s.gpa(self.courses) for s in self.students])
        order = np.argsort(-gpas, kind="stable")
        self.students = [self.students[i] for i in order]
