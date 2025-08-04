#create an array to store the number
MyList = [9, 21, 16, 2, 5, 4, 37, 20, 15, 8]

#enter item to search
item = int(input("Enter the item to be found"))
found = False

# We find the length of the array and use it as a range value
# This makes it so that we can use the value in the range as an index to the list MyList
# And if the value/item that we get from that same index we derived is equal to the item we wanted to search
# It will give us either an output of "Item found" or else "Item not found"

for index in range(len(MyList)):
    if MyList[index] == item:
        found = True
        break
        if found:
            print("Item found")
            
        else:
            print("Item not found")