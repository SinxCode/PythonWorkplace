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
