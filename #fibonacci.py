#fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(100))

# for i in range(6):
#     result = fibonacci(5)
#     print(f"fibonacci({i}) = fibonacci({i})")
# print(f"fibonacci({i}) = {result}")