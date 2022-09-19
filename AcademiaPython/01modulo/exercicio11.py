#Inicio manipulacao de lista, ultilizando conceito de import

#importado classe random
import random

#criando variaveis tipos predefinidos, solicitando dados
n1 = str(input('digite um nome: '))
n2 = str(input('digite um nome: '))
n3 = str(input('digite um nome: '))
n4 = str(input('digite um nome: '))

#Variavel recebendo uma lista definida pela simbologia [],
lista = [n1, n2, n3, n4]

#variavel recebendo metodo random que foi importado
sorteado = random.choice(lista)
#  random.shuffle(lista), #exibe no terminal ordenacao de lista

#print ultilizando polimorfismo e quebra de linhas
print( '='*20, 'NOME SORTEADO', '='*20, '\n' )

# print recebendo uma (variavel objeto) com o metodo choice da classe random
print(sorteado)