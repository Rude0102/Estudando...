from random import randint
lista=[]
for i in range(10):
    lista.append(randint(1,50))
print("numeros gerados:",lista)
numero= int(input("informe um número para a busca:"))

achou=False
for i in range(10):
    if lista[i] == numero:
        print(f"{numero} pertence a lista")
        achou=True
        break
if not achou:
    print(f"{numero} não pertence a lista")