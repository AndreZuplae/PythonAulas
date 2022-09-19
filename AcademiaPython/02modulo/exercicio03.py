choop = float(input('Quantos choop voce tomou Hoje? '))

if choop > 5:
    print('Voce ja esta  Faceiro!')
    multa = choop * 100
    print('Voce ira pagar uma multa de R$ {:.2f}  se te pegarem dirigindo bebado: '.format(multa))
else:
    print('Tome Choop Pra ficar faceiro')