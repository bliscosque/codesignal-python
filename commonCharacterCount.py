def commonCharacterCount(s1, s2):
    l1=[0 for x in range(26)]
    l2=[0 for x in range(26)]
    
    for ch in s1:
        l1[ord(ch) - ord('a')] += 1

    for ch in s2:
        l2[ord(ch) - ord('a')] += 1
    
    #print(l1, l2)    
    sum=0
    
    for i in range(26):
        sum+=min(l1[i],l2[i])
        #print(i, sum)
        
    return sum

s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1,s2))