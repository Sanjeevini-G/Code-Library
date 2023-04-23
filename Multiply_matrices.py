def multiply_matrices(mat1, mat2):
    # Get the number of rows and columns in the matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    
    # Check if the matrices can be multiplied
    if cols1 != rows2:
        print("The matrices cannot be multiplied.")
        return None
    
    # Create a new matrix with the appropriate dimensions
    result = [[0 for j in range(cols2)] for i in range(rows1)]
    
    # Multiply the matrices element-wise and sum the results
    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    # Return the resulting matrix
    return result
