import os
import zipfile

from domain.models import Student 
from domain.models import Course
from domain.models import Markmanager

def extract_all_data():
    info_dir = "info"

    if os.path.exists("student.data"):
        zipf = zipfile.ZipFile("student.data","r")
        zipf.extractall(info_dir)

        zipf.close()
    

def load_data_student():

    students = []

    info_dir = "info"
    student_file = os.path.join(info_dir, "students.txt")
    
    if not os.path.exists("info/students.dat"):
        return students
    else: 
        f= open(student_file, "r", encoding="utf-8")
                
        for line in f:    
            parts = line.strip().split("|") 
            if len(parts) == 3:
                new_student = Student(int(parts[0]), parts[1], parts[2])
                students.append(new_student)
            
        f.close()
    
    marks = []

    info_dir = "info"
    mark_file= os.path.join(info_dir, "marks.txt")

    if not os.path.exists("info/marks.txt"):
        return marks
    else:
        f = open(mark_file, "r", encoding="utf-8")

        for line in f:
            parts = line.strip().split("|")

            if len(parts) == 4: 
                marks.append((int(parts[0]), int(parts[1]), int(parts[2], int(parts[3]))))

        f.close()
    
    student_dict = {s.id: s for s in students}

    for course_id, tinchi, student_id, score in marks:
        student = student_dict.get(student_id)

        if student: 
            student.add_mark(course_id, tinchi, score)

    return students


def load_data_course():
    courses= []

    info_dir = "info"
    courses_file = os.path.join(info_dir, "courses.txt")

    if not os.path.exists("info/courses.txt"):
        return courses
    else:
        f = open(courses_file, "r", encoding="utf-8")

        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                new_course = Course(int(parts[0]), parts[1], int(parts[2]))
                courses.append(new_course)

    return courses
    
        