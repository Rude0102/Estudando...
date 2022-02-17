'''
5. Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
'''
num = 1
somaNum = qtNum = somaPar = qtPar = 0
maior = 0
menor = 9999999
while num != 0:
    num = int(input("Digite um número ou 0 para encerrar >> "))
    if num != 0:
        somaNum += num
        qtNum += 1
        if num % 2 == 0:
            somaPar += num
            qtPar += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
if qtNum==0:
                print("não foi inserido nenhum valor")
print("="*50)
print(f"(a) A soma dos números digitados >> {somaNum}")
print(f"(b) A quantidade de números digitados >> {qtNum}")
print(f"(c) A média dos números digitados >> {somaNum/qtNum:.2f}")
print(f"(d) O maior número digitado >> {maior}")
print(f"(e) O menor número digitado >> {menor}")
print(f"(f) A média dos números pares >> {somaPar/qtPar:.2f}")