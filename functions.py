def InputPositiveNumber():
    Number = -1
    while Number <= 0:
        Number = int(input("Enter a Positive Number"))
    return Number

InputPositiveNumber()
