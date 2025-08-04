def reverse_seq(n):
    if n > 0:
        return print(list(range(n, 0, -1)))
    else:
        return print("Value must be > 0")
    
reverse_seq(8091)