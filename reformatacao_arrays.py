import numpy as np

matriz1 = np.ones((4, 4))
matriz2 = np.ones((3, 4))
reformatacao1 = matriz1.reshape(12, 1)
reformatacao2 = matriz1.reshape(-1, 2)  # o -1 significa que coloca em quantas linhas for precisa

# concatenacao
concatenacao1 = np.vstack((matriz1, matriz2))  # vetical
concatenacao2 = np.concatenate((matriz1, matriz2), axis=0)  # 0-vertica 1-horizonta

repeticao = np.tile(matriz1, (2, 1))  # Repete a matriz1 duas vezes na vertical e uma vez na hori
