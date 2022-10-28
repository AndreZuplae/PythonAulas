"""
Desafio 05
Problema: Faça um programa que tenha uma função chamada contador(),
          que receba três parâmetros: inicio, fim e passo e realize a contagem.
          Seu programa tem que realizar três contagens atráves da função criada:
            A) De 1 até 10, de 1 em 1
            B) De 10 até 0, de 2 em 2
            C) Uma contagem personalizada
Resolução do problema:
"""
from controllerContador import contador


def menu():
    print('-' * 35, "Cabecalho Menu", '-' * 35)

    contador(1, 10, 1)
    contador(10, 0, -1)

    print('-' * 35 + f'\n{"PERSONALIZE SUA CONTAGEM"}\n' + '-' * 35)
    
    contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))

menu()