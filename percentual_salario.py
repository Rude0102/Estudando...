salario=float(input("insira o seu salario: "))
despesas= float(input("insira as despesas: "))
comprometido= despesas/salario*100
resultado=print(f' o valor comprometido é de {comprometido//2}%')

if resultado >= 50:
    print("Você está com uma boa média")
else:
    print(" Você está com uma péssima média")