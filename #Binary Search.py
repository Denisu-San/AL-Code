#Binary Search
MyList = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
Item = int(input("Enter item to be found"))
Lower = 0
Upper = len(MyList) - 1
Found = False

while Lower <= Upper:
    Mid = (Upper + Lower)//2  #// is for integer division so the 0.5 is discarded from the calculation
    if MyList[Mid] == Item:
        Found = True
        break
    elif Item > MyList[Mid]:
        Lower = Mid + 1
    else:
        Upper = Mid - 1
        
print("Item found" if Found else "Item not found")
