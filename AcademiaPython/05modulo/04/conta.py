#Primeiro encapsulamento namespace (documento.py)
#segundo encapsulamento classe(OBJ)
class Conta:
    #terceiro encapsulamento methodo contrutor e atributos
    def __init__(self, titular, numero, saldo, limite):
        #Variavel objeto acessando atributos da classe
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    def set_titular(self, titular):
        self.__titular = titular
    def get_titular(self):
        return self.__titular

    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero    

    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite

    def __str__(self):
        return f'Titular: {self.get_titular()}\nNumero da Conta: {self.get_numero()}\nSaldo da conta: {self.get_saldo()}\nLimite da conta: {self.get_limite()}'