class Conta:

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print('Passando pelo construtor da classe mae')

    def __str__(self):
        return f'{self.numero} {self.tipo}'