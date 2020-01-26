# -*- coding: utf-8 -*-
#trabalhando com manipulacao de arquivos
#arquivo = open("ola_mundo.txt")
#linhas = arquivo.readlines()
#print(linhas)

#criando novo arquivo
w = open("ola_mundo_2.txt", "a")
#escrevendo no arquivo criado
w.write("Este é o meu arquivo\n")
#fechando o arquivo
w.close