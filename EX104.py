def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\33[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digiou o número {n}.')
