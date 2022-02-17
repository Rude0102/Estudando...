#Criando a matriz pedindo valores

mat = [0] * 3
for i in range(3):
    print(f"Linha {i}")
    mat[i] = [0] * 4
    for j in range(4):
        mat[i][j] = int(input(f"[{i}][{j}] >>"))

print("Matriz informada")

#Formas de impressão da matria
#1ª forma
print(mat)
print("*" * 50)

#2ª forma
for i in range(3):
    print(mat[i])
print("*" * 50)

#3ª forma
for i in range(3):
    for j in range(4):
        print(f"{mat[i][j]:2}", end=" ")
    print()