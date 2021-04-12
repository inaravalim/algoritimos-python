from Bio.Seq import Seq
from Bio import pairwise2  # Funçoes de alinhamentos
from Bio.pairwise2 import format_alignment

# definindo as sequencias
Sa = Seq('ACTCGG')
Sb = Seq('TCG')

# realizando o alinhamento local usando o algoritmo Smith-Waterman
alinha_loc = pairwise2.align.localxx(Sa, Sb)

# imprimindo uma lista de alinhamento globais possiveis
# print(alinha_loc)

# imprimindo o 1 alinhamento possivel de maneira formatada
# print(format_alignment(*alinha_loc[0]))

# para ver todos os alinhamento possiveis podemos imprimir usando um loop for
for i in alinha_loc:
    print(format_alignment(*i))
Sa = Seq('ACTCGG')
Sb = Seq('TCG')
