MyList = [168, 23, 359, 284, 492, 274, 935, 841, 609, 718, 238, 613, 517, 739, 859, 672, 763, 965, 232, 637]

for index in range(1, len(MyList)):
    CurrentValue = MyList[index]
    SortedPos = 0
    InsPosFound = False
    
    while True:
        if CurrentValue > MyList[SortedPos]:
            SortedPos = SortedPos + 1
        else:
            InsPos = SortedPos
            InsPosFound = True
        if InsPosFound == True:
            break
        
    for ShufflePos in range(index, InsPos, -1):
        MyList[ShufflePos] = MyList[ShufflePos - 1]
        MyList[ShufflePos - 1] = CurrentValue
print(MyList)