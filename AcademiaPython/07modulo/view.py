from model import Conta
from controller import create, read

abacate = Conta()
abacate.titular = 'Jean Carlos boladao'
abacate.numero = '12345'
abacate.saldo = 3000.0

create(abacate)

lista_abacates = read()

print(lista_abacates)

print("*"*30)

for c in lista_abacates:
    print(c)