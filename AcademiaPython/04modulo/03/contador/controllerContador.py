from time import sleep

#Funcao de contador recebendo atributos por padrao
def contador(inicio, fim, passo):

    print('-' * 35)
    #abs()função retorna o valor absoluto do número fornecido.
    passo = abs(passo) if passo != 0 else 1 
    #print descritivo recebendo os passos defindos 
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    #funcao interna sleep
    sleep(0.5)

    #estrutura condicional se o inicio for menor que o final a condicao sera incremental
    if inicio < fim:
        print("Contador Incremental")
        #Contador Incremental
        #for recebendo variavel defindindo as sequencias dos passos executado
        for cont in range(inicio, fim + 1, passo):
            #Print recebendo variavel cont do for, e end para impresao dos passos lado a lado
            print(cont, end=' ')
            sleep(0.3)

    #estrutura condicional se o inicio for maior que o final a condicao sera decremental
    elif inicio > fim:
        print("Contador decremental")
        #Contador Decremental 
        #variavel definida recebendo condicao de contagem de decremento
        for cont in range(inicio, fim - 1, -passo):
            #Print recebendo variavel cont do for, e end para impresao dos passos lado a lado
            print(cont, end=' ')
            sleep(0.3)
    #Print De Saida Do bloco
    print('Final...')