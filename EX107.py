import EX107_moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de {p} é {EX107_moeda.metade(p)}')
print(f'o dobro de {p} é {EX107_moeda.dobro(p)}')
print(f'Aumentando em 15%, temos {EX107_moeda.aumentar(p,15)}')
print(f'Reduzindo em 20%, temos {EX107_moeda.diminuir(p,20)}')
