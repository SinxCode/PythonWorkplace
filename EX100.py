from random import randint
from time import sleep


def sorteio(lista):
    print('SORTEANDO 5 VALORES DA LISTA: ', end='')
    for c in range (1,6):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(0.5)
    print('Pronto!')



def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores Pares de {lista}, temos {soma}')
        


numeros = list()
sorteio(numeros)
somapar(numeros)