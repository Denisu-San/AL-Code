def TooMany(arr, val, max):
    counter = 0 
    for i in arr:
        if i == val:
            counter += 1 
    
    if counter > max:
        return print(True)
    else:
        return print(False)
    
    return 

TooMany(["g", "l", "f", "g", "g", "g"], "g", 3)