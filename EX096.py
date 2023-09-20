def area(l,c):
    a = l * c
    print(f'A área de um terreno {l:.2f}x{c:.2f} é de: {a:.2f}')


def lin():
    print('=-'*30)


lin()
print(f'{"CONTROLE DE TERRENOS":^55}')
lin()
l = float(input('Informe a largura do terreno (m): '))
c = float(input('Informe o comprimento do terreno(m): '))
lin()
area(l, c)