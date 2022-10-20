numero = int(input("Digite um numero referente a tabuada que voce deseja ver: "))

for tabuada in range(1,11):
    print("{} X {} = {}".format(numero, tabuada, numero*tabuada))