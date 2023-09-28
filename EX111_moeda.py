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
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}') #\t faz uma tabulação
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{redução}% de redução: \t{aumentar(n, redução, True)}')
    print('-' * 30)


def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada =='':
            print(f'\033[0;31mERRO: {entrada} é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)