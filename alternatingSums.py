def alternatingSums(a):
    suma=0
    sumb=0
    pos=True
    for i in a:
        if pos:
            suma+=i
        else:
            sumb+=i
        pos=not pos
    
    return [suma, sumb]

a = [50, 60, 60, 45, 70]
print(alternatingSums(a))
        