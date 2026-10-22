import math


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        # Round down to 1 decimal place
        self.__mark = math.floor(mark * 10) / 10

    def get_student_id(self):
        return self.__student_id

    def get_course_id(self):
        return self.__course_id

    def get_mark(self):
        return self.__mark
