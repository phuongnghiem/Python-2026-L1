# Lab 5: Data Manipulation with Pandas

import pandas as pd

print("=" * 50)
print("PART 1: Basic analysis on students.csv")
print("=" * 50)

# Load the dataset
df = pd.read_csv("../data/students.csv")
print("\n1. Dataset loaded successfully.")

# Display first five rows
print("\n2. First five rows:")
print(df.head())

# Number of rows and columns
print(f"\n3. Shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Select name and GPA
print("\n4. Name and GPA:")
print(df[["name", "GPA"]])

# Students with GPA >= 3.5
print("\n5. Students with GPA >= 3.5:")
print(df[df["GPA"] >= 3.5])

# Sort students by GPA
print("\n6. Students sorted by GPA (descending):")
print(df.sort_values("GPA", ascending=False))

# Average GPA by major
print("\n7. Average GPA by major:")
print(df.groupby("major")["GPA"].mean().round(2))


print("\n" + "=" * 50)
print("PART 2: From raw data to useful info")
print("=" * 50)

# Load both files
students = pd.read_csv("../data/students.csv")
scores = pd.read_csv("../data/scores.csv")
print("\n1. Both files loaded.")

# Check missing values
print("\n2. Missing values in students:")
print(students.isnull().sum())
print("\n   Missing values in scores:")
print(scores.isnull().sum())

# Fill or remove (no missing in sample, but example)
students = students.dropna()  # or fillna if needed
scores = scores.dropna()

# Merge the two datasets
merged = pd.merge(students, scores, on="student_id")
print("\n3. Merged dataset:")
print(merged)

# Calculate each student's average score
merged["avg_score"] = merged[["math", "python", "db"]].mean(axis=1).round(2)
print("\n4. Average score per student:")
print(merged[["name", "avg_score"]])

# Top 5 students
print("\n5. Top 5 students by average score:")
print(merged.nlargest(5, "avg_score")[["name", "avg_score", "major"]])

# Average score by major
print("\n6. Average score by major:")
print(merged.groupby("major")["avg_score"].mean().round(2))
