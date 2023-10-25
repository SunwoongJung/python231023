import numpy as np

print("matrix")
matrix = np.array([[ 0, 1, 2, 3],
                   [ 4, 5, 6, 7],
                   [ 8, 9,10,11], 
                   [12,13,14,15]])
print(matrix, "\n")

# Q1. matrix를 [3] 행에서 axis 0으로 나누기
'''
[[0  1   2  3]
 [4  5   6  7]
 [8  9  10 11]],

 [12 13 14 15]
'''
a, b = np.split(matrix, [2], axis = 0)
print(a, "\n")
print(b, "\n")


