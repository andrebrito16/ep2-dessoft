def adiciona_cor(carta):
    if extrai_naipe(carta) == '♦' or extrai_naipe(carta) == '♥':
        return f"\033[31m {carta}"
    else:
        return f"\033[30m {carta}"