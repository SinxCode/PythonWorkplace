from EX108 import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando em 15%, temos {moeda.aumentar(p,15)}')
print(f'Reduzindo em 20%, temos {moeda.diminuir(p,20)}')
