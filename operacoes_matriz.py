import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
# Igual para - * / ** escalar
soma = a + b
# multiplicacao de matriz AL
c = np.dot(a, b)

matriz_inversa = np.linalg.inv(a)
determinante = np.linalg.det(a)
transposta = a.transpose()
