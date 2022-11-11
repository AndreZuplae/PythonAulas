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

print("*"*30, "Extrato Inicial da conta", "*"*30)
conta.extrato()

print("*"*30,)
print(conta.depositar(float(input("Digite o valor do deposito:> "))))

print("*"*30, "Extrato Deposito", "*"*30)
conta.extrato()

print("*"*30,"\n")

print(conta.sacar(float(input("Digite o valor do Saque:> "))))
print("*"*30, "Extrato Saque", "*"*30)
conta.extrato()



print("*"*30, "Inicio Menu", "*"*30)
                #atributo titular
conta2 = Conta(input("Digite seu Nome:> "), 
#atributo Numero Conta
int(input("Digite o numero da sua conta:> ")),
#atributo Saldo Conta
float(input("Digite seu Saldo Inicial:> ")),
#atributo limite Conta
float(input("Digite o limite da sua Conta:> ")))

print("*"*30, "Extrato Inicial da conta", "*"*30)
conta2.extrato()

conta2.transferir(float(input("Digite O valor da transferencia:> ")), conta, conta2)
print("*"*30, "Extrato Transferencia", "*"*30)
conta2.extrato()

conta.extrato()



 