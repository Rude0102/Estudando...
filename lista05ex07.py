'''
7. Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e
ordene os números em ordem ascendente.
Imprima o vetor antes e após a ordenação. Pesquise sobre os métodos de ordenação.
'''
from random import randint
lista = []
for i in range(10):
    lista.append(randint(1,50))
print("Números gerados   >>",lista)
lista.sort() #ordenção em ordem crescente
print("Ordem crescente   >>",lista)
lista.sort(reverse=True) #ordenação em ordem decrescente
print("Ordem decrescente >>",lista)