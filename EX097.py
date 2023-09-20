def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam )


txt = input('Escreva algo: ')
escreva(txt)