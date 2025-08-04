def is_odd(num):
    if num <= 1:
        return False

    if num > 0:
        if (num+1)/6 == int((num+1)/6) or num == 2 or num == 3 or (num-1)/6 == int((num-1)/6):
            return print(True)
        else:
            return print(False)
        

is_odd(125)