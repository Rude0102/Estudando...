'''
minha solução
'''


trabalho_terca= input("Digite True or False se você fez o trabalho de terça: ")
trabalho_quinta= input("Digite True or False se você fez o trabalho de Quinta: ")

tv50= trabalho_terca and trabalho_quinta
if tv50 == True and True:
    print("Ganhou Tv 50")
    
tv32= trabalho_terca or trabalho_quinta
if tv32 == True or False:
    print("Ganhou TV32")

sorvete= True!= False    
if sorvete== True != False:
    print ("Ganhou um sorvete")

else:
    print("vc tem saúde")