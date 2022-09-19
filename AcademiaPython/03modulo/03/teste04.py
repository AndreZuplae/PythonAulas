# Dicionários

#--- Criação de uma variável tipo dicionário 
#dicionario = { 'Nome':'Andre', 'Sobrenome':'Belli' }
#--- Impressão de um dicionário completo
#print(dicionario)
#--- Impressão de um dos dados do dicionário através da chave
#print(dicionario ['Sobrenome'])

n1 = input('Digite seu nome: ')
n2 = input('Digite seu nome: ')
n3 = input('Digite seu nome: ')

print("\n", ' '*20, 'CABECALHO', ' '*20, '\n')

lista = [n1, n2, n3]

for i in range(0,3):
     print(lista[i])