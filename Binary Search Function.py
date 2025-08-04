# MyList = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
# Item = int(input("Enter item to be found"))
# Lower = 0
# Upper = len(MyList) - 1
# Found = False

# while Lower <= Upper:
#     Mid = (Upper + Lower)//2  #// is for integer division so the 0.5 is discarded from the calculation
#     if MyList[Mid] == Item:
#         Found = True
#         break
#     elif Item > MyList[Mid]:
#         Lower = Mid + 1
#     else:
#         Upper = Mid + 1
# print("Item found" if Found else "Item not found")

def find_item(array, item):
    item = int(item)
    lower = 0
    upper = len(array) - 1
    found = False
    
    while lower <= upper:
        mid = (upper + lower)//2
        if array[mid] == item:
            found = True
            break
        elif item > array[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    return found
    print("Item found" if found else "Item not found")
    


find_item([2, 5, 8, 12, 34, 67, 89, 90, 110, 169, 209], 30)
