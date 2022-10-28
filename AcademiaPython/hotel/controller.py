import os
from datetime import datetime

#funcao de saudacao recebendo condicional para cumprimentos
def saudacao():
    #variavel criada recebendo funcao internalizada para verificacao timezone
    hora = datetime.now(tz=None)
    #condicional if recebendo variavel, se a hora for maior que 5 e menor que 13 saudacao sera bom dia
    if hora.hour >=5 and hora.hour < 13:
        print("Bom dia")

    #condicional if recebendo variavel, se a hora for maior que 13 e menor que 18 saudacao sera boa tarde
    if hora.hour >=13 and hora.hour<18:
        print("Boa tarde")

    #condicional else se o horario nao for nenhum das duas opcoes anteriores a saudacao sera boa noite
    else:
        print("Boa noite")

#azerCheckin recebendo como atributo cliente
def fazerCheckin(cliente):

    #sintax com funcao open para arquivo txt, variavel criada refenciando o arquivo
    with open('hotel/hotel.txt', 'a') as arquivo:

        #variavel que referencia arquivo recebendo funcao write que recebe como atributo para escrita o cliente
        arquivo.write(str(cliente)+"\n")

#funcao relatorio hospedes
def relatorioHospedes():

    #sintax com funcao open para arquivo txt
    with open('hotel/hotel.txt') as arquivo:  

        #print recebendo a variavel arquivo que referencia arquivo txt, sendo lida pela funcao internalizada read
        print(arquivo.read())

# funcao procurarHospedes recebendo como atributo clientefin
def procurarHospedes(clienteFind):

    #variavel criada recebendo valor inteiro 
    index=0

    #variavel criada recebendo valor inteiro 
    flag=0

    #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
    arquivo = open("hotel/hotel.txt", "r") 

    #estrutura repeticao recebendo uma variavel line para ler o arquivo(txt)
    for line in arquivo:

        #variavel index recebendo operador relacional de incremento
        index +=1

        #if condicional recebendo o clinteFind, que é o atributo principal da funcao,
        # que recebe funcao interna do python eval(), permitindo assim manipular a linha atravez da chave condicional nome, ultilindo o meu dicionario inserido como um objeto
        if clienteFind == eval(line)['nome']:

            #imprindo a minha linha de dicionario como um obejto
            print(line)

            #variavel flag recendo incremento do dicionario
            flag =1

    # condional da variavel flag atribuindo atraves de operador relacional condicao de cliente nao encontrado 
    if flag == 0:
        print("Cliente não encontrado")
        
#funcao checkout esta recebendo por atributo clientfind
def fazerCheckout(clienteFind):

    #variavel criada recebendo valor inteiro 
    index=0

    #variavel criada recebendo valor inteiro 
    flag=0

    #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
    arquivo = open("hotel/hotel.txt", "r") 

    #estrutura repeticao recebendo uma variavel line para ler o arquivo(txt)
    for line in arquivo:

        #variavel index recebendo operador relacional de incremento
        index +=1

        #if condicional recebendo o clinteFind, que é o atributo principal da funcao,
        # que recebe funcao interna do python eval(), permitindo assim manipular a linha atravez da chave condicional nome, ultilindo o meu dicionario inserido como um objeto
        if clienteFind == eval(line)['nome']:

            #Variavel chave criada recebendo incremento do indice atraves da variavel index
            chave = index

            #variavel flag recendo incremento do dicionario

            flag =1

    #variavel arquivo que representa arquivo txt recebendo funcao internalizada do python.        
    #close() fecha o arquivo aberto. Um arquivo fechado não pode mais ser lido ou escrito
    arquivo.close()

    # condional da variavel flag atribuindo atraves de operador relacional condicao de cliente nao encontrado 
    if flag == 0:
        print("Cliente não encontrado")

    #condicional else, se nenhuma das condicoes estiverem nas condicionais acima o programa irá entra nesta condiçao
    else:

        # try é para que o Python tente executar o código dentro da estrutura
        try:

            #variavel referencia do arquivo txt, recebendo funcao open e o caminho do arquivo. letra(r) tem a funcao de ler o arquivo
            with open('hotel/hotel.txt', 'r') as arquivo:

                # variavel lines criada, recebendo a variavel que representa o caminho do txt.
                # funcao readlines() Retorna todas as linhas do arquivo, como uma lista onde cada linha é um item  objeto de lista:
                lines = arquivo.readlines()
                
                #Variavel criada recebendo valor inteiro igual a 1
                posicao = 1
      
                #funcao open recebendo  o caminho do arquivo, variavel referencia  arquivo txt letra(w) tem a funcao de escrever no arquivo
                with open('hotel/hotel.txt', 'w') as arquivo:

                    #estrutura de repeticao com variavel criada lendo as linhas atraves da chave do dicionario
                    for line in lines:
                        # condicao if se a posicao for diferente da chave
                        if posicao != chave:

                            #variavel arquivo recebendo a funcao escrita, ira percorrer linha a linha identificando se o valor digitado contem na lista
                            arquivo.write(line)

                        #variavel posicao incrementando, se o valor da chave que foi digitado  o cliente é deletado
                        posicao += 1

             #Print de saida do bloco           
            print("Pessoa Deletada")

      #caso não consiga executar por conta de um erro ele vai retornar o que temos dentro do except.
        except:
            print("Erro Sistema")
    
    
    
    
