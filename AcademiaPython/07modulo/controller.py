from model import Conta

def create(conta):
    #Variavel referencia para TXT
    contas = open('contas.txt', 'a')
    #Variavel de Referencia de escrita
    contas.write(str(conta)+'\n')

    #variavel de referencia fechando arquivo
    contas.close

def read():
    #Lista Vazia
    lista_contas = []
    #Variavel referencia arquivo txt
    contas = open('contas.txt', 'r')
    #for com variavel percorrendo arquivo txt
    for conta in contas:
        #variavel conta recebendo funcao internalizada para retirada espacos
        conta = conta.strip()
        #Variavel recebendo funcao internalizada de condicao para o indice
        conta__objeto = conta.split(';')

        print(conta__objeto)
        #Variavel referencia obejeto
        conta = Conta()
        #Setter recebendo um indice
        conta.titular = conta__objeto[0]
        #Setter recebendo um indice
        conta.numero = conta__objeto[1]
        #Setter recebendo um indice
        conta.saldo = conta__objeto[2]
        #escrevendo variavel lista e atribuindo nosso Objeto
        lista_contas.append(conta)
    contas.close
    return lista_contas

def update(conta_update:Conta):
        lista_contas = [] 
        contas = open('contas.txt', 'r')
        for conta in contas:
            conta_limpa = conta.strip()
            conta_objeto = conta_limpa.split(';')     

            if conta_update.numero == int(conta_objeto[1]):
                lista_contas.append(str(conta_update)+'\n')           
            else:
                lista_contas.append(conta)
        contas.close()

        contas = open('contas.txt','w')
        contas.writelines(lista_contas)
        contas.close()


def delete(numero_conta):
        lista_contas = [] 
        contas = open('contas.txt', 'r')
        for conta in contas:
            conta_limpa = conta.strip()
            conta_objeto = conta_limpa.split(';')
            if numero_conta != int(conta_objeto[1]):
                lista_contas.append(conta)
                
        contas.close()
        contas = open('contas.txt','w')
        contas.writelines(lista_contas)
        contas.close()