class Course:
    def __init__(self, course_id, name, credits):
        # Khởi tạo thông tin môn học
        self.id = course_id        # Mã môn học
        self.name = name          # Tên môn học
        self.credits = float(credits) # Số tín chỉ

    def to_dict(self):
        """Chuyển đổi đối tượng sang Dictionary để chuẩn bị lưu trữ dữ liệu"""
        return {
            "id": self.id,
            "name": self.name,
            "credits": self.credits
        }

    def __str__(self):
        return f"ID: {self.id:<10} | Ten: {self.name:<25} | Tin chi: {self.credits}"