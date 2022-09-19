#Tipos primitivos 

#Variavel texto
nome = 'Andre'

# Variavel Numerica do tipo inteira
idade = 18

#Variaveis booleanas
verdadeiro = True
falso = False

#variavel numerica tipoflutuante, (numero ponto)
salario = 1.200

#=======================================Imprimindo dados numericos===========================================


#n1 = input('Digite seu salario Janeiro: ')
#n2 = input('Digite seu salario Fevereiro: ')

n1 = float(input('Digite seu salario Janeiro: '))
n2 = float(input('Digite seu salario Fevereiro: '))

#n1 = int(input('Digite sua idade: '))
#n2 = int(input('Digite sua idade denovo: '))
soma = n1 + n2

# print ultilizando mensagem string mais concatenacao da variavel soma
#print("A soma Vale: ", soma)
# Print ultilizando format exibindo os valores digitados em cada variavel concatenando com mensagem string
print("A Soma entre {} e {} vale {}".format(n1, n2, soma))

#--- Impressão de multiplos textos e variávis usando virgula
#print('Idade:',idade, 'Salario:',salario, 'Nome:', nome, 'Verdadeiro:', verdadeiro, 'Falso:', falso)
#--- Impressão de multiplos textos e variávies usando a função format
#print('Idade:{} Salario:{} Nome:{} Verdadeiro:{} Falso:{}'.format(idade, salario, nome, verdadeiro, falso) )
#--- Impressão de multiplos textos e variávies usando interpolação de strings
#print(f'Idade:{idade} Salario:{salario} Nome:{nome} Verdadeiro:{verdadeiro} Falso:{falso}')