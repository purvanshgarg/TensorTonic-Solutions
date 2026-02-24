import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    transpose = [[row[i] for row in A] for i in range(len(A[0]))]
    return np.matrix(transpose)
    # Write code here
    pass
