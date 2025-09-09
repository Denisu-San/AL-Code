def accum(string):
    temp_arr = []
        
    for index, item in enumerate(string.lower(), start=1):
        new_item = item.upper() + item*(index-1)
        temp_arr.append(new_item)
    # return temp_arr
    
    # TURNING CONTENTS OF SPLIT_ARR INTO A STRING
    final = "-".join(temp_arr)
    return final

print(accum("JIAsdasOIQn"))