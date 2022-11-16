from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__('1030', 'Pessoa Fisica')
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial
        print('Passando Pelo Construtor da classe pessoa fisica')

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'{super().__str__()} {self.titular} {self.cpf} {self.saldo_inicial} {self.segundo_titular}'
    