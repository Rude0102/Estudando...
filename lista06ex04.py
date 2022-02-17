'''
4. Faça um programa em Python que gere uma matriz 10 x 10 de inteiros entre 1 e 50,
imprima a matriz e o menor elemento de cada linha.
'''
from random import randint
mat = [0] * 10
for i in range(10):
    mat[i] = [0] * 10
    for j in range(10):
        mat[i][j] = randint(1,50)

print("Matriz gerada")
print('='*30)

for i in range(10):
    menor = mat[i][0]
    for j in range(10):
        print(f"{mat[i][j]:2}", end=" ")
        if mat[i][j] < menor:
            menor = mat[i][j]
    print(f">> Menor elemento = {menor}")

print('='*30)