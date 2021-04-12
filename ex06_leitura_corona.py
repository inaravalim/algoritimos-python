file = open('corona_genomic.fasta', 'r')
texto = file.read()
aminoacidos = []
for i in texto:
    if (i == 'A') or (i == 'C') or (i == 'G') or (i == 'T'):
        aminoacidos.append(i)
print(aminoacidos)
file.close()
