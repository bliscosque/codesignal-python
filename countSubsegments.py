def countSubsegments(arr):
    count=0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            s1=sum(arr[:i])
            s2=sum(arr[i:j])
            s3=sum(arr[j:])
            #print(i,j,s1,s2,s3)
            if s1<=s2<=s3:
                count+=1

    return count

arr = [1, 1, 1]
print(countSubsegments(arr))
arr = [1, 2, 0]
print(countSubsegments(arr))
arr = [1, 2, 2, 2, 5, 0]
print(countSubsegments(arr))