from controller import salvar, listar

#*************************funcao******************************************
def menu():

    print('*'*25, 'Menu', '*'*25)

    cond = "sim"
    while cond == "sim":

        salvar(input("Digite seu nome "))

        cond = str(input("Deseja continuar \n sim\n nao \n :> "))
#*************************funcao******************************************

       
menu()
print('Lista Nomes: \n', listar())  