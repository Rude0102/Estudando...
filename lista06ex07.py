'''
Na teoria dos sistemas, define-se como elemento minimax de uma matriz o
menor elemento da linha onde se encontra o maior elemento da matriz.
Escreva um programa em Python que gere uma matriz 10 X 10 de números aleatórios
entre 1 e 99, imprima a matriz e encontre seu elemento minimax,
imprimindo-o e mostrando também sua posição.
'''
from random import randint
m = [0] * 10
for i in range(10):
    m[i] = [0] * 10
    for j in range(10):
        m[i][j] = randint(1,99)
        print(f"{m[i][j]:02}", end=" ")
    print()

maior = m[0][0]
linha = 0
col = 0
for i in range(10):
    for j in range(10):
        if m[i][j] > maior:
            maior = m[i][j]
            linha = i
            col = j
print(f"\nO maior número da matriz é {maior}. Se encontra na posição [{linha}][{col}]")

minimax = m[linha][0]
col = 0
for i in range(1,10):
    if m[linha][i] < minimax:
        minimax = m[linha][i]
        col = i
print(f"Minimax = {minimax}. Se encontra na posição [{linha}][{col}]")