import numpy as np

false = np.zeros((2, 2), dtype='bool')
matriz1 = np.random.randint(0, 10, (3, 3))
sel = matriz1 > 5  # cria matriz de vdd ou false
matriz2 = matriz1[sel]  # pega os valores vdd

sel2 =(matriz1>3) &(matriz1<5) # forma matriz de vdd ou false
