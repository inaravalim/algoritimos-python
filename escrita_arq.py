#se fosse a ele continuaria escrevendo
saida = open('saida.txt', 'w')
str = 'Inara \n'
str2 = 'Valim \n'
saida.write(str)
saida.write(str2)
saida.close
saida = open('saida.txt', 'w')
str_list = ['Inara \n','Aparecida\n', 'Valim\n']
saida.writelines(str_list)
saida.close
saida = open('saida.txt', 'w')
str_list = ['Inara','Aparecida', 'Valim']
for i in str_list:
    saida.writelines(i+'\n')
saida.close