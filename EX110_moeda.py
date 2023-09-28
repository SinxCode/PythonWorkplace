def metade(n = 0, formato = False):
    r = n / 2
    return r if not formato else moeda(r)


def dobro(n = 0, formato= False):
    r = n * 2
    return r if formato is False else moeda(r)

def aumentar(n = 0, x = 0, formato=False):
    r = n + (n * (x/100))
    return r if formato is False else moeda(r)


def diminuir(n = 0, x = 0, formato = False):
    r = n - (n * (x/100)) 
    return  r if formato is False else moeda(r)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(n = 0, aumento =10, redução = 5):
    print('=-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('=-' * 30)
    print(f'Preço analisado: {moeda(n)}')
