def possui_movimentos_possiveis(baralho):
    from lista_movimentos_possiveis import lista_movimentos_possiveis
    possivel = False

    for i in range(0, len(baralho)):
        if len(lista_movimentos_possiveis(baralho, i)) > 0:
            possivel = True
    
    return possivel



