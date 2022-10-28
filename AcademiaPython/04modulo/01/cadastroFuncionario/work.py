from controllerfuncionario import validacao, impressao
from datetime import date


def menu():
    #dict()função cria um dicionário.
    #Um dicionário é uma coleção não ordenada, que contem chave e valor
    camarao = dict()

    camarao['nome'] = input('NOME: ').strip().capitalize()
    #datetime módulo retorna um objeto de data que contém o valor da data de hoje
    camarao['idade'] = date.today().year - int(input('DATA NASCIMENTO: '))
    
    camarao['ctps'] = int(input('Nº CARTEIRA DE TRABALHO (0 se não tem): '))

    validacao(camarao)
    impressao(camarao)

    








menu()