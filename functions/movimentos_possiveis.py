from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor

def lista_movimentos_possiveis(baralho, posicao):
    if posicao == 0:
        return []


    movimentos_possiveis = list()

    valor = extrai_valor(baralho[posicao])
    naipe = extrai_naipe(baralho[posicao])

    if posicao < 3:
        if valor == extrai_valor(baralho[posicao-1]) or naipe == extrai_naipe(baralho[posicao-1]):
            movimentos_possiveis.append(1)
        return movimentos_possiveis


    if valor == extrai_valor(baralho[posicao-1]) or naipe == extrai_naipe(baralho[posicao-1]):
        movimentos_possiveis.append(1)
    if valor == extrai_valor(baralho[posicao-3]) or naipe == extrai_naipe(baralho[posicao-3]):
        movimentos_possiveis.append(3)
    
    return movimentos_possiveis