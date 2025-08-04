#objects-class
class Student:
    def __init__(self, age, name, birthyear):
        self.__age = age
        self.__name = name 
        self.__birthyear= birthyear
    def ShowDetails(self):
        print("Age:", self.__age)
        print("Name:", self.__name)
        print("Birth Year:", self.__birthyear)

person = Student(18, "Robert Garcia", 2006)
# Student(18, "Robert Garcia", 2006).ShowDetails()
person.ShowDetails()

