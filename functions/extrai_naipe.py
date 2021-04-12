def extrai_naipe(cartas):
    if len(cartas) == 3:
        return cartas[2]
    else:
        return cartas[1]