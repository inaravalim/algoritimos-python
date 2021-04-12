import numpy as np

a = np.array([1, 2, 3, 4, 5])
a.min()  # valor minimo
a.max()  # Valor maximo
a.sum()  # soma de todos elementos
# Todos tem essa propriedade
a.sum(0)  # soma de cada coluna
a.sum(1)  # soma de cada linha
a.cumsum()  # soma acumulativa
a.mean()  # media
a.std()  # desvio padrao

