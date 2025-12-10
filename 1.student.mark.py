Student_Number = int(input("type in a student number: "))

Student_information = list()

for i in range(1, Student_Number + 1):
    Name = input("type in student's name: ")
    ID = str(input("type in student's ID: "))
    DoB = str(input("type in the date  of birth of the student: "))
    Student_information.append({"Name": Name, "ID": ID, "DoB": DoB})
    print(Student_information)

Course_Number = int(input("type in the number of courses: "))

Course_information = list()

for i in range(1, Course_Number + 1):
    Course_Name = input("type in the course name: ")
    Course_ID = str(input("type in the course ID: "))
    Course_information.append({"Course_Name": Course_Name, "Course_ID": Course_ID})
    print(Course_information)

Mark_information = list()
print("The available courses are: ")
for course in Course_information:
    print(f"{course['Course_Name']} (ID: {course['Course_ID']})")

Selected_Course_ID = str(input("Type in the course ID you want to enter marks: "))
Course_Found = False
for course in Course_information:
    if course["Course_ID"] == Selected_Course_ID:
        Course_Found = True
        Current_Course_Name = course["Course_Name"]
        break
    if Course_Found:
        print(f"Entering marks for course: {course['Course_Name']}")

for student in Student_information:
    Mark = float(input(f"Type in the mark for {student['Name']} (ID: {student['ID']}): "))
    Mark_information.append({"Student_ID": student["ID"], "Course_ID": Selected_Course_ID, "Mark": Mark})
    print(Mark_information)

else:
    print(f"Course with ID {Selected_Course_ID} not found.")



