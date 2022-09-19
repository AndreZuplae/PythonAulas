
import random 

#criando variaveis tipos predefinidos, solicitando dados
n1 = str(input('digite um nome: '))
n2 = str(input('digite um nome: '))
n3 = str(input('digite um nome: '))
n4 = str(input('digite um nome: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(" "*20, "CABECALHO", " "*20, "\n")

print(lista)