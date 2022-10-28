from modulo1.calc2 import somaSalario #importar apenas o necessario

#*************************funcao******************************************
def menuSalario():
    print('*'*25, 'Menu', '*'*25)
    
    cond = "sim"
    while cond == "sim":
        n1 = float(input("Digite primeiro salario: "))
        n2 = float(input("Digite segundo salario: "))
        n3 = float(input("Digite terceiro salario: "))
        n4 = float(input("Digite quarto salario: "))

        resultado = somaSalario(n1, n2, n3, n4)

        print(f'a soma entre os salarios é {resultado}')

        cond = str(input("Deseja continuar \n sim\n nao \n :> "))
#*************************funcao******************************************


            
menuSalario()

print("Voce saiu da sua aplicacao!")