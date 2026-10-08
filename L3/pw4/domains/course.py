class Course:
    def __init__(self, course_id, name, credits):
        # Khởi tạo thông tin cơ bản của môn học bao gồm mã, tên và số tín chỉ
        self.id = course_id        # Mã môn học
        self.name = name          # Tên môn học
        self.credits = credits    # Số tín chỉ của môn học (dùng tính GPA)

    def __str__(self):
        # Định dạng chuỗi hiển thị khi in đối tượng Course
        return f"ID: {self.id:<10} | Ten: {self.name:<25} | Tin chi: {self.credits}"