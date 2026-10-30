import os
import zipfile
import pickle

DATA_FILE = "students.dat"
TEMP_STUDENTS = "students.pkl"
TEMP_COURSES = "courses.pkl"


def load_data():
    students = []
    courses = {}

    if not os.path.exists(DATA_FILE):
        return students, courses

    try:
        with zipfile.ZipFile(DATA_FILE, 'r') as zip_ref:
            zip_ref.extractall(".")

        if os.path.exists(TEMP_STUDENTS):
            with open(TEMP_STUDENTS, 'rb') as f:
                students = pickle.load(f)
            os.remove(TEMP_STUDENTS)

        if os.path.exists(TEMP_COURSES):
            with open(TEMP_COURSES, 'rb') as f:
                courses = pickle.load(f)
            os.remove(TEMP_COURSES)

    except Exception as e:
        print(f"Error loading data: {e}")

    return students, courses


def save_data(students, courses):
    try:
        with open(TEMP_STUDENTS, 'wb') as f:
            pickle.dump(students, f)

        with open(TEMP_COURSES, 'wb') as f:
            pickle.dump(courses, f)

        with zipfile.ZipFile(DATA_FILE, 'w', compression=zipfile.ZIP_DEFLATED) as zip_ref:
            zip_ref.write(TEMP_STUDENTS)
            zip_ref.write(TEMP_COURSES)

        if os.path.exists(TEMP_STUDENTS):
            os.remove(TEMP_STUDENTS)
        if os.path.exists(TEMP_COURSES):
            os.remove(TEMP_COURSES)

    except Exception as e:
        print(f"Error saving data: {e}")