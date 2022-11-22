from model.conta import Conta

class PessoaFisica(Conta):
    __segundo_titular = ''
    __titular = ''
    __cpf = ''
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
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial

    def __str__(self):
        return f'{super().__str__()}; {self.titular}; {self.cpf}; {self.saldo_inicial}; {self.segundo_titular}'
    