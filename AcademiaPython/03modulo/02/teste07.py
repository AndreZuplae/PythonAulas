soma = 0
cont = 0

#Variavel polimorfismo
poli = "*"*20

#funcao de imprecao ultilizando polimorfismo em variaveis
print(f"\n{poli} Cabecalho Repeticao {poli} \n")


for c in range(1, 501):
    if c % 3 == 0:
        soma += c
        cont += 1
    

print("A soma dos valores {} os valores solicitados sao {} ".format(cont, soma))