# Student Mark Management System - PW4 (Modularization)

Dự án Quản lý Điểm Sinh viên được xây dựng theo mô hình **Lập trình Hướng đối tượng (OOP)** và cấu trúc **Phân chia Mô-đun (Modularization)** dành cho bài tập thực hành môn Python tại USTH[cite: 1, 2, 3].

---

## 📌 Giới thiệu (Overview)

Chương trình được phát triển từ bài tập PW3[cite: 2, 3], cho phép quản lý thông tin sinh viên, môn học, số tín chỉ, điểm số và tự động tính điểm GPA tích lũy có trọng số bằng NumPy[cite: 2]. Giao diện tương tác trực tiếp trên dòng lệnh Terminal được trang trí và điều hướng bằng thư viện `curses`[cite: 2].

---

## 🏗️ Cấu trúc thư mục (Project Structure)

Chương trình được chia nhỏ thành các gói (packages) và mô-đun (modules) độc lập theo đúng yêu cầu thiết kế PW4[cite: 3]:

```text
pw4/
├── domains/                # Package chứa các lớp đối tượng chính (Domain models)
│   ├── __init__.py         # Khởi tạo package domains
│   ├── student.py          # Lớp Student & Logic tính GPA bằng NumPy
│   └── course.py           # Lớp Course quản lý thông tin môn học
├── input.py                # Module quản lý các chức năng nhập dữ liệu Curses UI
├── output.py               # Module quản lý các chức năng hiển thị Curses UI
├── main.py                 # File điều phối chính (Entry Point)
└── README.md               # Tài liệu hướng dẫn dự án
```

---

## ✨ Tính năng chính (Key Features)

* **Hướng đối tượng (OOP)**: Đóng gói toàn bộ logic và thuộc tính của `Student` và `Course` trong package `domains`[cite: 3].
* **Làm tròn điểm chuẩn**: Sử dụng module `math.floor()` làm tròn xuống 1 chữ số thập phân khi nhập điểm[cite: 2].
* **Tính GPA có trọng số**: Sử dụng mảng NumPy (`np.array`) tính tổng tích điểm và tín chỉ[cite: 2]:
  $$\text{GPA} = \frac{\sum (\text{Điểm môn} \times \text{Tín chỉ})}{\sum \text{Tín chỉ}}$$
* **Sắp xếp tự động**: Danh sách sinh viên được sắp xếp giảm dần theo điểm trung bình GPA[cite: 2].
* **Giao diện Curses UI**: Giao diện khung viền bảng biểu sạch sẽ, trực quan trên dòng lệnh Terminal (sử dụng tiếng Việt không dấu để đảm bảo tương thích mọi màn hình)[cite: 2].

---

## 🛠️ Yêu cầu & Cài đặt (Requirements & Setup)

### 1. Yêu cầu hệ thống
* Python 3.8 trở lên.
* Thư viện `numpy`[cite: 2].
* Thư viện `windows-curses` (dành cho hệ điều hành Windows)[cite: 2].

### 2. Cài đặt các thư viện cần thiết

Mở Terminal / Command Prompt và chạy câu lệnh:

```bash
pip install numpy
```

> **Lưu ý với hệ điều hành Windows:**
> Thư viện `curses` mặc định sẵn có trên Linux/macOS. Nếu chạy trên Windows, bạn bắt buộc phải cài gói hỗ trợ[cite: 2]:
> ```bash
> pip install windows-curses
> ```

---

## 🚀 Hướng dẫn chạy chương trình (How to Run)

1. Mở Terminal và di chuyển vào thư mục dự án `pw4`[cite: 3]:
   ```bash
   cd pw4
   ```

2. Thực thi file script chính `main.py`[cite: 3]:
   ```bash
   python main.py
   ```

---

## 📋 Hướng dẫn sử dụng Menu

Khi khởi chạy, chương trình hiển thị bảng chọn điều hướng:

1. **1. Nhap thong tin Sinh vien**: Thêm sinh viên (Mã SV, Họ tên, Ngày sinh).
2. **2. Nhap thong tin Khoa hoc**: Thêm môn học mới (Mã môn, Tên môn, Số tín chỉ).
3. **3. Nhap diem mon hoc**: Chọn môn học và nhập điểm cho từng sinh viên (điểm tự động được làm tròn down 1 chữ số thập phân).
4. **4. Hien thi danh sach Sinh vien**: Bảng xếp hạng sinh viên sắp xếp giảm dần theo GPA.
5. **5. Hien thi danh sach Khoa hoc**: Xem bảng danh sách toàn bộ các môn học và số tín chỉ.
6. **6. Hien thi Bang diem theo mon hoc**: Tra cứu điểm thi từng môn học.
7. **0. Thoat chuong trinh**: Thoát ứng dụng.

---

## 📤 Hướng dẫn đưa dự án lên GitHub (Push to GitHub)

### Trường hợp 1: Đẩy bài làm lên repository đã Fork từ trường/thầy giáo (Theo yêu cầu PW4)[cite: 3]

1. Mở Terminal tại thư mục `pw4`:
   ```bash
   cd pw4
   ```

2. Khởi tạo Git repository ở máy cá nhân (nếu chưa khởi tạo):
   ```bash
   git init
   ```

3. Liên kết với Repository đã được Fork về tài khoản GitHub của bạn:
   ```bash
   git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
   ```

4. Kiểm tra trạng thái và thêm toàn bộ mã nguồn vào staging area:
   ```bash
   git status
   git add .
   ```

5. Lưu lại thay đổi (Commit):
   ```bash
   git commit -m "Complete PW4: Modularization"
   ```

6. Đẩy code lên GitHub:
   ```bash
   git push -u origin main
   ```
   *(Lưu ý: Nếu tên nhánh chính mặc định trên GitHub của bạn là `master`, hãy đổi `main` thành `master`)*

---

### Trường hợp 2: Tạo một Repository mới từ đầu trên GitHub

1. Truy cập [GitHub](https://github.com) -> Nhấn vào dấu **+** ở góc trên bên phải -> Chọn **New repository**.
2. Đặt tên cho Repository (ví dụ: `pw4-student-management`) -> Nhấn **Create repository**.
3. Tại thư mục `pw4` trên máy tính, mở Terminal và thực hiện lần lượt các lệnh:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for PW4 project"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
   git push -u origin main
   ```

---

## 👤 Thông tin Tác giả

* **Họ và tên**: Nguyễn Hữu Dũng
* **Mã sinh viên**: 2410234
* **Lớp**: 261ICT2013.L2
* **Trường**: Đại học Khoa học và Công nghệ Hà Nội (USTH)