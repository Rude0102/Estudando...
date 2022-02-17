#Pedro Gottlob, Lucas Figueredo, Leonardo Vitor Da Silva
num= int(input("digite um número:" ))
tot=0
for i in range(1,num + 1):
    if num %  i == 0:
        print("\033[34m", end="" )
        tot += 1
    else:
        print("\033[m")
    print("{} " .format(i), end=" ")
print(" O numero{} foi divisivel {} vezes".format(num, tot))
if tot == 2:
    print("ele não é primo")
else:
    print("ele  é primo")
