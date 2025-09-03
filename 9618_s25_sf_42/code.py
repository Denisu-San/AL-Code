MAX = 20
Stack = ["-1"]*MAX
TopOfStack = -1

#main
def push(str):
    global Stack, TopOfStack
    if len(Stack) >= MAX:
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = str
        return 1

def pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return "-1"
    else:
        TopOfStack -= 1
        #Stack[TopOfStack] = "-1"
        return Stack[TopOfStack]
    

def ReadData(filename):
    global Stack, TopOfStack
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip()
                result = push(data)
                if result == -1:
                    print("Stack full")
                    break
    except:
        print("Cannot open file")
    
    
    # except IOError:
    #     print( f"ERROR: Could not read file '{filename}'")
    # except FileNotFoundError:
    #     print( f"ERROR: File '{filename}' could not be found")
    # #commented out because it cannot work with a catch-all except condition like the one above

#note that the order of values stored is number-operator-number.....
def Calculate():
    global Stack, TopOfStack
    if TopOfStack == -1:
        print("Stack is empty")
        
    total_str = pop() #value stored as string in the stack so we pop it out and convert
    total = float(total_str)
    
    while TopOfStack != -1:
        operator = pop()
        # if TopOfStack == -1:
        #     break #this is for when we have no number after an operator
        num_str = pop()
        num = float(num_str)
        
        if operator == "+":
            total += num
        elif operator == "-":
            total -= num
        elif operator == "*":
            total *= num
        elif operator == "/":
            total /= num
        elif operator == "^":
            total **= num
        else:
            print(f"unknown operator: {operator}")
    
    return total

FileName = input("Enter the fielname")
ReadData(FileName)
answer = Calculate()
print("answer")
