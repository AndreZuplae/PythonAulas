class Conta:
    #Atributos recebendo tipos
    titular = ''
    numero = 0
    saldo = 0
    limite = 0
    
    #methodo de acesso aos atributos da classe
    def __str__(self): #Conta
        return f' {self.titular} - {self.numero} - {self.saldo} - {self.limite}'
