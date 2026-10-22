"""Persistence module: compress / decompress using zipfile + pickle"""
import os
import zipfile
import pickle
from domains import Student, Course, Mark


def compress_data(students, courses, marks, filename="students.dat"):
    """Serialize objects and compress into students.dat"""
    data = {
        "students": [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in students],
        "courses": [(c.get_id(), c.get_name(), c.get_credits()) for c in courses],
        "marks": [(m.get_student_id(), m.get_course_id(), m.get_mark()) for m in marks],
    }
    # First write pickle
    with open("temp_data.pkl", "wb") as f:
        pickle.dump(data, f)

    # Compress with zip
    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write("temp_data.pkl", "data.pkl")
        # Also include the text files if they exist
        for txt in ["students.txt", "courses.txt", "marks.txt"]:
            if os.path.exists(txt):
                zf.write(txt)

    os.remove("temp_data.pkl")
    print(f"→ Compressed data to {filename}")


def decompress_and_load(filename="students.dat"):
    """Decompress students.dat and return students, courses, marks lists"""
    if not os.path.exists(filename):
        return [], [], []

    with zipfile.ZipFile(filename, "r") as zf:
        zf.extract("data.pkl")

    with open("data.pkl", "rb") as f:
        data = pickle.load(f)

    os.remove("data.pkl")

    students = []
    for sid, name, dob, gpa in data.get("students", []):
        s = Student(sid, name, dob)
        s.set_gpa(gpa)
        students.append(s)

    courses = []
    for cid, name, credits in data.get("courses", []):
        courses.append(Course(cid, name, credits))

    marks = []
    for sid, cid, mark in data.get("marks", []):
        marks.append(Mark(sid, cid, mark))

    print(f"→ Loaded data from {filename}")
    return students, courses, marks
