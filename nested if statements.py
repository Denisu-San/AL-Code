#nested if statements

age = int(input("Entre your age"))

if age > 18:
    print("You are an adult")
else:
    if age > 12:
        print("You are a teenager")
    else:
        print("You are a kid")