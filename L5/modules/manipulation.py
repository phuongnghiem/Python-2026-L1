def display_summary(df):
    """Hiển thị 5 dòng đầu tiên và số hàng/cột của DataFrame"""
    print("\n[Part 1] 5 dong dau tien trong danh sach:")
    print(df.head(5))
    rows, cols = df.shape
    print(f"\n[Part 1] Kich thuoc du lieu: {rows} hang, {cols} cot")

def select_name_and_gpa(df):
    """Lựa chọn và hiển thị 2 cột name và GPA"""
    print("\n[Part 1] Danh sach Name va GPA:")
    print(df[["name", "GPA"]])

def filter_students_by_gpa(df, min_gpa=3.5):
    """Lọc danh sách sinh viên có GPA >= min_gpa"""
    filtered = df[df["GPA"] >= min_gpa]
    print(f"\n[Part 1] Danh sach sinh vien co GPA >= {min_gpa}:")
    print(filtered)
    return filtered

def sort_students_by_gpa(df, ascending=False):
    """Sắp xếp danh sách sinh viên theo GPA"""
    sorted_df = df.sort_values(by="GPA", ascending=ascending)
    print("\n[Part 1] Danh sach sinh vien sap xep theo GPA (Giam dan):")
    print(sorted_df)
    return sorted_df