#Linear Search
def search(v, arr):
#Counting number of items in array/ indices
    index = 0
    for i in arr:
        if v == i:
            return index
        index += 1       
    # else:
    #     print("Not in List")
    return -1
        
result = search(1, [2, 12, 6, 7, 77, 1, 0])
print(f"value at index: {result}")

