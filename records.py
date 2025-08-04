import pickle
from datetime import datetime

class Student:
    def __init__(self):
        self.name = ""
        self.registerNumber = 0
        self.dateOfBirth = None
        self.fullTime = True

studentRecords = []
while True:
    student = Student()
    student.name = input("Enter student name(or press enter to finish): ")
    if student.name == "":
        break
    student.registerNumber = int(input("Enter register number: "))
    student.dateOfBirth = input("Enter date of birth (YYYY-MM-DD): ")
    try:
        student.dateOfBirth = datetime.strptime(student.dateOfBirth, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        continue

    student.fullTime = (input("Enter True for full-time, or false for part-time: ") == "True")
    studentRecords.append(Student)
    
studentRecords.sort(key = lambda x: x.registerNumber)
with open("Student.dat", "wb") as file:
        pickle.dump(studentRecords, file)
print("Student records Saved to student.dat")