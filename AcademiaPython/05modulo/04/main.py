from conta import Conta

print("*"*30, "Inicio Menu", "*"*30)

                #atributo titular
conta = Conta(input("Digite seu Nome:> "), 
#atributo Numero Conta
int(input("Digite o numero da sua conta:> ")),
#atributo Saldo Conta
float(input("Digite seu Saldo Inicial:> ")),
#atributo limite Conta
float(input("Digite o limite da sua Conta:> ")))



print('*'*30, "Menu Conta", '*'*30)
print("O Nome Do Titular é {} o numero da conta é {} o saldo e {}".format(conta.get_titular(), conta.get_numero(), conta.get_saldo()))