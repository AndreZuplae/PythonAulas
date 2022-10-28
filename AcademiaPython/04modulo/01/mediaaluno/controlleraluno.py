def resultado(n1, n2, n3, n4):

    media = (n1 + n2+ n3+ n4) / 4

    if media >= 7:
        media = 'Aprovado'

    elif media >= 5:
        media = 'Recuperação'

    else:
        media = 'Reprovado'
    return media