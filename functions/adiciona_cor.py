def adiciona_cor(carta):
    if extrai_naipe(carta) == '♦':  
        return f"\033[31m {carta}"
    elif extrai_naipe(carta) == '♥':
        return f"\033[33m {carta}"
    elif extrai_naipe(carta) == '♠':
        return f"\033[34m {carta}"
    else:
        return f"\033[35m {carta}"
    