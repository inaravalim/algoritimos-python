sequencia = str(input('Digite uma sequencia de DNA: ')).upper()
count_nucleo = len(sequencia)
count_A = count_C = count_G = count_T = 0
validade = True

for c in range(0, count_nucleo):
    if sequencia[c] == 'A':
        count_A = count_A + 1
    elif sequencia[c] == 'C':
        count_C = count_C + 1
    elif sequencia[c] == 'G':
        count_G = count_G + 1
    elif sequencia[c] == 'T':
        count_T = count_T + 1
    else:
        validade = False

# Verificar  validade
if not validade:
    print('A sequência digitada não é válida')
else:
    print('A sequência digitada é válida')
    print('O número total de nucleotideos da sequência digitada é {}'.format(count_nucleo))

    # Contador de base
    print('A sequência digitada possui:')
    print('{} Adenina (A)'.format(count_A))
    print('{} Guanina (G)'.format(count_G))
    print('{} Citosina (C)'.format(count_C))
    print('{} Timina (T)'.format(count_T))

    # Calculo de frequencia
    print('A frequência de nucleotideos é ')
    freq_A = float((100 * count_A) / count_nucleo)
    freq_C = float((100 * count_C) / count_nucleo)
    freq_G = float((100 * count_G) / count_nucleo)
    freq_T = float((100 * count_T) / count_nucleo)
    print('{}% Adenina (A)'.format(freq_A))
    print('{}% Guanina (G)'.format(freq_G))
    print('{}% Citosina (C)'.format(freq_C))
    print('{}% Timina (T)'.format(freq_T))
