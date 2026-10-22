"""Persistence with background thread + pickle + compression"""
import os
import zipfile
import pickle
import threading
from domains import Student, Course, Mark


def _save_worker(students, courses, marks, filename="students.dat"):
    """Worker function that runs in background thread"""
    data = {
        "students": [(s.get_id(), s.get_name(), s.get_dob(), s.get_gpa()) for s in students],
        "courses": [(c.get_id(), c.get_name(), c.get_credits()) for c in courses],
        "marks": [(m.get_student_id(), m.get_course_id(), m.get_mark()) for m in marks],
    }
    with open("temp_data.pkl", "wb") as f:
        pickle.dump(data, f)

    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write("temp_data.pkl", "data.pkl")
        for txt in ["students.txt", "courses.txt", "marks.txt"]:
            if os.path.exists(txt):
                zf.write(txt)

    if os.path.exists("temp_data.pkl"):
        os.remove("temp_data.pkl")
    print(f"\n[Background] → Compressed & saved to {filename}")


def compress_data_async(students, courses, marks, filename="students.dat"):
    """Launch save in a background thread"""
    thread = threading.Thread(
        target=_save_worker,
        args=(list(students), list(courses), list(marks), filename),
        daemon=True
    )
    thread.start()
    print("→ Saving data in background thread...")
    return thread


def decompress_and_load(filename="students.dat"):
    if not os.path.exists(filename):
        return [], [], []

    with zipfile.ZipFile(filename, "r") as zf:
        zf.extract("data.pkl")

    with open("data.pkl", "rb") as f:
        data = pickle.load(f)

    if os.path.exists("data.pkl"):
        os.remove("data.pkl")

    students = []
    for sid, name, dob, gpa in data.get("students", []):
        s = Student(sid, name, dob)
        s.set_gpa(gpa)
        students.append(s)

    courses = [Course(cid, name, credits) for cid, name, credits in data.get("courses", [])]
    marks = [Mark(sid, cid, mark) for sid, cid, mark in data.get("marks", [])]

    print(f"→ Loaded data from {filename}")
    return students, courses, marks
