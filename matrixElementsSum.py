def matrixElementsSum(matrix):
    lin=len(matrix)
    col=len(matrix[0])
    print(lin, col)
    sum = 0
    for j in range(col):
        for i in range(lin):
            print (i, j, matrix[i][j])
            if matrix[i][j] == 0:
                break
            sum += matrix[i][j]
    
    return sum