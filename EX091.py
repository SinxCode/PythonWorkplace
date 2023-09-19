from random import randint
from time import sleep
from operator import itemgetter #Serve para pegar o item de um dicionário para ordena-lo ou trata-lo de outra forma
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #número 1 pois se fosse 0, pegaria a chave, o 1 se referfe ao valor do dicionario
print('=-'*30)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)