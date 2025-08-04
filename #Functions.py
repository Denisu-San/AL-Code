#Functions
def InputPositiveNumber():
    Number = -1
    while Number <= 0:
        Number = int(input("Enter a positive Number"))
    return Number
    
NewNumber = InputPositiveNumber()

