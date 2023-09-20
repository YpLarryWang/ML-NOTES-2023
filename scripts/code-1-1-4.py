import numpy as np

# 定义系数矩阵
A = np.array([[2, 3], [4, 5]])

# 定义常数向量
b = np.array([5, 7])

# 使用线性代数模块中的solve函数求解方程组
x = np.linalg.solve(A, b)

# 打印解向量
print("解向量 x:", x)
# 解向量 x: [-2.  3.]