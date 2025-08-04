MyList = [168, 23, 359, 284, 492, 274, 935, 841, 609, 718, 238, 613, 517, 739, 859, 672, 763, 965, 232, 637]
top = len(MyList)
swap = True

while (swap) or (top > 0):
    swap = False
    for i in range(top - 1):
        if MyList[i] > MyList[i + 1]:
            MyList[i], MyList[i + 1] = MyList[i + 1], MyList[i]
            swap = True
    top = top - 1

print(MyList)