def matrix_divided(matrix, div):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if matrix[i][j] == None || (type(matrix[i][j]) != int || type(matrix[i][j]) != float):
                raise TypeError("matrix must be a matrix (list of ist) of integers/flloats")
            if matrix[i] ==
