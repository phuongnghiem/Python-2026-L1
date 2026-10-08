# Student Mark Management System - PW5 (Persistent Information)

Dự án Quản lý Điểm Sinh viên được nâng cấp theo mô hình **Lập trình Hướng đối tượng (OOP)**, **Phân chia Mô-đun (Modularization)** và **Lưu trữ dữ liệu bền vững (Persistence Storage)** dành cho môn Lập trình Python tại USTH.

---

## 📌 Giới thiệu (Overview)

Chương trình được phát triển dựa trên PW4, bổ sung tính năng lưu trữ dữ liệu vĩnh viễn:
1. **Khởi chạy**: Tự động kiểm tra và nạp lại toàn bộ dữ liệu từ file nén `students.dat` (nếu tồn tại).
2. **Thoát chương trình**: Tự động ghi toàn bộ danh sách sinh viên, môn học và điểm số ra các file văn bản, sau đó đóng gói và nén lại thành file `students.dat`.

---

## 🏗️ Cấu trúc thư mục (Project Structure)

```text
pw5/
├── domains/                # Package chứa các lớp đối tượng (Domain models)
│   ├── __init__.py         # Khởi tạo package domains
│   ├── student.py          # Lớp Student & Logic tính GPA bằng NumPy
│   └── course.py           # Lớp Course quản lý môn học
├── input.py                # Module quản lý chức năng nhập dữ liệu Curses UI
├── output.py               # Module quản lý chức năng hiển thị Curses UI
├── persistence.py          # Module xử lý nạp/lưu và nén zip file (students.dat)
├── main.py                 # File điều phối chính (Entry Point)
└── README.md               # Tài liệu hướng dẫn dự án
