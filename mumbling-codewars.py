# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(string):
    index = 0
    temp_arr = []
    
    split_arr = [str(i) for i in string.lower()]
    # return split_arr
    
    for item in split_arr:
        index += 1
        new_item = item.upper() + item*(index-1)
        temp_arr.append(new_item)
    # return temp_arr
    
    # TURNING CONTENTS OF SPLIT_ARR INTO A STRING
    final = "-".join(temp_arr)
    return final


print(accum("JIAsdas"))