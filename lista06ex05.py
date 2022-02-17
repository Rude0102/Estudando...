'''
5. Faça um programa em Python que gere uma matriz
10 x 10 de inteiros entre 1 e 50, imprima a matriz
e o menor elemento de cada coluna.
'''
from random import randint

print("Matriz gerada")
print("="*30)

mat = [0] * 3
for i in range(3):
    mat[i] = [0] * 3
    for j in range(3):
        mat[i][j] = randint(1,50)
        print(f"{mat[i][j]:2}", end=" ")
    print()
print('='*30)

for i in range(3):
    menor = mat[0][i]
    for j in range(3):
        if mat[j][i] < menor:
            menor = mat[j][i]
    print(f">> Menor elemento da coluna {i} = {menor}")