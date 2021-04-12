from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# definindo as sequencias
Sa = Seq('ACTCGTCTTGCT')
Sb = Seq('ATTCGTTGAC')

# realizando o alinhamento global e saindo somente o valores dos scores
score_only= pairwise2.align.globalxx(Sa,Sb,one_alignment_only = True, score_only=True)

#imprimindo o alinhamento global com maior score
print(score_only)

# calculando a porcentagem, de similaridade do alinhamento  score/comprimento sequencia sa
similaridade = 100*score_only/len(Sa)
print(similaridade)