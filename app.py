
# Importações das funções
from funcoes import *


print('''
Paciência Acordeão 
================== 

Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

Existem apenas dois movimentos possíveis: 

1. Empilhar uma carta sobre a carta imediatamente anterior; 
2. Empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

1. As duas cartas possuem o mesmo valor ou 
2. As duas cartas possuem o mesmo naipe. 

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

''')
# input("Aperte [Enter] para iniciar o jogo...")


baralho = cria_baralho()

while True:
    if len(baralho) == 0:
        print("Você GANHOU! ")
        break
    indice = 1
    for carta in baralho:
        print(f"{indice}. {carta}")
        indice += 1
    
    if possui_movimentos_possiveis(baralho):
        movimento = int(input("Escolha uma carta para movimentar: "))
        possibilidades = lista_movimentos_possiveis(baralho, movimento-1)
        if len(possibilidades) == 0:
            print("Essa carta não pode ser movida, tente novamente!")
        else:
            if len(possibilidades) > 1:
                print(f"Essas são as opções para movimento da carta {baralho[movimento-1]}")
                indice_possibilidades = 1
                for p in possibilidades:
                    print(f"{indice_possibilidades}. {baralho[movimento-1-p]}")
                    indice_possibilidades += 1
                while True:
                    escolha_movimento = int(input("Escolha uma opção: ").strip())
                    if escolha_movimento > len(possibilidades) and escolha_movimento < 1:
                        print("Escolha inválida, tente novamente!")
                        indice_possibilidades = 1
                        for p in possibilidades:
                            print(f"{indice_possibilidades}. {baralho[movimento-p]}")
                            indice_possibilidades += 1
                    else:
                        print(f"Empilhar a carta {baralho[movimento-1]} sobre a carta {baralho[movimento-1-possibilidades[escolha_movimento-1]]}")
                        baralho[movimento-1-possibilidades[escolha_movimento-1]] = baralho[movimento-1] 
                        del baralho[movimento-1]
                        break
            elif len(possibilidades) == 0:
                print("Nenhum movimento possível, tente novamente!")
            else:
                # Remove a carta realizando o único movimento possível!

                baralho[movimento-1-possibilidades[0]] = baralho[movimento-1] 
                del baralho[movimento-1]
    else:
        print("Você perdeu!")
                
                
        
            
            

            
                   
           
            
            
    
        