#Pedro Henrique Gottlob Bech,Lucas Figueiredo,Leonardo

l=[]
while l !=6:
    n = int(input('Digite um valor'))
    if n<1 or n>60:
        print('valor invalido')
    else:
        if n not in l:
            l.append(n)
        else:
            print('valor já inserido')
#professora eu só consegui chegar até aqui