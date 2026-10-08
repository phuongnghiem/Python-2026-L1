import os
import zipfile

STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"
MARKS_FILE = "marks.txt"
DATA_ARCHIVE = "students.dat"

def save_data(students, courses, marks_dict):
    """Ghi dữ liệu ra các file text"""
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s}\n")

    with open(COURSES_FILE, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c}\n")

def compress_data():
    """Nén các file text thành students.dat trước khi thoát"""
    files_to_compress = [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]
    with zipfile.ZipFile(DATA_ARCHIVE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file)

def load_data(students, courses):
    """Giải nén và nạp dữ liệu khi khởi động"""
    if os.path.exists(DATA_ARCHIVE):
        with zipfile.ZipFile(DATA_ARCHIVE, 'r') as zipf:
            zipf.extractall()