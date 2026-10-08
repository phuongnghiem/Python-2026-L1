# Labwork 5 - Data Manipulation & Analysis with Pandas

Dự án thực hành xử lý và phân tích dữ liệu sinh viên sử dụng thư viện **Pandas** và **NumPy** thuộc chương trình Lập trình Python nâng cao tại USTH.

---

## 📌 Giới thiệu (Overview)

Chương trình được chia thành 2 phần chính theo cấu trúc mô-đun:
1. **Part 1 - Data Manipulation**: Tải tập dữ liệu `students.csv`, truy vấn, lọc sinh viên theo điều kiện GPA, sắp xếp và tính toán chỉ số GPA trung bình theo ngành học (Major)[cite: 9].
2. **Part 2 - From Raw Data to Useful Info**: Kiểm tra và làm sạch dữ liệu thiếu (`NaN`), gộp hai bảng `students.csv` và `scores.csv`, tính điểm trung bình các môn, tìm Top 5 sinh viên xuất sắc và tính điểm trung bình theo từng ngành.

---

## 🏗️ Cấu trúc thư mục (Project Structure)

```text
labwork5/
├── modules/                # Package chứa các mô-đun xử lý dữ liệu
│   ├── __init__.py         # Khởi tạo package modules
│   ├── data_loader.py      # Module nạp, kiểm tra và làm sạch dữ liệu khuyết
│   ├── manipulation.py     # Module thực hiện lọc & sắp xếp dữ liệu (Part 1)
│   └── analysis.py         # Module gộp bảng & tính toán phân tích (Part 2)
├── students.csv            # Tập dữ liệu sinh viên
├── scores.csv              # Tập dữ liệu điểm số các môn
├── main.py                 # File điều phối chính (Entry Point)
└── README.md               # Tài liệu hướng dẫn dự án
