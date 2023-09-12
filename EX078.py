lista = list()
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor inteiro: ')))
    if c ==0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior valor digitado é {maior} nas posições: ',end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}; ',end='')
print(f'\nO menor valor digitado é {menor} nas posições: ',end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}; ',end='')
