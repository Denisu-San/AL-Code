import math

def amount(a):
    
    points = 0

    roundedAmount = math.floor(a) #int(a) also works
    if roundedAmount < 10:
        points = roundedAmount * 5
    elif roundedAmount < 100:
        points = roundedAmount * 7
    elif roundedAmount > 100:
        points = roundedAmount * 10
    
    print(points)
    return

amount(96.87)

