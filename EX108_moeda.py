def metade(n = 0):
    return n / 2


def dobro(n = 0):
    return n * 2

def aumentar(n = 0, x = 0):
    return n + (n * (x/100))


def diminuir(n = 0, x = 0):
    return n - (n * (x/100)) 


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
