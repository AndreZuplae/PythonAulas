from model.pessoaFisica import PessoaFisica

def create_psf(conta):
    contas = open('pessoafisica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def read_psf():
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')
    for conta in contas:

        conta = conta.strip()
        conta__objeto = conta.split(';')

        print(conta__objeto)

        pessoaFisica = PessoaFisica()
        
        pessoaFisica.agencia = conta__objeto[0]
        pessoaFisica.numero_agencia = conta__objeto[1]

        pessoaFisica.titular = conta__objeto[2]
        pessoaFisica.cpf = conta__objeto[3]
        pessoaFisica.saldo_inicial = conta__objeto[4]
    
        lista_contas.append(conta)
    contas.close
    return lista_contas