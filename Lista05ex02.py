from random import randint
numeros = []
cpar = 0
soma = 0
for i in range(20):
    numeros.append(randint(1, 50))
    if numeros[i] % 2 == 0:
         cpar += 1
print(f"números gerados {numeros}")
print(f"o numeros pares são: {cpar}")

#///////////////////////////////////

'''
2. Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50),
armazene-os em uma lista. Imprima os números e calcule a média apenas dos
números pares.
'''
from random import randint
L = []
somaPar = cPar = 0
for i in range(20):
    L.append(randint(1,50))
    if L[i] % 2 == 0:
        somaPar += L[i]
        cPar += 1
print("Números >>",L)
print(f"Média dos números pares = {somaPar/cPar:.2f}")