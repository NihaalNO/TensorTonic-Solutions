import numpy as np

def matrix_transpose(A):
    A = np.asarray(A)
    n,m = A.shape

    t = np.zeros((m,n), dtype=A.dtype)
    for i in range(n):
        for j in range(m):
            t[j,i] = A[i,j]
    return t
    
    
