#Variavel tipo predefinido recebendo dados
inicio = int(input("Digite um numero: "))
fim = int(input("Digite um numero: "))
passo = int(input("Digite um numero: "))


#Variavel polimorfismo
poli = "*"*20

#funcao print ultilizando interpolacao de string atibuindo a variavel polimorfismo ao cabecalho
print(f"\n{poli} Cabecalho Repeticao {poli} \n")


for c in range(inicio, fim+1, passo):
    print(c)

print(f"\n{poli} FIM  Repeticao {poli}\n")