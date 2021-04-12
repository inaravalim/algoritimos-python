import numpy as np

# Forma mais simples de criar array
matriz = np.array([[1, 2, 3], [4, 5, 6], [3, 6, 7]])
m = [[1, 2, 3], [4, 5, 6], [3, 6, 7]]
matriz2 = np.array(m)

# Pegar todos elementos
matriz2[0, :]

# criar Array sequencia e passo 2
matriz3 = np.arange(0, 10, 2)

# Criar array de ZERO formato(2,2) e depoi um
matriz4 = np.zeros((2, 2))
matriz5 = np.ones((2, 2))

# Cria vetor de zero/ om do mesmo formato que outro
matriz6 = np.zeros_like(matriz2)

# Elementos igualmente espaçados de tamanho T- inicial, final, quantidade T
matriz7 = np.linspace(0, 1, 5)

# numeros aleatorios int- min,max,formato
matriz8 = np.random.randint(0, 10, (3, 3))

# igualmente espaçados
matriz9 = np.linspace(0, 2 * np.pi, 3)
# Dimensao
matriz2.ndim
# Formato
matriz2.shape
# Qntd de elementos
matriz2.size
# Tipo dos elementos
matriz2.dtype
