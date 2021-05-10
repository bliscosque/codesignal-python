def almostIncreasingSequence(sequence):
    if (sorted(set(sequence)) == sequence):
        return True
        
    count=0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            mat2=list(sequence.copy())
            del mat2[i]
            if (sorted(set(mat2))==mat2):
                return True
            mat2=list(sequence.copy())
            del mat2[i+1]
            if (sorted(set(mat2))==mat2):
                return True

    
    return False
        
            
        
print(almostIncreasingSequence([1, 3, 2, 1])) #F
print(almostIncreasingSequence([1, 3, 2])) #T
print(almostIncreasingSequence([1, 2, 1, 2])) #F
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5])) #T
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6])) #T
