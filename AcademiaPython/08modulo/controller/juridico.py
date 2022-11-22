from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    #Variavel referencia para TXT
    contas = open('pessoajuridica.txt', 'a')
    #Variavel de Referencia de escrita
    contas.write(str(conta)+'\n')

    #variavel de referencia fechando arquivo
    contas.close

def read_pj():
    lista_contas = []
    contas = open('pessoajuridica.txt', 'r')

    for conta in contas:
        
        conta = conta.strip()
        conta__objeto = conta.split(';')

        print(conta__objeto)
        
        pessoajuridica = PessoaJuridica()

        pessoajuridica.agencia = conta__objeto[0]
        pessoajuridica.numero_agencia = conta__objeto[1]
        
        pessoajuridica.titular = conta__objeto[2]
        pessoajuridica.cnpj = conta__objeto[3]
        pessoajuridica.saldo_inicial = conta__objeto[4]

        lista_contas.append(pessoajuridica)
        
    contas.close
    return lista_contas