# Cấu trúc dữ liệu lưu trữ
students = []   # Lưu danh sách sinh viên dưới dạng dictionary
courses = []    # Lưu danh sách khóa học dưới dạng dictionary
marks = {}      # Lưu điểm với cấu trúc: {course_id: {student_id: mark}}

def input_students():
    """Nhập số lượng và thông tin sinh viên"""
    try:
        num_students = int(input("\nNhập số lượng sinh viên trong lớp: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
        return

    for i in range(num_students):
        print(f"\n--- Nhập thông tin sinh viên thứ {i+1} ---")
        student_id = input("Mã sinh viên (ID): ")
        name = input("Họ và tên: ")
        dob = input("Ngày sinh (DoB): ")
        
        # Thêm vào danh sách students
        students.append({"id": student_id, "name": name, "dob": dob})
    print("Đã thêm thông tin sinh viên thành công!")

def input_courses():
    """Nhập số lượng và thông tin khóa học"""
    try:
        num_courses = int(input("\nNhập số lượng khóa học: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
        return

    for i in range(num_courses):
        print(f"\n--- Nhập thông tin khóa học thứ {i+1} ---")
        course_id = input("Mã khóa học (ID): ")
        name = input("Tên khóa học: ")
        
        # Thêm vào danh sách courses và khởi tạo từ điển điểm rỗng cho môn này
        courses.append({"id": course_id, "name": name})
        marks[course_id] = {}
    print("Đã thêm thông tin khóa học thành công!")

def input_marks():
    """Chọn khóa học và nhập điểm cho các sinh viên"""
    if not courses or not students:
        print("\nLỗi: Bạn cần nhập thông tin sinh viên và khóa học trước!")
        return

    list_courses()
    course_id = input("\nNhập ID khóa học muốn nhập điểm: ")

    # Kiểm tra xem ID khóa học có tồn tại không
    if course_id not in [c['id'] for c in courses]:
        print("Lỗi: Khóa học không tồn tại!")
        return

    print(f"\n--- Nhập điểm cho khóa học {course_id} ---")
    for student in students:
        while True:
            try:
                mark = float(input(f"Nhập điểm cho sinh viên {student['name']} (ID: {student['id']}): "))
                # Lưu điểm vào dictionary marks
                marks[course_id][student['id']] = mark
                break
            except ValueError:
                print("Vui lòng nhập một số thực hợp lệ cho điểm số!")

def list_courses():
    """Hiển thị danh sách khóa học"""
    print("\n" + "="*30)
    print("DANH SÁCH KHÓA HỌC")
    print("="*30)
    if not courses:
        print("Chưa có dữ liệu khóa học.")
    else:
        for course in courses:
            print(f"ID: {course['id']:<10} | Tên môn: {course['name']}")

def list_students():
    """Hiển thị danh sách sinh viên"""
    print("\n" + "="*30)
    print("DANH SÁCH SINH VIÊN")
    print("="*30)
    if not students:
        print("Chưa có dữ liệu sinh viên.")
    else:
        for student in students:
            print(f"ID: {student['id']:<10} | Họ tên: {student['name']:<20} | Ngày sinh: {student['dob']}")

def show_marks():
    """Hiển thị điểm của sinh viên theo một khóa học cụ thể"""
    if not marks:
        print("\nChưa có dữ liệu điểm nào được nhập.")
        return

    list_courses()
    course_id = input("\nNhập ID khóa học muốn xem bảng điểm: ")

    if course_id not in marks:
        print("Lỗi: Khóa học không tồn tại hoặc chưa được khởi tạo!")
        return

    print("\n" + "="*40)
    print(f"BẢNG ĐIỂM KHÓA HỌC: {course_id}")
    print("="*40)
    
    course_marks = marks[course_id]
    if not course_marks:
        print("Khóa học này hiện chưa có điểm của sinh viên nào.")
    else:
        for student in students:
            student_id = student['id']
            if student_id in course_marks:
                print(f"ID: {student_id:<10} | Tên: {student['name']:<20} | Điểm: {course_marks[student_id]}")

def main():
    """Hàm main điều khiển luồng chương trình bằng Menu"""
    while True:
        print("\n" + "*"*40)
        print("PHẦN MỀM QUẢN LÝ ĐIỂM SINH VIÊN (PW1)".center(40))
        print("*"*40)
        print("1. Nhập danh sách sinh viên")
        print("2. Nhập danh sách khóa học")
        print("3. Nhập điểm cho khóa học")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Hiển thị danh sách khóa học")
        print("6. Hiển thị bảng điểm theo khóa học")
        print("0. Thoát chương trình")
        print("*"*40)

        choice = input("Vui lòng chọn chức năng (0-6): ")

        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            print("Đang thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 6!")

# Điểm bắt đầu thực thi chương trình
if __name__ == "__main__":
    main()