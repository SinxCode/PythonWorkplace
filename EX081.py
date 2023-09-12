lista = list()
c = 0
c5 = 0
while True:
    v = int(input('Digite um valor:'))
    lista.append(v)
    resposta = input('Deseja digitar outro número? [S/N]').strip().upper()
    if resposta == 'N':
        break
    if v == 5:
        c5 = c5 + 1
    c = c + 1
lista.sort(reverse=True)
print(f'Foram digitados {c+1} valores!')
print(f'Os números digitados foram: {lista}')
print(f'O número 5 foi digitado {c5} vezes.')


