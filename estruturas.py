resp='S'
i=0
while resp.upper()=='S':
    n= int(input("Entre o valor da tabuada: "))
    while i <=10:
        print(f'{n}x{i} = {n*i}')
        i=+1
        resp=input("deseja continuar [S/N]? ")
        print(f'{n}x{i} = {n*i}')