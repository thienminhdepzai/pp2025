# Student_Number = int(input("type in a student number: "))

# Student_information = list()

# for i in range(1, Student_Number + 1):
#     Name = input("type in student's name: ")
#     ID = str(input("type in student's ID: "))
#     DoB = str(input("type in the date  of birth of the student: "))
#     Student_information.append({"Name": Name, "ID": ID, "DoB": DoB})
#     print(Student_information)

# Course_Number = int(input("type in the number of courses: "))

# Course_information = list()

# for i in range(1, Course_Number + 1):
#     Course_Name = input("type in the course name: ")
#     Course_ID = str(input("type in the course ID: "))
#     Course_information.append({"Course_Name": Course_Name, "Course_ID": Course_ID})
#     print(Course_information)

# Mark_information = list()
# print("The available courses are: ")
# for course in Course_information:
#     print(f"{course['Course_Name']} (ID: {course['Course_ID']})")

# Selected_Course_ID = str(input("Type in the course ID you want to enter marks: "))

# for student in Student_information:
#     Mark = float(input(f"Type in the mark for {student['Name']} (ID: {student['ID']}): "))
#     Mark_information.append({"Student_ID": student["ID"], "Course_ID": Selected_Course_ID, "Mark": Mark})
#     print(Mark_information)

class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id


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
            self.courses.append(Course(name, cid))

    def input_marks(self):
        print("Available courses:")
        for c in self.courses:
            print(c.course_id, "-", c.name)

        selected = input("Enter course ID to input marks: ")

        for s in self.students:
            mark = float(input(f"Enter mark for {s.name}: "))
            self.marks.append(Mark(s.student_id, selected, mark))


def main():
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()


if __name__ == "__main__":
    main()

