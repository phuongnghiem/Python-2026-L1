import pandas as pd

def compute_avg_gpa_by_major(df):
    """Tính GPA trung bình theo ngành học (Major)"""
    avg_gpa = df.groupby("major")["GPA"].mean()
    print("\n[Part 1] GPA trung binh theo nganh hoc (Major):")
    print(avg_gpa)
    return avg_gpa

def merge_student_scores(students_df, scores_df, on_col="student_id"):
    """Gộp 2 bảng dữ liệu sinh viên và điểm số theo student_id"""
    merged = pd.merge(students_df, scores_df, on=on_col, how="inner")
    print("\n[Part 2] Bang du lieu sau khi Gop (Merge) - 5 dong dau:")
    print(merged.head(5))
    return merged

def compute_student_avg_score(merged_df):
    """Tính điểm trung bình các môn (python, math, database) của từng sinh viên"""
    score_cols = ["python", "math", "database"]
    merged_df["avg_score"] = merged_df[score_cols].mean(axis=1)
    
    result = merged_df[["student_id", "name", "major", "avg_score"]]
    print("\n[Part 2] Diem trung binh cac mon cua tung sinh vien (5 sinh vien dau):")
    print(result.head(5))
    return merged_df

def get_top_students(merged_df, top_n=5):
    """Tìm Top N sinh viên có điểm trung bình cao nhất"""
    top_students = merged_df[["student_id", "name", "major", "avg_score"]].sort_values(
        by="avg_score", ascending=False
    ).head(top_n)
    print(f"\n[Part 2] Top {top_n} sinh vien co diem trung binh cao nhat:")
    print(top_students)
    return top_students

def compute_avg_score_by_major(merged_df):
    """Tính điểm trung bình môn theo từng ngành học (Major)"""
    major_avg = merged_df.groupby("major")["avg_score"].mean()
    print("\n[Part 2] Diem trung binh theo nganh hoc (Major):")
    print(major_avg)
    return major_avg