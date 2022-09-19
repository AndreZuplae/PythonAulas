# conceitos de importacao 
# from (A partir de) documento import Classe, atributo.
# importando documento, importando classe completa, ou importacao otimizada onde importa apenas um atributo.
# podendo assim ultilizar bibliotecas python, ou classe e atributos criados pelo proprio desenvolvedor


# importando biblioteca math(matematica) para realizar calculos com todas as funcoes disponibilizadas pela linguagem
import math

#variavel definida inteiro solicitando dados
num = int(input('Digite um numero: '))

#variavel recebendo anotacao da biblioteca math (biblioteca importada)
raiz = math.sqrt(num)

# print com descricao e concatenando com mascara de substituicao ultilizando metodo .format
print('A raiz de {} é igual {}'.format(num, raiz))

# importando biblioteca math(matematica) com importacao otimizada, ultilizando apenas funcao sqrt
#from math import sqrt

#variavel definida inteiro solicitando dados
#num = int(input('Digite um numero: '))

#variavel recebendo anotacao da biblioteca math (biblioteca importada) executando diretamente a funcao sqrt
#raiz = sqrt(num)

# print com descricao e concatenando com mascara de substituicao ultilizando metodo .format
#print('A raiz de {} é igual {}'.format(num, raiz))
