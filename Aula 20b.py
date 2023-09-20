def contador(*n): #O '*' informa ao python que pode ser passado vários parâmetros, sem saber sua finitude.
    for v in n:
        print(v, end=' ')
    print('fim')
    t = len(n)
    print(f'Recebi os valores {n} e são ao todo {t} números')

contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)