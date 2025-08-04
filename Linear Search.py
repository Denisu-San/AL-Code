MyList = [9,8,1,4,2,3,0,5,7]

#prompt the user to enter the no. to search

Item = int(input("Enter the item to be found:"))
found=False
for index in range(len(MyList)):
    if MyList [index]==Item:
        found=True
        break
if found:
    print("Item found")
else:
    print("Item not found")