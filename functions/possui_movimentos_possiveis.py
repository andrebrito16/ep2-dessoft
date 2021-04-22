from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor
from movimentos_possiveis import lista_movimentos_possiveis

def possui_movimentos_possiveis(baralho):
    possivel = False

    for i in range(0, len(baralho)):
        if len(lista_movimentos_possiveis(baralho, i)) > 0:
            possivel = True
    
    return possivel



