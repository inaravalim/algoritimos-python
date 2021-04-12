from Bio.Blast import NCBIWWW
from Bio.Seq import Seq
from Bio import SeqIO

# definindo uma sequencia
seqa =  SeqIO.read('Corona_genomic.fasta',format='fasta')
print(seqa.seq)
# iniciando o blast pelo biopython usando a API
print('Iniciando busca no NCBIWWW...' )
resultado = NCBIWWW.qblast("blastn", "nt",seqa.seq, format_type="Text")
print('busca concluida ')
saida = open("blast_resultado.xml", "w")
saida.write(resultado.read())
saida.close()