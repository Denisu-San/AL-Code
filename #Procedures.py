#Procedures
def InputPositiveNumber():
    Number = -1
    while Number <= 0:
        Number = int(input("Enter a positive Number"))
        print(Number)

InputPositiveNumber()