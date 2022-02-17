'''
1. Leia dois vetores de inteiros x e y, cada um com 5 elementos
(não insira no vetor elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
• Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
• Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma
                       posição em y.
• Diferença entre x e y: todos os elementos de x que não existam em y.
• Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores.
• União entre x e y: todos os elementos de x, e todos os elementos de y que não
                     estão em x.
'''

x = []
i = 1
print("Informe 5 números da lista x")
while len(x) != 5:
    n = int(input(f"{i}º >> "))
    if n not in x:
        x.append(n)
        i += 1
    else:
        print("Número já inserido. Digite outro...")

y = []
i = 1
print("Informe 5 números da lista y")
while len(y) != 5:
    n = int(input(f"{i}º >> "))
    if n not in y:
        y.append(n)
        i += 1
    else:
        print("Número já inserido. Digite outro...")

print("=" * 50)
print("x >>",x)
print("y >>",y)
print("=" * 50)

soma = []
prod = []
dif = []
inter = []
uniao = x[:]

for i in range(5):
    soma.append(x[i] + y[i])
    prod.append(x[i] * y[i])
    if x[i] not in y:
        dif.append(x[i])
    else:
        inter.append(x[i])
    if y[i] not in uniao:
        uniao.append(y[i])

print("Soma              >>",soma)
print("Produto           >>",prod)
print("Diferença (x - y) >>",dif)
print("Intersecção       >>",inter)
print("União             >>",uniao)