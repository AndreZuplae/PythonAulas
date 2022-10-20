#Repositorio com erro de logica identificar e resolver
from time import sleep

situacao = 'Reprovado'

while situacao == "Reprovado":

    nome = str(input("Digite seu nome: "))
    sobreNome = str(input("Digite seu SobreNome: "))
    idade = int(input("Digite sua idade: "))
    nota = int(input("Digite Sua nota: "))
    for lista in range(0, 2):
        
        lista_notas = [nota] 
        media = sum(lista_notas)/ len(lista_notas)
    situacao = 'Reprovado Por favor Tente novamente'


    if media >=7:
        sleep(2)
        for c in range(0,10):
            print("*")
            sleep(2)
        situacao = 'PARABENS! VOCE FOI APROVADO'


    dicionario_alunos = {'Nome':nome, 'SobreNome':sobreNome, 'Idade':idade,'Lista_Notas':lista_notas, 'Media': media, 'Situacao':situacao}

    #--- Impressão de dados do dicionário através de suas chaves

    print(f"{dicionario_alunos['Nome']} {dicionario_alunos['SobreNome']} {dicionario_alunos['Idade']} - {dicionario_alunos['Situacao']}")




    
print("Voce saiu da sua aplicacao!")