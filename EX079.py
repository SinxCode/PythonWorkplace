lista = []
valor = 0
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Digite um valor não duplicado')
    resposta = input('Deseja digitar outro valor? [S/N]').strip().upper()
    if resposta == 'N':
        break
lista.sort()
print(f'Os valores digitados foram: {lista}')
print('Fim')
