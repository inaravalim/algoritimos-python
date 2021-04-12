from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# definindo as sequencias
Sa = Seq('ACTCGT')
Sb = Seq('ATTCG')

# realizando o alinhamento global usando o algoritmo Needleman-wunsch
alinha_glob = pairwise2.align.globalxx(Sa, Sb)

# imprimindo uma lista de alinhamento globais possiveis
# print(alinha_glob)

# imprimindo o 1 alinhamento possivel de maneira formatada
# print(format_alignment(*alinha_glob[1]))

# para ver todos os alinhamento possiveis podemos imprimir usando um loop for

for i in alinha_glob:
    print(format_alignment(*i))
