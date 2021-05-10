def shapeArea(n):
    m=[]
    for i in range(n+1):
        if i<=1:
            m.append(i)
        else:
            m.append(m[i-1]+4*(i-1))
    print(m)
    return m[-1]

shapeArea(3)