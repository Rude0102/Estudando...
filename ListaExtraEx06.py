num = int(input("digite um numero:"))
x= num
inv = 0
while x != 0:
   inv *=10
   inv += x % 10
   x//=10
print(inv)


#daqui para baixo é só curiosidade (vc vai aprender mais para frente)
num= 3498
x = str(num)
inv= x [::-1]
print (num,inv)


achou= False
for i in range(100,1000):
    for j in range (999,99,-1):
        num=str(i*j)
        inv=num [::-1]
        if num == inv:
           print(num)
           achou= True
            break
    if achou:
        break