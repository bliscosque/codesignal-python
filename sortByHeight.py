def sortByHeight(a):
    n_matrix=[i for i in a if i!=-1]
    n_matrix.sort()
    
    #print(n_matrix)
    
    pos=0
    for i in range(len(a)):
        if a[i] == -1:
            continue
        a[i]=n_matrix[pos]
        pos+=1
        #print(a)
        
    #print(a)
    return a
    