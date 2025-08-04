class Student:
    def __init__(s, name, studentid, age, course):
        s.__name = name
        s.__studentid = studentid
        s.__age = age
        s.__course = course
    def ShowDetails(s):
        print("Student Name:",  s.__name)
        print("StudentID Number:", s.__studentid)
        print("Student Age:", s.__age)
        print("Student Course:", s.__course)

pupil = Student("Chris Sinon", 8712, 18, "CS, Econ, Maths")
pupil.ShowDetails()