from random import randint
numeros = []
multiplo = []
for i in range(20):
    numeros.append(randint(1,50))
    if numeros[i] % 5 == 0:
        multiplo.append(numeros[i])
print(f"Números gerados {numeros}")
print(f"Números múltiplos de 5 {multiplo}")