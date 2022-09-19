# Duas Variaveis recebendo dados do tipo flutuante
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

#Variavel realizando soma entre dois dados recebidos, e dividindo
#Aqui estamos trabalhando com ordem de procendencia aritimetica
#ordem precedencia aritimetica é um conceito matematico, onde () tem primeira prioridade
# * multiplicacao, / divisao, ** espoente, % porcentagem tem segunda prioridade
# terceira e ultima prioridade + soma, - subtracao

nota = (n1 + n2) / 2



#print ultilizando polimorfismo e quebra de linhas
print( '='*20, 'NOME SORTEADO', '='*20, '\n' )

print('sua primeira nota é {} \nsua segunda nota é {} \nResultado {}'.format(n1, n2, nota))


if nota > 7.0:
    
    print('parabens voce foi esta acima da  media!')

elif nota == 7.0:
    print("voce atingiu a media esperada")

elif nota > 5.0 < 7.0:
    print("Voce pode solicitar recuperacao!")

elif nota > 4.0 <=5.0:
    print("Procure seu professsor sua nota esta abaixo do esperado!")
    
else:
    print('infelismente voce nao conseguiu')