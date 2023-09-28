from EX109_moeda import *

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda(p)} é {metade(p,True)}')
print(f'o dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando em 15%, temos {aumentar(p,15,True)}')
print(f'Reduzindo em 20%, temos {diminuir(p,20,True)}')
