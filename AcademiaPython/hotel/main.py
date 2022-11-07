#from time import sleep

from controller import fazerCheckin, fazerCheckout, procurarHospedes, relatorioHospedes, saudacao

def menu():

    

    # Variavel Recebendo valor inteiro para condicional de saida do menu
    menu=1

    while(menu!=0):

        #chamando funcao de saudacao
        print('-'* 30)
        saudacao() 

        #Print descritivo para usuario
        print("\nDigite o Numero da opcão Desejadas!\n")

        #Variavel menu solicitando dados com descritivo condicional, para as opcoes de menu de interacao!
        menu = int(input('''1.Fazer checkin\n2.Relatorio hospedes\n3.Procurar hospedes\n4.Fazer checkout\n0.Finalizar atendimento\n :> '''))

        #Sintax Case menu
        match menu:
            case 1:
                #Variavel pessoa recebendo dicionario vazio
                pessoa = {}

                #Variavel pessoa, sendo atribuido chave, solicitando valor para o usuario
                pessoa["nome"]=str(input("Digite seu nome:> "))
                pessoa["cpf"]=int(input("Digite seu cpf:> "))
                pessoa["idade"]=int(input("Digite sua idade:> "))
                pessoa["telefone"]=int(input("Digite seu telefone:> "))

                #chamada da funcao checkin
                fazerCheckin(pessoa)

            case 2:
                #chamada da funcao Relatorio
                relatorioHospedes()

            case 3:
                #variavel condicional para busca de hospede
                pessoa = str(input("Digite o nome desejado:"))
                #chamada da funcao procurar hospedes
                procurarHospedes(pessoa)

            case 4:
                #variavel condicional para busca de hospede
                pessoa = str(input("Digite o nome desejado:"))
                #chamada funcao checkout
                fazerCheckout(pessoa)

menu()