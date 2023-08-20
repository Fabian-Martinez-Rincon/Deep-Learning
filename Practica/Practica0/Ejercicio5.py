import numpy as np

vector = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(vector[2]) # 2
print(vector[2:7]) # [2 3 4 5 6]

vector[5:8] = -1
print(vector) # [ 0  1  2  3  4 -1 -1 -1  8  9]


print('----------------------------------')

# Matrices (Arrays Bidimensionales)
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Acceso a elementos individuales
print(matriz[1, 2]) # 6

# Acceso a filas/columnas
print(matriz[1, :]) # [4 5 6]

print(matriz[:, 2]) # [ 3  6  9 12]

# Acceso a submatrices
print(matriz[1:3, 1:3])
# [[5 6]
#  [8 9]]

# Modificación de submatrices
matriz[2:4, 1:3] = 0
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  0  0]
#  [10  0  0]]

print('----------------------------------')


# Creación de un tensor
tensor = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 10], [11, 12]],
    [[13, 14], [15, 16], [17, 18]]
])

elemento_2_2_1 = tensor[1, 1, 0] # 9
matriz_2 = tensor[1, :, :]
# [[ 7  8]
#  [ 9 10]
#  [11 12]]
