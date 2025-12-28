from input import get_input
from output import print_menu, show_message_box

import math
import curses 
from curses import wrapper
import numpy as np


class Student:
    def __init__(self, sid: int , name: str, dod: str):
        self._id = sid
        self._name= name
        self._dod= dod
        self._mark= []
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def dod(self):
        return self._dod
    
    @property
    def mark(self):
        return self._mark
    
    def add_mark(self, course: str, score: int, credits):
        self._mark.append((course, score, credits))
    
    def __str__(self):
        if self._mark:
            return f"({self._id}. '{self._name}', '{self._dod}', '{self._mark}')"
        else: 
            return f"({self._id}. '{self._name}', '{self._dod}')"
        
    

class Course:
    def __init__(self, cid: int, name: str, credit: int):
        self._id=cid
        self._name= name
        self._mark = []
        self._credits = credit
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def credit(self):
        return self._credits 

    def add_mark(self, student_name: str, score: str):
        self._mark.append((student_name, score))

    @property
    def mark(self):
        return self._mark
    
    def __str__(self):
        if self._mark:
            return f"({self._id}, '{self._name}', {self._mark})"
        else:
            return f"({self._id}, '{self._name}')"


class Markmanager:
    def __init__(self):
        self._student= []
        self._courses= []

    def input_student(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0,"--input student--")

        n_str = get_input(stdscr, 2, 0,"Type in the number of student: ")
        n= int(n_str)
        for i in range (1, n+1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Student {i}/{n} ---")

            sid_str = get_input(stdscr,2,0,f'ID student {i}: ')
            sid= int(sid_str)

            name = get_input(stdscr, 3, 0, f'Name student {i}: ')
            
            dob= get_input(stdscr, 4, 0, f'DoB student {i}: ')

            self._student.append(Student(sid, name, dob))

    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0,"--input course--")

        n_str = get_input(stdscr, 2, 0,"Type in the number of Course: ")
        n = int(n_str)

        for i in range(1, n + 1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Course {i}/{n} ---")

            cid_str = get_input(stdscr,2,0,f'ID course {i}: ')
            cid = int(cid_str)

            name = get_input(stdscr, 3, 0, f'Name course {i}: ')

            credit=get_input(stdscr, 4, 0, f'Credit course {i}: ')

            self._courses.append(Course(cid, name, credit))
    
    def input_marks_for_course(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0,"--input mark for course--")
        
        cid_str = get_input(stdscr,2,0,f'Type the id of the course to write mark:  ')
        cid = int(cid_str)

        course = self.find_course(cid)

        if not course:
            show_message_box(stdscr, "ERROR", [f'Course with ID {cid} not found'])
            return 
        count=0
        for student in self._student:
            stdscr.clear()
            stdscr.addstr(0, 0, f"--- Student: {student.name} with id: {student.id}:  ---")

            score_str = get_input(stdscr, 2, 0 , f'Mark: ')
            score = math.floor(float(score_str))

            course.add_mark(student.name, score)
            student.add_mark(course.name, score, course.credit)
            count+=1

    def find_course(self, id:int):
        for course in self._courses:
            if(course.id == id):
                return course
        return None

    def find_student(self,id:int):
        for astudent in self._student:
            if(id==astudent.id):
                return astudent
        return None

    def GPA(self, scores: list, credit: list):
        np_scores = np.array(scores, dtype=float)
        np_credits = np.array(credit, dtype=float)

        if np_scores.size == 0 or np_credits.size == 0:
            return 0.0
        
        gpa = float(np.average(np_scores, weights=np_credits))

        return gpa

    def calculate_GPA(self, stdscr):
        stdscr.clear()
        
        stdscr.addstr(0, 0, "--calculate GPA of student--")

        sID_str = get_input(stdscr, 2, 0, f'ID student to calculate: ')
        sID=int(sID_str)

        student=self.find_student(sID)

        if student is None:
            stdscr.addstr(stdscr, 3, 0,f"student with ID {sID} not found")
            return
        
        marks = student.mark
        scores = [score for [_course, score, credit] in marks]
        credits = [credit for [_course, score, credit] in marks]

        if not scores:
            stdscr.addstr(stdscr, 3, 0,f"No mark available for student {sID}")
            return

        gpa = self.GPA(scores, credits)

        show_message_box(stdscr, "RESULT", [f"Student: {student.name}", f"ID: {student.id}", f"GPA: {gpa:.2f}"])

    def show_list_GPA(self, stdscr):
        stdscr.clear()
        
        stdscr.addstr(0, 0, "--List GPA--")
        
        line=[]

        for astudent in self._student:
            marks = astudent.mark

            scores = [score for [_course, score, credit] in marks]
            credits = [credit for [_course, score, credit] in marks]

            if not scores:
                line.append(f"Student {astudent.name} (ID {astudent.id}): N/A (no marks)")
                continue

            gpa = self.GPA(scores, credits)
            line.append(f"Student {astudent.name} (ID {astudent.id}) - GPA: {gpa:.2f}")

            show_message_box(stdscr, "CLASS GPA LIST", line)


    def show_student(self, stdscr):
            line = []
            for s in self._student:
                line.append(str(s))
            show_message_box(stdscr, "LIST OF STUDENTS", line)
    
    def show_course(self, stdscr):
        line = []
        for c in self._courses:
            line.append(str(c))

        show_message_box(stdscr, "LIST OF COURSES", line)