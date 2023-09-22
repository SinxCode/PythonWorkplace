def fatorial(n = 1, show = False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) para mostrar ou não o cálculo.
    :return: O valor fatorial de um número n.

    """
    f =1
    for c in range (n, 0,-1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c

    return f
    
     


num = int(input('Digite um número: '))
resposta = fatorial(num, show = True)
print(f'{resposta}')
help(fatorial)
