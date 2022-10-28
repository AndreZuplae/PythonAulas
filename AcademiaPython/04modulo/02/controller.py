
#*************************funcao******************************************
def salvar(nome):
    with open('modulo2/pessoa.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')
#*************************funcao******************************************

#*************************funcao******************************************
def listar():
    nomes = []
    with open('modulo2/pessoa.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)    

    return nomes
#*************************funcao******************************************



