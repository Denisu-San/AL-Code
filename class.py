class Employee:
    def __init__(self, name, staffno):
        self.__name = name
        self.__staffno = staffno
    def ShowDetails(self):
        print("Employee Name:", self.__name)
        print("Employee Staff Number:", self.__staffno)
        
mystaff = Employee("Chris Sinon", 18)
mystaff.ShowDetails()