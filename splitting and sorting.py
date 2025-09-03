def splitSentence(a):
    a = str(a)
    arr = [int(char) for char in a]
    new = sorted(arr)
    return new
print(splitSentence((12938123)))