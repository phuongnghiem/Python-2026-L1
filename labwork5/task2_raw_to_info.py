"""Labwork 5 - Task 2: From raw data to useful info (students.csv + scores.csv)"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent
SUBJECTS = ["python", "math", "database"]


def section(title):
    print(f"\n=== {title} ===")


# 1. Load both files
students = pd.read_csv(DATA_DIR / "students.csv")
scores = pd.read_csv(DATA_DIR / "scores.csv")

# 2. Check missing values
section("Missing values - students.csv")
print(students.isna().sum())
section("Missing values - scores.csv")
print(scores.isna().sum())

# 3. Fill or remove missing data appropriately
#    - We do NOT drop rows: the datasets are small (30 students), dropping would
#      lose students and distort the ranking.
#    - age   : median of all students (robust, ages are whole numbers)
#    - GPA   : mean GPA of the student's own major (students in a major are alike)
#    - scores: mean of the same subject over all students
students["age"] = students["age"].fillna(students["age"].median()).astype(int)
students["GPA"] = students["GPA"].fillna(students.groupby("major")["GPA"].transform("mean"))
scores[SUBJECTS] = scores[SUBJECTS].fillna(scores[SUBJECTS].mean())

section("Missing values after cleaning")
print(students.isna().sum().sum() + scores.isna().sum().sum(), "missing values left")

# 4. Merge the two datasets on student_id
merged = students.merge(scores, on="student_id", how="inner")
section("Merged dataset (first 5 rows)")
print(merged.head())
print("Shape:", merged.shape)

# 5. Calculate each student's average score
merged["avg_score"] = merged[SUBJECTS].mean(axis=1).round(2)
section("Average score of each student")
print(merged[["student_id", "name", "major", "avg_score"]])

# 6. Find the top 5 students
section("Top 5 students")
top5 = merged.sort_values("avg_score", ascending=False).head(5)
print(top5[["student_id", "name", "major", "avg_score"]].to_string(index=False))

# 7. Compute average score by major
section("Average score by major")
print(merged.groupby("major")["avg_score"].mean().round(2).sort_values(ascending=False))
