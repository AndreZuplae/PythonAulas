validador = False
#--- Substituição do valor inicial
validador = True

idade = input('Digite sua idade: ')

print(" "*15, "expressão de igualdade", " "*15 ,"\n")
#--- Criação de variável booleana através de expressão de igualdade
idade = 18
validador = ( idade == 18 )
print(validador)


print(" "*15, "expressão da diferença", " "*15 ,"\n")

#--- Criação de variável booleana através de expressão da diferença
validador = ( idade != 18 )
print(validador)


print(" "*15, "expressão de maior", " "*15 ,"\n")
#--- Criação de variável booleana através de expressão de maior
validador = ( idade > 18 )
print(validador)

print(" "*15, "expressão da menor", " "*15 ,"\n")

#--- Criação de variável booleana através de expressão da menor
validador = ( idade < 18 )
print(validador)

print(" "*15, "expressão da maior e igual", " "*15 ,"\n")
#--- Criação de variável booleana através de expressão da maior e igual
validador = ( idade >= 18 )
print(validador)

print(" "*15, "expressão da menor e igual ", " "*15 ,"\n")
#--- Criação de variável booleana através de expressão da menor e igual
validador = ( idade <= 18 )
print(validador)