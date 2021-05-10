def makeArrayConsecutive2(statues):
    mat=list(sorted(statues))
    sum=0
    i=1
    while i<=(len(mat)-1):
        sum+=(mat[i]-mat[i-1]-1)
        #print(sum)
        i+=1
    return sum
    
print(makeArrayConsecutive2([6, 2, 3, 8]))