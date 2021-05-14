def isLucky(n):
    n=str(n)
    print(n)
    n = [ord(i)-ord('0') for i in n ]
    print(n)
    
    size=len(n)
    print(size)
    met=size//2
    print(f'met {met}')
    
    m1=sum(n[:met])
    print(m1)
    m2=sum(n[met:])
    print(m2)
    
    return m1==m2

#Converter inteiro em lista de inteiros
#s = [int(x) for x in str(n)]