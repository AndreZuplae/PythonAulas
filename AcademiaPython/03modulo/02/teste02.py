#Variavel tipo predefinido recebendo dados
numero = int(input("Digite um numero: "))

#Variavel polimorfismo
poli = "*"*20

#funcao print ultilizando interpolacao de string atibuindo a variavel polimorfismo ao cabecalho
print(f"\n{poli} Cabecalho Repeticao {poli} \n")


for c in range(0, numero+1):
    print(c)
    
print(f"\n{poli} FIM  Repeticao {poli}\n")
