def allLongestStrings(inputArray):
    max=0
    for str in inputArray:
        if len(str) > max:
            max=len(str)
    
    nMat=[]
    for str in inputArray:
        if len(str) == max:
            nMat.append(str)
    
    return nMat




inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))