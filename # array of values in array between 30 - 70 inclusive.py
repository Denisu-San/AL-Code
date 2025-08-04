# array of values 30 - 70 inclusive, output sum of values within said range

def sumofvals(arr):
    
    sum = 0
    
    for i in arr:
        if 30<=i<=70:
            sum += i
    print(sum)

sumofvals([22, 35, 64, 7, 20, 17, 81, 92, 63, 75, 87, 124, 1024, 2, 4, 8, 16, 32, 64, 128])
