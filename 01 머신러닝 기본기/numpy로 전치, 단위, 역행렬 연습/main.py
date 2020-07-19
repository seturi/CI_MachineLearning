import numpy as np

A = np.array([
    [1, -1, 2],
    [3, 2, 2]
])

B = np.array([
    [0, 1],
    [-1, 1],
    [5, 2]
])

C = np.array([
    [2, -1],
    [-3, 3]
])

D = np.array([
    [-5, 1],
    [2, 0]
])

# 행렬 연산을 result 변수에 저장하세요
A_transpose = np.transpose(A)
B_transpose = np.transpose(B)
C_inverse = np.linalg.pinv(C)
D_transpose = np.transpose(D)

result = B_transpose @ (2 * A_transpose) @ (3 * C_inverse + D_transpose)

result