import os
import pandas as pd

def ensure_sample_data():
    """
    Tự động tạo file students.csv và scores.csv với đầy đủ dữ liệu
    nếu phát hiện các file này chưa tồn tại trong thư mục.
    """
    if not os.path.exists("students.csv"):
        students_csv_content = """student_id,name,age,major,GPA
S001,Alice,20,ICT,3.4
S002,Bob,21,Data Science,3.7
S003,Carol,20,ICT,3.2
S004,David,22,Data Science,3.8
S005,Emma,21,Cybersecurity,3.55
S006,Frank,20,Applied Mathematics,3.1
S007,Grace,21,ICT,3.85
S008,Henry,22,Cybersecurity,2.95
S009,Ivy,20,Data Science,3.6
S010,Jack,21,Applied Mathematics,3.35
S011,Kate,22,ICT,3.9
S012,Leo,20,Data Science,
S013,Mia,21,Cybersecurity,3.45
S014,Noah,22,Applied Mathematics,3.75
S015,Olivia,,ICT,3.5
S016,Peter,21,Data Science,3.15
S017,Quinn,20,Cybersecurity,3.65
S018,Rose,22,Applied Mathematics,3.05
S019,Sam,21,ICT,3.3
S020,Tina,20,Data Science,3.95
S021,Uma,22,Cybersecurity,3.25
S022,Victor,21,Applied Mathematics,3.55
S023,Wendy,20,ICT,3.7
S024,Xavier,22,Data Science,3.4
S025,Yara,21,Cybersecurity,
S026,Zack,20,Applied Mathematics,3.8
S027,Anna,21,ICT,3.6
S028,Brian,22,Data Science,2.85
S029,Chloe,20,Cybersecurity,3.9
S030,Daniel,21,Applied Mathematics,3.45"""
        with open("students.csv", "w", encoding="utf-8") as f:
            f.write(students_csv_content)
        print("-> Da khoi tao file 'students.csv' thành cong.")

    if not os.path.exists("scores.csv"):
        scores_csv_content = """student_id,python,math,database
S001,85,80,88
S002,92,88,90
S003,78,82,76
S004,95,91,94
S005,89,84,91
S006,74,86,72
S007,96,90,93
S008,70,75,68
S009,91,89,87
S010,82,93,79
S011,97,92,96
S012,84,,81
S013,88,83,90
S014,90,95,86
S015,86,79,85
S016,77,81,80
S017,93,85,92
S018,72,88,74
S019,80,78,82
S020,98,94,97
S021,79,76,84
S022,87,91,83
S023,94,86,89
S024,83,85,
S025,81,80,86
S026,92,97,88
S027,89,87,91
S028,69,74,71
S029,96,,95
S030,84,90,82"""
        with open("scores.csv", "w", encoding="utf-8") as f:
            f.write(scores_csv_content)
        print("-> Da khoi tao file 'scores.csv' thanh cong.")

def load_csv(file_path):
    """Nạp file CSV vào DataFrame"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Khong tim thay file: {file_path}")
    return pd.read_csv(file_path)

def check_missing_values(df, name="Dataset"):
    """Kiểm tra và hiển thị số lượng giá trị thiếu (NaN) trong DataFrame"""
    print(f"\n--- So luong gia tri khuyet (NaN) trong {name} ---")
    missing = df.isnull().sum()
    print(missing)
    return missing

def clean_missing_data(students_df, scores_df):
    """Xử lý giá trị khuyết (Fill hoặc Remove) cho cả 2 DataFrame"""
    students_clean = students_df.dropna(subset=["student_id"]).copy()
    scores_clean = scores_df.dropna(subset=["student_id"]).copy()

    # Điền giá trị trung bình cho GPA và trung vị cho age bị thiếu
    if "GPA" in students_clean.columns:
        students_clean["GPA"] = students_clean["GPA"].fillna(students_clean["GPA"].mean())
    if "age" in students_clean.columns:
        students_clean["age"] = students_clean["age"].fillna(students_clean["age"].median())

    # Điền điểm trung bình cho các môn thi bị thiếu trong scores.csv
    score_cols = ["python", "math", "database"]
    for col in score_cols:
        if col in scores_clean.columns:
            scores_clean[col] = scores_clean[col].fillna(scores_clean[col].mean())

    return students_clean, scores_clean