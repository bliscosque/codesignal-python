def boundedRatio(a, l, r):
    pos = 1
    ret = []
    for num in a:
        if (num%pos != 0):
            #print("r1")
            pos+=1
            ret.append(False)
            continue
        if l<=(num/pos)<=r:
            #print("r2")
            ret.append(True)
            pos+=1
            continue
        ret.append(False)
        pos+=1
        #print("r3")
    return ret

a = [8, 5, 6, 16, 5]
l = 1
r = 3
print(boundedRatio(a,l,r))

#boundedRatio(a, l, r) = [false, false, true, false, true]
#b[i] = true 