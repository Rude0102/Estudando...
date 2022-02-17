from random import randint
n=[]
for i in range(10):
    n.append([])
    for j in range(10):
        n[i].append (randint(1,50))
        soma += n[i][j]
print("matriz gerada")
for i in range(10):
    for j in range(10):
        print(f"{m[i][j]:2}", end="")