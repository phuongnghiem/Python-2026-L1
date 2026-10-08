import modules as mod

def main():
    # 0. Tự động kiểm tra và khởi tạo file dữ liệu nếu thiếu
    mod.ensure_sample_data()

    print("       PART 1: DATA MANIPULATION (students.csv)   ")
    
    # 1. Load the dataset[cite: 9]
    students_df = mod.load_csv("students.csv")
    print("-> Nap thanh cong file 'students.csv'")
    
    # 2 & 3. Display first 5 rows and find shape[cite: 9]
    mod.display_summary(students_df)
    
    # 4. Select name and GPA[cite: 9]
    mod.select_name_and_gpa(students_df)
    
    # 5. Find students with GPA >= 3.5[cite: 9]
    mod.filter_students_by_gpa(students_df, min_gpa=3.5)
    
    # 6. Sort students by GPA[cite: 9]
    mod.sort_students_by_gpa(students_df, ascending=False)
    
    # 7. Find average GPA by major[cite: 9]
    mod.compute_avg_gpa_by_major(students_df)


    print("    PART 2: FROM RAW DATA TO USEFUL INFO          ")
    
    # 1. Load both files[cite: 10]
    scores_df = mod.load_csv("scores.csv")
    print("-> Nap thanh cong file 'scores.csv'")
    
    # 2. Check missing values[cite: 10]
    mod.check_missing_values(students_df, "students.csv")
    mod.check_missing_values(scores_df, "scores.csv")
    
    # 3. Fill or remove missing data appropriately[cite: 10]
    students_clean, scores_clean = mod.clean_missing_data(students_df, scores_df)
    print("\n-> Da xu ly xong gia tri khuyet (NaN).")
    
    # 4. Merge the two datasets[cite: 10]
    merged_df = mod.merge_student_scores(students_clean, scores_clean)
    
    # 5. Calculate each student's average score[cite: 10]
    merged_df = mod.compute_student_avg_score(merged_df)
    
    # 6. Find the top 5 students[cite: 10]
    mod.get_top_students(merged_df, top_n=5)
    
    # 7. Compute average score by major[cite: 10]
    mod.compute_avg_score_by_major(merged_df)

if __name__ == "__main__":
    main()