n = []
for i in range(2):
    n.append([])
    for j in range(3):
        n[i].append(int(input(f"[{i}][{j}]:")))
soma=i+j

#PROFESSORA
matriz=[]
for i in range(2):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f"{i}{j}:")))
        soma+= matriz [i][j]
    print("matriz informada")
    for i in range(2):
        for j in range(3):
            print(f"{matriz[i][j]:2}", end=" ")