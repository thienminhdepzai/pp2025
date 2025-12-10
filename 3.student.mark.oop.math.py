# class Student:
#     def __init__(self, name, student_id, dob):
#         self.name = name
#         self.student_id = student_id
#         self.dob = dob


# class Course:
#     def __init__(self, name, course_id):
#         self.name = name
#         self.course_id = course_id


# class Mark:
#     def __init__(self, student_id, course_id, mark):
#         self.student_id = student_id
#         self.course_id = course_id
#         self.mark = mark


# class School:
#     def __init__(self):
#         self.students = []
#         self.courses = []
#         self.marks = []

#     def input_students(self):
#         n = int(input("Number of students: "))
#         for _ in range(n):
#             name = input("Student name: ")
#             sid = input("Student ID: ")
#             dob = input("Date of birth: ")
#             self.students.append(Student(name, sid, dob))

#     def input_courses(self):
#         n = int(input("Number of courses: "))
#         for _ in range(n):
#             name = input("Course name: ")
#             cid = input("Course ID: ")
#             self.courses.append(Course(name, cid))

#     def input_marks(self):
#         print("Available courses:")
#         for c in self.courses:
#             print(c.course_id, "-", c.name)

#         selected = input("Enter course ID to input marks: ")

#         for s in self.students:
#             mark = float(input(f"Enter mark for {s.name}: "))
#             self.marks.append(Mark(s.student_id, selected, mark))


# def main():
#     school = School()
#     school.input_students()
#     school.input_courses()
#     school.input_marks()


# if __name__ == "__main__":
#     main()


import math
import numpy as np
import curses


class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.gpa = 0.0


class Course:
    def __init__(self, name, course_id, credits):
        self.name = name
        self.course_id = course_id
        self.credits = credits


class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            name = input("Student name: ")
            sid = input("Student ID: ")
            dob = input("Date of birth: ")
            self.students.append(Student(name, sid, dob))

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            name = input("Course name: ")
            cid = input("Course ID: ")
            credits = int(input("Credits: "))
            self.courses.append(Course(name, cid, credits))

    def input_marks(self):
        print("Available courses:")
        for c in self.courses:
            print(c.course_id, "-", c.name)

        selected = input("Enter course ID to input marks: ")

        for s in self.students:
            raw = float(input(f"Enter mark for {s.name}: "))
            mark = math.floor(raw * 10) / 10.0
            self.marks.append(Mark(s.student_id, selected, mark))

    def calc_gpa(self, student_id):
        scores = []
        credits = []
        for m in self.marks:
            if m.student_id == student_id:
                for c in self.courses:
                    if c.course_id == m.course_id:
                        scores.append(m.mark)
                        credits.append(c.credits)
        if not scores:
            return 0.0
        scores = np.array(scores)
        credits = np.array(credits)
        gpa = np.sum(scores * credits) / np.sum(credits)
        return round(gpa, 2)

    def update_all_gpa(self):
        for s in self.students:
            s.gpa = self.calc_gpa(s.student_id)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def curses_ui(self, stdscr):
        curses.curs_set(0)
        while True:
            stdscr.clear()
            stdscr.addstr("=== School Manager ===\n")
            stdscr.addstr("1. Show student list\n")
            stdscr.addstr("2. Show GPA\n")
            stdscr.addstr("3. Sort students by GPA\n")
            stdscr.addstr("4. Exit\n")
            stdscr.addstr("\nChoose: ")

            choice = stdscr.getch()

            if choice == ord("1"):
                stdscr.clear()
                for s in self.students:
                    stdscr.addstr(f"{s.name} - GPA: {s.gpa}\n")
                stdscr.addstr("\nPress any key...")
                stdscr.getch()

            elif choice == ord("2"):
                self.update_all_gpa()
                stdscr.clear()
                for s in self.students:
                    stdscr.addstr(f"{s.name}: {s.gpa}\n")
                stdscr.addstr("\nPress any key...")
                stdscr.getch()

            elif choice == ord("3"):
                self.update_all_gpa()
                self.sort_students_by_gpa()
                stdscr.clear()
                for s in self.students:
                    stdscr.addstr(f"{s.name}: {s.gpa}\n")
                stdscr.addstr("\nPress any key...")
                stdscr.getch()

            elif choice == ord("4"):
                break


def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()
    curses.wrapper(school.curses_ui)


if __name__ == "__main__":
    main()

