'''
3. Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
aleatórios entre 1 e 50, imprima a matriz e a soma de todos os elementos
de cada linha.
'''
from random import randint
M = [0] * 10
for i in range(10):
    M[i] = [0] * 10
    for j in range(10):
        M[i][j] = randint(1,50)

print("Matriz gerada")
print('='*30)

for i in range(10):
    soma = 0
    for j in range(10):
        print(f"{M[i][j]:2}", end=" ")
