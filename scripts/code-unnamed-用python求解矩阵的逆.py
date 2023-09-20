import numpy as np

# 定义一个矩阵
A = np.array([[1, 2], [3, 4]])

# 使用numpy的linalg.inv()函数来找到它的逆
A_inv = np.linalg.inv(A)

print(f'逆矩阵 A^{{-1}}:\n {A_inv}')
# [[-2.   1. ]
# [ 1.5 -0.5]]