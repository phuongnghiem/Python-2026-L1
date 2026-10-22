"""
Extra feature (labwork5a):
- Export students / courses / marks to CSV
- Load with Pandas
- Query function that accepts conditions like: name = "Mr. Volunteers"
"""

import csv
import os
import pandas as pd
from domains import Student, Course, Mark


def export_to_csv(students, courses, marks):
    # students.csv
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "dob", "gpa"])
        for s in students:
            writer.writerow([s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()])
    print("→ Exported students.csv")

    # courses.csv
    with open("courses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "credits"])
        for c in courses:
            writer.writerow([c.get_id(), c.get_name(), c.get_credits()])
    print("→ Exported courses.csv")

    # marks.csv
    with open("marks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "course_id", "mark"])
        for m in marks:
            writer.writerow([m.get_student_id(), m.get_course_id(), m.get_mark()])
    print("→ Exported marks.csv")


def query_students(condition: str):
    """
    Simple query parser.
    Supported examples:
        name = "Nguyen Van A"
        gpa > 3.5
        id = "S001"
    """
    if not os.path.exists("students.csv"):
        print("students.csv not found. Please export first.")
        return

    df = pd.read_csv("students.csv")
    print("\nLoaded students DataFrame:")
    print(df)
    print()

    condition = condition.strip()
    try:
        # Very simple parser: column operator value
        for op in [">=", "<=", "!=", "==", "=", ">", "<"]:
            if op in condition:
                col, val = condition.split(op, 1)
                col = col.strip()
                val = val.strip().strip('"').strip("'")
                if op == "=":
                    op = "=="
                # Try numeric conversion
                try:
                    val = float(val)
                except ValueError:
                    pass
                query_str = f"`{col}` {op} @val"
                result = df.query(query_str, local_dict={"val": val})
                print(f"Query result for: {condition}")
                print(result if not result.empty else "No matching rows.")
                return
        print("Could not parse condition. Use format: column operator value")
    except Exception as e:
        print(f"Query error: {e}")


if __name__ == "__main__":
    # Demo
    print("This module provides export_to_csv() and query_students()")
    print("Example usage from main program after you have data:")
    print('  export_to_csv(students, courses, marks)')
    print('  query_students(\'name = "Nguyen Van A"\')')
    print('  query_students("gpa >= 3.5")')
