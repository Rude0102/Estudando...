from random import randint
lista=[]
for i in range(10):
    lista.append(randint(1,50))
print("ordem,direita>> ",lista)
print("ordem, inversa",lista[::-1])

