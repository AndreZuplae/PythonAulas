from model.conta import Conta

class PessoaJuridica(Conta):
    __segundo_titular = ''
    __titular = ''
    __cnpj = ''
    __saldo_inicial = 0

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial

    def __str__(self):
        return f'{super().__str__()}; {self.titular}; {self.cnpj}; {self.saldo_inicial}; {self.segundo_titular}'