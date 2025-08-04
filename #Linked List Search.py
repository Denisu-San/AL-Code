#Linked List Search
linked_list = [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
linked_list_pointer = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,-1]
start_p = 4
null_p = -1

def find(i):
    found = False
    item_pointer = start_p
    while (item_pointer != null_p) and not found:
        if linked_list[item_pointer] == i:
            found = True
        else:
            item_pointer = linked_list_pointer[item_pointer]
    return item_pointer

#user input
item_s = int(input("please input the item you wish to find"))
result = find(item_s)
if result != -1:
    print(f"item found at pointer: {result}")
else:
    print("item not found")