class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Từ bước trước
        self.gpa = 0.0   # Thuộc tính lưu điểm GPA

    def calculate_gpa(self, courses):
        """Tính điểm GPA dựa trên điểm số và số tín chỉ của các môn học"""
        total_score = 0
        total_credits = 0
        
        for cid, mark in self.marks.items():
            if cid in courses:
                # Lấy số tín chỉ của môn học (mặc định là 1 nếu không có thuộc tính credits)
                credit = getattr(courses[cid], 'credits', 1)
                total_score += mark * credit
                total_credits += credit
                
        if total_credits > 0:
            self.gpa = total_score / total_credits
        else:
            self.gpa = 0.0