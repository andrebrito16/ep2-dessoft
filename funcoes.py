from random import shuffle

def cria_baralho():
    lista =  ['10♠', '10♥', '10♦', '10♣','9♠', '9♥', '9♦', '9♣', '8♠', '8♥', '8♦','8♣', '7♠', '7♥', '7♦', '7♣', '6♠', '6♥','6♦', '6♣', '5♠', '5♥', '5♦', '5♣', '4♠','4♥', '4♦', '4♣', '3♠', '3♥', '3♦', '3♣','2♠', '2♥', '2♦', '2♣', 'A♠', 'A♥', 'A♦','A♣', 'K♠', 'K♥', 'K♦', 'K♣', 'J♠', 'J♥','J♦', 'J♣', 'Q♠', 'Q♥', 'Q♦', 'Q♣']
    shuffle(lista)
    return lista

def empilha(baralho, origem, destino):

    baralho[destino] = baralho[origem]

    del baralho[origem]
    
    return baralho



def extrai_naipe(carta):
    return str(carta)[::-1][0]


def extrai_valor(cartas):
    return str(cartas)[:-1]


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

def possui_movimentos_possiveis(baralho):
    possivel = False

    for i in range(0, len(baralho)):
        if len(lista_movimentos_possiveis(baralho, i)) > 0:
            possivel = True
    
    return possivel

def adiciona_cor(carta):
    if extrai_naipe(carta) == '♦' or extrai_naipe(carta) == '♥':
        return f"\033[31m {carta}"
    else:
        return f"\033[30m {carta}"



