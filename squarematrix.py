def squarematrix(mat):
    size=len(mat)
    var = 2*size-1
    lis=[]
    print("var: " + str(var)) #tenho aqui as 7 variacoes (0 a 6)
    for i in range(var):
        lis.append([])
        #print(i)
        for j in range(size):
            for k in range(size):
                if k+j==i:
                    lis[i].append(mat[j][k])
    
    print(lis)
    for slis in lis:
        slis.sort(reverse=True)

    print(lis)
    

    for i in range(var):
        for j in range(size):
            for k in range(size):
                if k+j==i:
                    mat[j][k] = lis[i][0]
                    del lis[i][0]

    print(mat)

a = [[1, 3, 9, 4],
     [9, 5, 7, 7],
     [3, 6, 9, 7],
     [1, 2, 2, 2]]

squarematrix(a)

a = [[10, 1],
    [7, 5]]

squarematrix(a)

#0 0

#0 1
#1 0

#0 2
#1 1
#2 0

#0 3
#1 2
#2 1
#3 0

#1 3
#2 2
#3 1

#2 3
#3 2

#3 3