from datetime import date

# Caso possua Carteira de Trabalho entra na funcao de validacao
def validacao(dados):
    #condicional if recebendo a variavel de atributo da funcao 
    # se a pessoa possuir carteira de trabalho e numero digitado for diferente de 0 entra nas seguintes condicionais
     if dados['ctps'] > 0:
        dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
        dados['salário'] = float(input('SALÁRIO: R$'))
        dados['aposentadoria'] = dados['contratação'] - (date.today().year - dados['idade']) + 35

# Mostrando os dados pessoais na tela
def impressao(dados):
    
    print('-' * 25 + f'\n{"DADOS PESSOAIS":^25}\n' + '-' * 25)
    
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')