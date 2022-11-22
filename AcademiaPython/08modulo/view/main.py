from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf
 
 
def menu():
 
   #menu
   menu=1
   while(menu!=0):
    
       print('-'* 30)
       
       print("\nDigite o Numero da Opcao desejada!\n")
 
       #Variavel menu solicitando dados com descritivo condicional, para as opcoes de menu de interacao!
       menu_inicial = int(input(" Cadastrar Conta \n 1.Pessoa Fisica \n 2.Pessoa Juridica\n escolha a opcao desejada:>  "))
 
       #Sintax Case menu
       match menu_inicial:
          
           case 1:
 
               menu = int(input(" MENU DE CADASTRO CONTA PESSOA FISICA \n 1.Cadastrar Conta\n 2.Lista Cadastro\n 3. \n 4. \n 0.Finalizar atendimento\n :> "))
               match menu:
 
                   case 1:
                       print("*"*30, "MENU CADASTRO DE PESSOA FISICA", "*"*30)
 
                       pessoaFisica = PessoaFisica()
                       pessoaFisica.titular = input("Digite o Titular:> ")
                       pessoaFisica.cpf = input("Digite o CPF:> ")
                       pessoaFisica.saldo_inicial = float(input('Deposite o Saldo Inicial:> '))
 
                       cond = "sim"
                       cond = (input("Deseja cadastrar Segundo titular \n sim\n nao \n :> "))
                       if cond == "sim":
                           pessoaFisica.segundo_titular = input("Digite o nome do segunto titular:> ")
                      
                       create_psf(pessoaFisica)
 
                   case 2:
                       print("*"*30, "MENU CADASTRO DE PESSOA FISICA", "*"*30)
                       read_psf()
                      
           case 2:
 
               menu = int(input(" MENU DE CADASTRO CONTA PESSOA JURIDICA  \n 1.Cadastrar Conta\n 2.Lista Cadastro\n 3.\n 4. \n 0.Finalizar atendimento\n :> "))
               match menu:
                   case 1:
                       # Variavel pessoa recebendo dcionario vazio
                       print("*"*30, "CADASTRO DE PESSOA JURIDICA", "*"*30)
 
                       pessoaJuridica = PessoaJuridica()
                       pessoaJuridica.titular = input("Digite o Titular:> ")
                       pessoaJuridica.cnpj = input("Digite o CNPJ:> ")
                       pessoaJuridica.saldo_inicial = float(input('Deposite o Saldo Inicial:> '))
                      
                       cond = "sim"
                       if cond == "sim":
                           pessoaJuridica.segundo_titular = input("Digite o nome do segunto titular:> ")
 
                       print(pessoaJuridica)
                       create_pj(pessoaJuridica)
 
                   case 2:
                      read_pj()