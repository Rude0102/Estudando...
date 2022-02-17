'''
1. Faça um programa em Python que gere 10 números aleatórios (entre 1 e 50),
imprima os números e calcule quantos são números pares e quantos são números ímpares.
'''
from random import randint
numeros = []
cPar = cImpar = 0
for i in range(10):
    numeros.append(randint(1,50))
    if numeros[i] % 2 == 0:
        cPar += 1
    else:
        cImpar += 1
print("Números gerados >>",numeros)
print(f"Quantidade de números pares   >> {cPar}")
print(f"Quantidade de números ímpares >> {cImpar}")