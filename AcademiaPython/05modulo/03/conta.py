#Primeiro encapsulamento namespace (documento.py)

#segundo encapsulamento classe(OBJ)
class Conta:

    #terceiro encapsulamento methodo contrutor e atributos
    def __init__(self, titular, numero, saldo, limite):
        #Variavel objeto acessando atributos da classe
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    #Metodo extrato imprimindo valores dos atributos
    def extrato(self):
        print("O numero da conta {} do {} tem o valor de {}".format(self.numero, self.titular, self.saldo))

    #Metodo depositar recebendo variavel objeto e atributo valor interno metodo
    #E realizando condicional de incremento ao saldo
    def depositar(self, valor):
        self.saldo += valor
        
    #Metodo sacar recebendo variavel objeto e atributo valor interno metodo
    #E realizando condicional de incremento ao saldo
    def sacar(self, valor):
        self.saldo -= valor
        
    #Metodo transferir recebendo variavel objeto e atributo valor, origem, destino internos do metodo
    #recebendo condicional de sacar para o atributo origem
    #recebendo condicional de depositar para o atributo destino
    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
       
    


    