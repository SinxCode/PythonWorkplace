def contador(*n): #O '*' informa ao python que pode ser passado vários parâmetros, sem saber sua finitude.
    for v in n:
        print(v, end=' ')
    print('fim')
    t = len(n)
    print(f'Recebi os valores {n} e são ao todo {t} números')

contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)


def soma(*valores):
    s = 0
    for n in valores:
        s = s + n
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4) #Pela função 'soma' estar recebendo '*' valores é possível colocar vários valores dentro do parametro