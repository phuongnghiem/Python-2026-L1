"""Labwork 5 - Task 1: Data Manipulation (students.csv)"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent  # CSV files live next to this script


def section(title):
    print(f"\n=== {title} ===")


# 1. Load the dataset
students = pd.read_csv(DATA_DIR / "students.csv")

# 2. Display first five rows
section("First five rows")
print(students.head())

# 3. Find number of rows and columns
section("Number of rows and columns")
rows, cols = students.shape
print(f"Rows: {rows}, Columns: {cols}")

# 4. Select name and GPA
section("Name and GPA")
print(students[["name", "GPA"]])

# 5. Find students with GPA >= 3.5 (students with missing GPA are not included)
section("Students with GPA >= 3.5")
high_gpa = students[students["GPA"] >= 3.5]
print(high_gpa)
print(f"-> {len(high_gpa)} students")

# 6. Sort students by GPA (descending; missing GPA goes last)
section("Students sorted by GPA (descending)")
print(students.sort_values("GPA", ascending=False))

# 7. Find average GPA by major (missing values are skipped)
section("Average GPA by major")
print(students.groupby("major")["GPA"].mean().round(3).sort_values(ascending=False))
