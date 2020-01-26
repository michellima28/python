# -*- coding: utf-8 -*-
#declaração de lista (entre conchetes)
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

print(minha_lista)
print(minha_lista_2)
print(minha_lista_3)
print(minha_lista[2])
print(minha_lista_2[2:])

for x in minha_lista:
	print(x)

tamanho1 = len(minha_lista)
tamanho2 = len(minha_lista_2)
tamanho3 = len(minha_lista_3)	

print(tamanho1)
print(tamanho2)
print(tamanho3)

#adicionando elementos à lista
minha_lista.append("limão")
minha_lista.append("uva")
minha_lista.append("maçã")
print(minha_lista)

#verificando existência de elementos na lista
if 3 in minha_lista_2:
	print("3 está na lista")

#removendo itens da lista
del minha_lista[:2]
print(minha_lista)	








