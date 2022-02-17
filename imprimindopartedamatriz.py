from random import randint
from termcolor import colored

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,50)
        print(f"{M[i][j]:2}",end=" ")
    print()

#Imprimindo a Diagonal Primária
print("Diagonal Principal")
for i in range(5):
    print(f"{M[i][i]:2}", end=" ")

print("\nDiagonal Principal")
for i in range(5):
    for j in range(5):
        if i == j:
            print(colored(f"{M[i][j]:2}","blue"), end=" ")
        else:
            print(f"{M[i][j]:2}", end=" ")
    print()

#Imprimindo a Diagonal Secundária
print("Diagonal Secundária")
for i in range(5):
    print(f"{M[i][4-i]:2}", end=" ")

print("\nDiagonal Secundária")
for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(colored(f"{M[i][j]:2}","red"), end=" ")
        else:
            print(f"{M[i][j]:2}", end=" ")
    print()

#Imprimindo os Triângulos
print("Triângulo Inferior Esquerdo em relação a DP")
for i in range(5):
    for j in range(5):
        if i > j:
            print(colored(f"{M[i][j]:2}","red"), end=" ")
        else:
            print(f"{M[i][j]:2}", end=" ")
    print()

print("Triângulo Superior Direito em relação a DP")

print("Triângulo Inferior Direito em relação a DS")

print("Triângulo Superior Esquerdo em relação a DS")