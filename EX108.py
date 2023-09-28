from EX108_moeda import *

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'o dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando em 15%, temos {moeda(aumentar(p,15))}')
print(f'Reduzindo em 20%, temos {moeda(diminuir(p,20))}')
