from model import Conta
from controller import create, read, update, delete

abacate = Conta()
abacate.titular = 'Dieter'
abacate.numero = 123456
abacate.saldo = 10000.0

#create(abacate)

#lista_abacates = read()

#print(lista_abacates)

#print("*"*30)

#for c in lista_abacates:
    #print(c)
update(abacate)
#delete(1234567)