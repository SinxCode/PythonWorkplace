listagem = ('LÁPIS', 1.75,
            'BORRACHA', 2,
            'CADERNO', 15.90,
            'ESTOJO', 25,
            'TRANSFERIDOR',4.20,
            'COMPASSO', 9.99,
            'MOCHILA', 120.32,
            'CANETAS', 22.30,
            'LIVRO', 34.90)
print('-=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^55}')
print('-=' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 ==0: #Isso pois cada nome de produto esta em um index par dentro da tupla
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-=' * 30)