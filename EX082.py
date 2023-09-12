lista = list()
par = list()
impar = list()

while True:
    v = int(input('Digite um valor: '))
    resposta = input('Deseja digiar outro valor? [S/N] ').strip().upper()
    lista.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
    if resposta == 'N':
        break
print(f'Os valores digitados foram: {lista}')
print(f'Os valores PARES digitados foram: {par}')
print(f'Os valores IMPARES digitados foram: {impar}')