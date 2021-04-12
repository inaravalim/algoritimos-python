file = open('entrada.txt', 'r')
# pode escolher quantos caracteres quer ler colocando dentro do read
# print(file.read())
# le uma linha
texto = file.readlines()
for i in texto:
    print(i, end='')
file.close()

