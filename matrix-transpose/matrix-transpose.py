import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    n, m = A.shape
    A_T = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            A_T[i][j] = A[j][i]
    return A_T
    # return np.array(A).T
