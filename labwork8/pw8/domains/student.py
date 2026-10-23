import numpy as np


class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.marks = {}  # course_id -> mark

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def gpa(self, courses):
        """Weighted average of marks by course credits (numpy arrays)."""
        ids = [c for c in self.marks if c in courses]
        if not ids:
            return 0.0
        marks = np.array([self.marks[c] for c in ids])
        credits = np.array([courses[c].credits for c in ids])
        return float(np.sum(marks * credits) / np.sum(credits))
