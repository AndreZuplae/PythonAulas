numero = 0

#Variavel polimorfismo
poli = "*"*20

#funcao de imprecao ultilizando polimorfismo em variaveis
print(f"\n{poli} Cabecalho Repeticao {poli} \n")


for c in range(0, 3):

    valores = int(input("Digite um numero: "))

    numero += valores

print("A soma dos valores digitador é! {}".format(numero))

#funcao de imprecao ultilizando polimorfismo em variaveis
print(f"\n{poli} FIM  Repeticao {poli}\n")

#funcao de imprecao ultilizando polimorfismo em variaveis

print(f"\n{poli} Inicio Decisao {poli}\n")

#estrutura decisao
if numero > 5:
    
    print('a soma dos numeros e maior que cinco')

elif numero < 5:
    print("a soma dos numeros e menor que cinco")
    
elif numero == 5:
    print("a soma dos numeros foi cinco")

else:
    print('resultado saida!')

#funcao de imprecao ultilizando polimorfismo em variaveis

print(f"\n{poli} FIM Decisao {poli}\n")

