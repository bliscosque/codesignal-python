def mostFrequentDigits(a):
    mat={ i:0 for i in range(10)}
    print(mat)

    for i in a:
        if i< 10:
            mat[i] +=1
        elif i <100:
            mat[i//10]  +=1
            mat[i%10] +=1
    print(mat)
    
    
    sorted_keys = sorted(mat, key=mat.get, reverse=True)  
    ret = []
    max=mat[sorted_keys[0]]
    #print(max)
    for i in sorted_keys:
        if mat[i] == max:
            ret.append(i)
    return ret
    


a = [25, 2, 3, 57, 38, 41]
print(mostFrequentDigits(a))
