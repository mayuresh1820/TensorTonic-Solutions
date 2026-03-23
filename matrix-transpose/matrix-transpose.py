import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A, copy=True)   # copy=True ensures original is never modified
    M, N = A.shape                # M rows, N cols

    result = np.empty((N, M), dtype=A.dtype)

    for i in range(M):
        for j in range(N):
            result[j][i] = A[i][j]   # swap indices

    return result
    
