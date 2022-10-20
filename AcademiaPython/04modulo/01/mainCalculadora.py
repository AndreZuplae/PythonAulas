from modulo1.calc2 import soma, div, sub, mul 

#*************************funcao******************************************
def menu():

    print('*'*25, 'Menu', '*'*25)
    
    cond = "sim"
    while cond == "sim":
        n1 = int(input("Digite primeiro numero: "))
        n2 = int(input("Digite segundo numero: "))

        Soma = soma(n1, n2)
        Subtracao = sub(n1, n2)
        divizao = div(n1, n2)
        Multiplicacao = mul(n1, n2)
                
        print('A soma entre os numeros é: {}\nA subtracao é: {}\nA divisao é: {}\nA multipilcacao é: {}'.format(Soma, Subtracao, divizao, Multiplicacao))

        cond = str(input("Deseja continuar \n sim\n nao \n :> "))
#*************************funcao******************************************



#*************************chamada******************************************
menu()
print("Voce saiu da sua aplicacao!")
#*************************chamada******************************************
