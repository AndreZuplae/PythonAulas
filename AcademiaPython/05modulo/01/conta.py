#classe conta
class Conta:
    #methodo Construtor
    def __init__(self):
        #imprimindo espaco alocado de memoria
        print(f"Imprimindo variavel refencia {self}")
        #acessando atributos construtor
        self.numero = 123
        self.titular = 'Lirinha'
        self.cpf = 1234567
        self.saldo = 120
        self.limite = 1200.0
