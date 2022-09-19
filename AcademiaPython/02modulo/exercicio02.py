#ultilizando estrutura de condicao 

#criando duas variaveis com tipos predefinidos
n1 = float(input('Digite Primeira nota: '))
n2 = float(input('Digite Segunda nota: '))


#ultilizando conceito de procedencia aritimetica 
média = (n1 + n2) / 2

# estrutura de condicao
#if média >= 7:
  #  print('Parabens voce atingiu a media')

#else:
 #   print('Voce nao atingiu a media')

#condicao simplificada, estrutura de condicao concatenada com string
print('Parabens Voce Atingiu a media: ' if média >=7 else 'Voce nao atingiu a media: ')

print('Sua media Foi {:.1}!'.format(média))