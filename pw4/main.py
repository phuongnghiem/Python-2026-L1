import curses
import input as ui_input
import output as ui_output


def main(stdscr):
    curses.curs_set(0)
    students = []
    courses = {}

    while True:
        if not ui_output.display_menu(stdscr, len(students), len(courses)):
            continue

        key = stdscr.getch()

        if key == ord('1'):
            new_students = ui_input.input_students(stdscr)
            if new_students:
                students.extend(new_students)
                ui_output.display_notification(stdscr, f"Them thanh cong {len(new_students)} sinh vien!")
            else:
                ui_output.display_notification(stdscr, "So luong khong hop le hoac bi huy!")

        elif key == ord('2'):
            new_courses = ui_input.input_courses(stdscr)
            if new_courses:
                courses.update(new_courses)
                ui_output.display_notification(stdscr, f"Them thanh cong {len(new_courses)} mon hoc!")
            else:
                ui_output.display_notification(stdscr, "So luong khong hop le hoac bi huy!")

        elif key == ord('3'):
            if not courses:
                ui_output.display_notification(stdscr, "Chua co mon hoc nao trong he thong!")
                continue
            if not students:
                ui_output.display_notification(stdscr, "Chua co sinh vien nao trong he thong!")
                continue

            success, msg = ui_input.input_marks_for_course(stdscr, students, courses)
            ui_output.display_notification(stdscr, msg)

        elif key == ord('4'):
            if not students:
                ui_output.display_notification(stdscr, "Danh sach sinh vien dang trong!")
                continue

            # Tính điểm GPA cho toàn bộ sinh viên
            for s in students:
                s.calculate_gpa(courses)

            # Sắp xếp giảm dần theo GPA
            students.sort(key=lambda s: s.gpa, reverse=True)

            ui_output.display_students_gpa(stdscr, students)

        elif key == ord('5'):
            break


if __name__ == "__main__":
    curses.wrapper(main)