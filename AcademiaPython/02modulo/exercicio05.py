#importado classe random
from random import choice

#criando variaveis tipos predefinidos, solicitando dados
n1 = str(input('digite um nome: '))
n2 = str(input('digite um nome: '))
n3 = str(input('digite um nome: '))
n4 = str(input('digite um nome: '))

#Variavel recebendo uma lista definida pela simbologia [],
lista = [n1, n2, n3, n4]

#variavel recebendo metodo choice que foi importado
sorteado = choice(lista)


#print ultilizando polimorfismo e quebra de linhas
print( '='*20, 'NOME SORTEADO', '='*20, '\n' )

#print utilizando interpolacao
print(f"O nome sorteado foi {sorteado}")

#estrutura decisao
if sorteado == n1:
    
    print('o nome sorteado foi o primeiro digitado')

elif sorteado == n2:
    print("o nome sorteado foi o segundo a ser sorteado!")
    
elif sorteado == n3:
    print("o nome sorteado foi o terceiro")

else:
    print('o nome sorteado foi o quarto')